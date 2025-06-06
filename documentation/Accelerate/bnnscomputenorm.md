# BNNSComputeNorm(_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Computes the specified norm over an entire tensor or the specified axes.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
func BNNSComputeNorm(_ dest: UnsafeMutablePointer<BNNSNDArrayDescriptor>, _ src: UnsafePointer<BNNSNDArrayDescriptor>, _ norm_type: BNNSNormType, _ axis_flags: UInt32) -> Int32
```

#### Discussion

Use this function to compute the norm of either an entire tensor or the axis or axes of a tensor.

For example, the following code defines a 3D tensor:

```swift
let inputData = UnsafeMutableBufferPointer<Float>.allocate(capacity: 24)
_ = inputData.initialize(from: [1, 2, 3,
                                4, 5, 6,
                                
                                10, 20, 30,
                                40, 50, 60,
                                
                                100, 200, 300,
                                400, 500, 600,
                                
                                1000, 2000, 3000,
                                4000, 5000, 6000])
var inputDescriptor = BNNSNDArrayDescriptor(flags: BNNSNDArrayFlags(0),
                                            layout: BNNSDataLayoutImageCHW,
                                            size: (3, 2, 4, 0, 0, 0, 0, 0),
                                            stride: (0, 0, 0, 0, 0, 0, 0, 0),
                                            data: inputData.baseAddress!,
                                            data_type: BNNSDataType.float,
                                            table_data: nil,
                                            table_data_type: BNNSDataType.float,
                                            data_scale: 1, data_bias: 0)
```

Define the `axis_flags` parameter as either `0b111` or `0` to specify that the operation computes the norm of the entire tensor. In this case, the norm is a scalar value, and the destination’s data layout must be a `BNNSDataLayoutVector` with a size of `1`.

```swift
let outputData = UnsafeMutableBufferPointer<Float>.allocate(capacity: 1)
var outputDescriptor = BNNSNDArrayDescriptor(flags: BNNSNDArrayFlags(0),
                                             layout: BNNSDataLayoutVector,
                                             size: (1, 0, 0, 0, 0, 0, 0, 0),
                                             stride: (0, 0, 0, 0, 0, 0, 0, 0),
                                             data: outputData.baseAddress!,
                                             data_type: BNNSDataType.float,
                                             table_data: nil,
                                             table_data_type: BNNSDataType.float,
                                             data_scale: 1, data_bias: 0)

BNNSComputeNorm(&outputDescriptor,
                 &inputDescriptor,
                 BNNSL2Norm,
                 0b111)

// Prints `[9587.45]`
print(Array(outputData))
```

On return, the output descriptor contains a single value that is the square root of the sum of squares of each element in the tensor:

![A diagram that depicts a 3D tensor as four 2D planes along the channel axis. Each plane is two elements high and three elements wide. The compute norm operation calculates a single value for the norm of the entire tensor.](https://docs-assets.developer.apple.com/published/a829c34d4b4f4071bbaf72b10112a033/media-3761084%402x.png)

Specify an `axis_flags` of `0b100` to compute the norm along the second axis. In this case, the destination should be a matrix with a size that matches the zeroth and first dimensions of the source tensor:

```swift
let outputData = UnsafeMutableBufferPointer<Float>.allocate(capacity: 6)
var outputDescriptor = BNNSNDArrayDescriptor(flags: BNNSNDArrayFlags(0),
                                             layout: BNNSDataLayoutColumnMajorMatrix,
                                             size: (3, 2, 0, 0, 0, 0, 0, 0),
                                             stride: (0, 0, 0, 0, 0, 0, 0, 0),
                                             data: outputData.baseAddress!,
                                             data_type: BNNSDataType.float,
                                             table_data: nil,
                                             table_data_type: BNNSDataType.float,
                                             data_scale: 1, data_bias: 0)

BNNSComputeNorm(&outputDescriptor,
                 &inputDescriptor,
                 BNNSL2Norm,
                 0b100)

// Prints
//      [1005.0378, 2010.075, 3015.113,
//       4020.1511, 5025.189, 6030.227]
print(Array(outputData))
```

On return, the output descriptor contains six values that are the norms of the slices along the second axis of the input tensor:

![A diagram that depicts a 3D tensor as four 2D planes along the channel axis. Each plane is two elements high and three elements wide. The compute norm operation calculates separate norms for the six 4-element vectors along the channel axis.](https://docs-assets.developer.apple.com/published/be33dde19816c79781bdf5340a21e1a1/media-3761079%402x.png)

To compute the norm along more that one dimension, define the destination tensor with a size of the dimensions you’re not calculating over. For example, the following code defines an `axis_flags` with a value of `0b101` to compute the norm of dimensions zero and two:

```swift
let outputData = UnsafeMutableBufferPointer<Float>.allocate(capacity: 2)
var outputDescriptor = BNNSNDArrayDescriptor(flags: BNNSNDArrayFlags(0),
                                             layout: BNNSDataLayoutVector,
                                             size: (2, 0, 0, 0, 0, 0, 0, 0),
                                             stride: (0, 0, 0, 0, 0, 0, 0, 0),
                                             data: outputData.baseAddress!,
                                             data_type: BNNSDataType.float,
                                             table_data: nil,
                                             table_data_type: BNNSDataType.float,
                                             data_scale: 1, data_bias: 0)

BNNSComputeNorm(&outputDescriptor,
                 &inputDescriptor,
                 BNNSL2Norm,
                 0b101)

// Prints `[3760.507, 8819.171]`
print(Array(outputData))
```

On return, the output descriptor contains two values that are the norms of the top and bottom slices of the input tensor:

![A diagram that depicts a 3D tensor as four 2D planes along the channel axis. Each plane is two elements high and three elements wide. The compute norm operation calculates separate norms for the pair of three-by-four matrices defined by the channel axis and the width axis.](https://docs-assets.developer.apple.com/published/2c2a41e95612a64cab4fadb97d45b77d/media-3761082%402x.png)

## Parameters

- `dest`: The descriptor of the output.
- `src`: The descriptor of the input.
- `norm_type`: The type of the norm. This function supports only  .
- `axis_flags`: The dimensions that the function uses to compute the norm. Set to   to specify that the function computes the norm over all dimensions.

## See Also

- [static func computeNorm(input: BNNSNDArrayDescriptor, output: BNNSNDArrayDescriptor, axes: [Int]?) throws](bnns/computenorm(input:output:axes:).md)
  Computes the Euclidean norm and writes the result to the output tensor.
- [static func computeNormBackward(input: BNNSNDArrayDescriptor, output: BNNSNDArrayDescriptor, axes: [Int]?, outputGradient: BNNSNDArrayDescriptor, generatingInputGradient: BNNSNDArrayDescriptor) throws](bnns/computenormbackward(input:output:axes:outputgradient:generatinginputgradient:).md)
  Backpropogates gradients for the compute norm function.
- [func BNNSComputeNormBackward(UnsafeRawPointer, UnsafeMutablePointer<BNNSNDArrayDescriptor>, UnsafeRawPointer, UnsafePointer<BNNSNDArrayDescriptor>, BNNSNormType, UInt32) -> Int32](bnnscomputenormbackward(_:_:_:_:_:_:).md)
  Backpropogates gradients for the compute norm function.
- [struct BNNSNormType](bnnsnormtype.md)
  Constants that describe norm types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnscomputenorm(_:_:_:_:))*