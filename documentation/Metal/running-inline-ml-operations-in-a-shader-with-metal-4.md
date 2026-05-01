# Running inline ML operations in a shader with Metal 4

**Framework**: Metal

Multiply matrices across multiple GPU cores with inline tensor operations.

**Availability**:
- macOS 26.0+
- Xcode 26.0+

#### Overview

This sample code project demonstrates how to run matrix multiplications in a GPU kernel function with inline tensor operations, which are available in Metal Shading Language 4 and later. The sample app multiplies two matrices in a single GPU dispatch, and verifies the result by comparing it to a CPU-based reference implementation.

The sample’s GPU kernel function runs the matrix multiplication in parallel by invoking a Metal 4 tensor operation, which distributes the workload across multiple GPU cores. The kernel stores intermediate results in a cooperative tensor, which keeps the data in register memory, and avoids the latency of writing to device or threadgroup memory. The sample’s implementation of the kernel is minimal because Apple silicon GPUs don’t require an explicit software pipeline to overlap memory and compute operations. For GPUs in the [`MTLGPUFamily.apple10`](mtlgpufamily/apple10.md) GPU family, and later, each core has a neural accelerator that improves runtime performance by running tensor operations directly in hardware.

> **Note**: For a list of chips in each GPU family, see [`Metal Feature Set Tables (PDF)`](https://developer.apple.comhttps://developer.apple.com/metal/Metal-Feature-Set-Tables.pdf).

For more information about how the app creates tensors on the CPU side and passes them to the GPU kernel with an argument table, see [`Running a machine learning model on the GPU timeline`](running-a-machine-learning-model-on-the-gpu-timeline.md).

#### Bind Tensors to the Kernel

The kernel function declares three `tensor` parameters for the matrix multiplicand, multiplier, and product. Each parameter declares a rank-2 tensor with an extents type of `dextents<int, 2>`.

```metal
kernel void
matrix_multiplication_kernel(uint2 threadgroupIdentifier [[threadgroup_position_in_grid]],
                             tensor<device half, dextents<int, 2>> sourceA,
                             tensor<device half, dextents<int, 2>> sourceB,
                             tensor<device half, dextents<int, 2>> destination)
```

The kernel reads the extents from each tensor’s metadata at runtime.

> **Note**: Tensor operations require an index type of `int` for the tensors you pass to them.

#### Slice the Input and Output Tensors

The kernel divides the matrix multiplication into a hierarchy of tiles by dispatching threadgroups across the tensors. Each threadgroup computes one tile of the output with SIMD groups by slicing portions of the input and destination tensors it’s responsible for.

```metal
const int TileSize = 64;
int tileOriginX = TileSize * threadgroupIdentifier.x;
int tileOriginY = TileSize * threadgroupIdentifier.y;

auto sliceA = sourceA.slice<dynamic_extent, TileSize>(0, tileOriginY);
auto sliceB = sourceB.slice<TileSize, dynamic_extent>(tileOriginX, 0);
auto destinationSlice = destination.slice<TileSize, TileSize>(tileOriginX, tileOriginY);
```

The kernel sets the size of each output tile by passing static extent template parameters to the `slice()` member function. The inner dimension of each input tensor uses `dynamic_extent`, so the compiler infers the shared dimension from the source tensor’s extent rather than requiring a fixed size.

> 💡 **Tip**: When you know the tile size at compile time, pass static extents to `slice()` as template parameters. The operation avoids per-element bounds checks that dynamic extents require.

Static extents let the operation skip edge handling, which improves runtime performance.

#### Create a Matrix Multiplication Operation

To configure the matrix multiplication, the kernel creates a `matmul2d_descriptor` that describes the output tile’s height, width, and inner dimension.

```metal
constexpr auto descriptor = matmul2d_descriptor(TileSize,
                                                TileSize,
                                                dynamic_length_v<int>);
```

The first two parameters set the output tile’s height and width to `TileSize`, so each threadgroup produces a 64 x 64 tile. The third parameter passes `dynamic_length_v<int>`, which tells the operation to infer the inner dimension from the extents of the input tensors at runtime.

The kernel passes the descriptor as a template parameter to `matmul2d`, so the compiler generates the most efficient implementation for those dimensions.

```metal
matmul2d<descriptor, execution_simdgroups<4>> operation;
```

The `execution_simdgroups<4>` template parameter defines the operation’s *execution scope*, the four SIMD groups from the threadgroup that participate in the computation together.

For more information about tensor operations, see section 7.2 of the [`Metal Shading Language Specification (PDF)`](https://developer.apple.comhttps://developer.apple.com/metal/Metal-Shading-Language-Specification.pdf).

#### Capture the Result in a Cooperative Tensor

To avoid the latency of writing intermediate results to device or threadgroup memory, the kernel captures the output of the matrix multiplication in a cooperative tensor. It creates a cooperative tensor by passing the input slice types and the output element type as template parameters to `get_destination_cooperative_tensor()`.

```metal
auto cooperativeTensor = operation.get_destination_cooperative_tensor<decltype(sliceA),
                                                                      decltype(sliceB),
                                                                      half>();
```

A cooperative tensor distributes its elements across the threads in the execution scope by storing them in the register memory of each thread’s GPU core rather than in a contiguous block of device or threadgroup memory. With a cooperative tensor, the kernel directly accesses the subset of elements that belong to the current thread, which avoids the time it takes to read from, and write to, memory.

> **Note**: Apple silicon GPUs don’t require threadgroup memory staging for tensor operations because the on-chip memory hierarchy reuses memory with its caching.

The kernel invokes the matrix multiplication operation by calling its `run()` member function with two slices for the operands, and the cooperative tensor for the result.

```metal
operation.run(sliceA, sliceB, cooperativeTensor);
```

#### Combine an Element Wise Function

The kernel combines an activation function — an example of a *postfix* operation — by applying an element-wise function to the elements of the product matrix that are in thread-local memory. It calls the app’s `relu` function for each element it owns in the cooperative tensor.

```metal
auto threadElements = cooperativeTensor.get_capacity();
for (int element = 0; element < threadElements; element++)
{
    auto value = cooperativeTensor[element];
    cooperativeTensor[element] = relu(value);
}
```

The `get_capacity()` member function returns the number of elements in the cooperative tensor that belong to the calling thread.

The rectified linear unit (ReLU) activation function sets any negative value to zero.

```metal
half relu(half value) {
    return max(value, (half)0.0f);
}
```

> 💡 **Tip**: Combining operations within a single dispatch avoids runtime costs of loading and storing the results of additional GPU compute dispatches.

#### Store the Result

The kernel saves the final output to the destination tensor by passing the output slice to the cooperative tensor’s `store()` member function.

```metal
cooperativeTensor.store(destinationSlice);
```

The kernel saves each thread’s results from the cooperative tensor by calling `store()`. It passes `destinationSlice` because the slice represents the tile of the `destination` output tensor that belongs to the thread’s threadgroup.

## See Also

- [Running a machine learning model on the GPU timeline](running-a-machine-learning-model-on-the-gpu-timeline.md)
  Dispatch model inference commands with a machine learning pass in a Metal 4 command buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/running-inline-ml-operations-in-a-shader-with-metal-4)*