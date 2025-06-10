# computeNorm(input:output:axes:)

**Framework**: Accelerate  
**Kind**: method

Computes the Euclidean norm and writes the result to the output tensor.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst ?+
- macOS 12.0+
- tvOS 15.0+
- visionOS ?+
- watchOS 8.0+
- Unknown ?+ - Deprecated

## Declaration

```swift
static func computeNorm(input: BNNSNDArrayDescriptor, output: BNNSNDArrayDescriptor, axes: [Int]? = nil) throws
```

#### Discussion

Use this function to compute the norm of either an entire tensor or an axis or axes of a tensor.

For example, the following code defines a 3D tensor:

```swift
let inputValues: [Float] = [1, 2, 3,
                            4, 5, 6,
                            
                            10, 20, 30,
                            40, 50, 60,
                            
                            100, 200, 300,
                            400, 500, 600,
                            
                            1000, 2000, 3000,
                            4000, 5000, 6000]

let input = BNNSNDArrayDescriptor.allocate(
    initializingFrom: inputValues,
    shape: .imageCHW(3, 2, 4))
```

Define the `axes` parameter as either `[0, 1, 2]` or `nil` to specify that the operation computes the norm of the entire tensor. In this case, the norm is a scalar value, and the destination’s data layout must be a [`BNNS.DataLayout.vector`](bnns/datalayout/vector.md) with a size of `1`.

```swift
let output = BNNSNDArrayDescriptor.allocateUninitialized(
    scalarType: Float.self,
    shape: .vector(1))

try? BNNS.computeNorm(input: input,
                     output: output,
                     axes: [0, 1, 2])

// Prints `[9587.45]`.
print(output.makeArray(of: Float.self)!)
```

On return, the output descriptor contains a single value that is the square root of the sum of squares of each element in the tensor:

![A diagram that depicts a 3D tensor as four 2D planes along the channel axis. Each plane is two elements high and three elements wide. The compute norm operation calculates a single value for the norm of the entire tensor.](https://docs-assets.developer.apple.com/published/a829c34d4b4f4071bbaf72b10112a033/media-3786765%402x.png)

Specify an `axes` of `[2]` to compute the norms along the second axis. In this case, the destination must be a matrix with a size that matches the zeroth and first dimensions of the source tensor:

```swift
let output = BNNSNDArrayDescriptor.allocateUninitialized(
    scalarType: Float.self,
    shape: .matrixColumnMajor(3, 2))

try? BNNS.computeNorm(input: input,
                     output: output,
                     axes: [2])

// Prints
//      [1005.0378, 2010.075, 3015.113,
//       4020.1511, 5025.189, 6030.227]
print(output.makeArray(of: Float.self)!)
```

On return, the output descriptor contains six values that are the norms of the slices along the second axis of the input tensor:

![A diagram that depicts a 3D tensor as four 2D planes along the channel axis. Each plane is two elements high and three elements wide. The compute norm operation calculates separate norms for the six 4-element vectors along the channel axis.](https://docs-assets.developer.apple.com/published/be33dde19816c79781bdf5340a21e1a1/media-3786768%402x.png)

To compute the norm along more that one dimension, define the destination tensor with a size of the dimensions you’re not calculating over. For example, the following code defines an `axes` with a value of `[0, 2]` to compute the norm of dimensions zero and two:

```swift
let output = BNNSNDArrayDescriptor.allocateUninitialized(
    scalarType: Float.self,
    shape: .vector(2))

try? BNNS.computeNorm(input: input,
                     output: output,
                     axes: [0, 2])

// Prints `[3760.507, 8819.171]`
print(output.makeArray(of: Float.self)!)
```

On return, the output descriptor contains two values that are the norms of the top and bottom slices of the input tensor:

![A diagram that depicts a 3D tensor as four 2D planes along the channel axis. Each plane is two elements high and three elements wide. The compute norm operation calculates separate norms for the pair of three-by-four matrices defined by the channel axis and the width axis.](https://docs-assets.developer.apple.com/published/2c2a41e95612a64cab4fadb97d45b77d/media-3786762%402x.png)

## Parameters

- `input`: The descriptor of the input.
- `output`: The descriptor of the output.
- `axes`: The indices of the axes over which the function computes the norm. Set to   to specify that the function computes the norm over the entire tensor.

## See Also

- [static func computeNormBackward(input: BNNSNDArrayDescriptor, output: BNNSNDArrayDescriptor, axes: [Int]?, outputGradient: BNNSNDArrayDescriptor, generatingInputGradient: BNNSNDArrayDescriptor) throws](bnns/computenormbackward(input:output:axes:outputgradient:generatinginputgradient:).md)
  Backpropogates gradients for the compute norm function.
- [func BNNSComputeNorm(UnsafeMutablePointer<BNNSNDArrayDescriptor>, UnsafePointer<BNNSNDArrayDescriptor>, BNNSNormType, UInt32) -> Int32](bnnscomputenorm(_:_:_:_:).md)
  Computes the specified norm over an entire tensor or the specified axes.
- [func BNNSComputeNormBackward(UnsafeRawPointer, UnsafeMutablePointer<BNNSNDArrayDescriptor>, UnsafeRawPointer, UnsafePointer<BNNSNDArrayDescriptor>, BNNSNormType, UInt32) -> Int32](bnnscomputenormbackward(_:_:_:_:_:_:).md)
  Backpropogates gradients for the compute norm function.
- [struct BNNSNormType](bnnsnormtype.md)
  Constants that describe norm types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnns/computenorm(input:output:axes:))*