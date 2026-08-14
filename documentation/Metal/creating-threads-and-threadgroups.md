# Creating threads and threadgroups

**Framework**: Metal

Learn how Metal organizes compute-processing workloads.

#### Overview

A compute pass can run a kernel function over a 1D, 2D, or 3D grid. Each point in the grid represents a *thread*, which is a single  instance of your kernel function. For example, in image processing, the grid is typically a 2D matrix of threads—representing the entire image—with each thread corresponding to a single pixel of the image being processed.

Each thread belongs to a *threadgroup* that run together and share a common block of memory. You can design your kernel functions so that each thread runs independently, or so that they collaborate as a group on a common working set.

##### Identification of Threads By Position in Grid

[`Figure 1`](compute_passes/creating_threads_and_threadgroups#2928936.md) shows how an image being processed by a compute kernel is divided into threadgroups and how each threadgroup is composed of individual threads. Each thread processes a single pixel.

![A grid divided into threadgroups that are composed of individual threads.](/images/com.apple.metal/creating-threads-and-threadgroups-1@2x.png)

You can identify a thread by its position in the grid, which is a unique position that gives your kernel function the ability to do something different for each thread. The example kernel function below — from [`Combining blit and compute operations in a single pass`](combining-blit-and-compute-operations-in-a-single-pass.md) — has a `gridID` parameter, a vector that represents each thread’s 2D coordinates, which it applies when reading one and writing to another texture.

```metal
kernel void
convertToGrayscale(texture2d<half, access::read>  inTexture  [[texture(ComputeTextureBindingIndexForColorImage)]],
                   texture2d<half, access::write> outTexture [[texture(ComputeTextureBindingIndexForGrayscaleImage)]],
                   uint2                          gridId     [[thread_position_in_grid]])
{

    // Check that this part of the grid is within the texture's bounds.
    if ((gridId.x >= outTexture.get_width()) ||
        (gridId.y >= outTexture.get_height()))
    {
        // Exit early for coordinates outside the bounds of the destination.
        return;
    }

    /// The input texture's data value at the thread's coordinates.
    half4 colorValue  = inTexture.read(gridId);

    /// A grayscale equivalent of the input texture's color value.
    half grayValue = dot(colorValue.rgb, kRec709LumaCoefficients);

    // Save the grayscale value to the output texture at the thread's coordinates.
    outTexture.write(half4(grayValue, grayValue, grayValue, 1.0), gridId);
}
```

`[[thread_position_in_grid]]` is an *attribute qualifier*. Attribute qualifiers, identifiable by their double square-bracket syntax, allow kernel parameters to be bound to resources and built-in variables — in this case, the thread’s position in the grid to the kernel function.

For example, given a grid of 16 x 16 threads partitioned into 2 x 4 threadgroups of 8 x 4 threads, a single thread (shown in [`Figure 2`](compute_passes/creating_threads_and_threadgroups#2929009.md) in red) has a position in the grid of (9,10):

![The position of a single thread in a 16 x 16 grid.](/images/com.apple.metal/creating-threads-and-threadgroups-2@2x.png)

##### Identification of Threads By Position in Threadgroup

A thread’s position in its threadgroup is also available as the attribute qualifier `[[thread_position_in_threadgroup]]`, and a threadgroup’s position in the grid is available as `[[threadgroup_position_in_grid]]`.

Depending on the shape of the grid, these position attributes are either a scalar value, or a two- or three-element vector. In the case of a 2D grid, position attributes are two-element vectors, with the origin at the top-left.

The thread identified in [`Figure 2`](compute_passes/creating_threads_and_threadgroups#2929009.md) is in the threadgroup with a position in the grid of (1,2), and its position in that threadgroup is (1,2), as shown in [`Figure 3`](compute_passes/creating_threads_and_threadgroups#2929421.md):

![The position of a single thread in a threadgroup.](/images/com.apple.metal/creating-threads-and-threadgroups-3@2x.png)

Using the following code, you can also calculate a thread’s position in the grid based on its position in its threadgroup and that threadgroup’s size and position in the grid:

```metal
kernel void 
myKernel(uint2 threadgroup_position_in_grid   [[ threadgroup_position_in_grid ]],
         uint2 thread_position_in_threadgroup [[ thread_position_in_threadgroup ]],
         uint2 threads_per_threadgroup        [[ threads_per_threadgroup ]]) 
{
    
    uint2 thread_position_in_grid = 
        (threadgroup_position_in_grid * threads_per_threadgroup) + 
        thread_position_in_threadgroup;
}
```

##### Simd Groups

The threads in a threadgroup are further organized into single-instruction, multiple-data (SIMD) groups, also known as *warps* or *wavefronts*, that execute concurrently. The threads in a SIMD group execute the same code. Avoid writing code that could cause your kernel function to *diverge*; that is, to follow different code paths. A typical example of divergence is caused by using an *if* statement. Even if a single thread in a SIMD group takes a different path from the others, all threads in that group execute both branches, and the execution time for the group is the sum of the execution time of both branches.

The division of threadgroups into SIMD groups is defined by Metal. It remains constant for the duration of a kernel’s execution, across dispatches of a given kernel with the same launch parameters, and from one threadgroup to another within the dispatch.

The number of threads in a SIMD group is returned by the [`threadExecutionWidth`](mtlcomputepipelinestate/threadexecutionwidth.md) of your compute pipeline state object. Attribute qualifiers allow you to access a SIMD group’s scalar index within a threadgroup, and a thread’s scalar index within a SIMD group:

- **`[[simdgroup_index_in_threadgroup]]`**: The unique scalar index of a SIMD group in its threadgroup.
- **`[[thread_index_in_simdgroup]]`**: The unique scalar index of a thread in its SIMD group, also known as the *lane ID*.

Although threadgroups can be multidimensional, SIMD groups are 1D. Therefore, a thread’s position within a SIMD group is a scalar value for all threadgroup shapes. The SIMD group size remains constant and is unaffected by the threadgroup size.

For example, using the same 16 x 16 grid shown in [`Figure 2`](compute_passes/creating_threads_and_threadgroups#2929009.md), with a thread execution width of 16, a single 8 x 4 threadgroup consists of 2 SIMD groups. Because a SIMD group contains 16 threads, each SIMD group constitutes 2 rows in the threadgroup:

![A threadgroup composed of 2 SIMD groups.](/images/com.apple.metal/creating-threads-and-threadgroups-4@2x.png)

The thread shown in red in [`Figure 5`](compute_passes/creating_threads_and_threadgroups#2929426.md) has a `[[simdgroup_index_in_threadgroup]]` value of 1 and a `[[thread_index_in_simdgroup]]` value of 1:

![The position of a single thread in a SIMD group.](/images/com.apple.metal/creating-threads-and-threadgroups-5@2x.png)

## See Also

- [Calculating threadgroup and grid sizes](calculating-threadgroup-and-grid-sizes.md)
  Calculate the optimum sizes for threadgroups and grids when dispatching compute-processing workloads.
- [protocol MTL4ComputeCommandEncoder](mtl4computecommandencoder.md)
  Encodes computation dispatches, resource copying commands, and acceleration structure building commands for a single pass into a command buffer.
- [protocol MTLComputeCommandEncoder](mtlcomputecommandencoder.md)
  Encodes computation dispatch commands for a single compute pass into a command buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/creating-threads-and-threadgroups)*