# BNNSComputeNormBackward(_:_:_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Backpropogates gradients for the compute norm function.

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
func BNNSComputeNormBackward(_ in: UnsafeRawPointer, _ in_delta: UnsafeMutablePointer<BNNSNDArrayDescriptor>, _ out: UnsafeRawPointer, _ out_delta: UnsafePointer<BNNSNDArrayDescriptor>, _ norm_type: BNNSNormType, _ axis_flags: UInt32) -> Int32
```

## Parameters

- `in`: The descriptor of the input.
- `in_delta`: The descriptor of the input delta.
- `out`: The descriptor of the output.
- `out_delta`: The descriptor of the output delta.
- `norm_type`: The type of the norm. This function supports only  .
- `axis_flags`: The dimensions that the function uses to compute the norm. Set to   to specify that the function computes the norm over all dimensions.

## See Also

- [static func computeNorm(input: BNNSNDArrayDescriptor, output: BNNSNDArrayDescriptor, axes: [Int]?) throws](bnns/computenorm(input:output:axes:).md)
  Computes the Euclidean norm and writes the result to the output tensor.
- [static func computeNormBackward(input: BNNSNDArrayDescriptor, output: BNNSNDArrayDescriptor, axes: [Int]?, outputGradient: BNNSNDArrayDescriptor, generatingInputGradient: BNNSNDArrayDescriptor) throws](bnns/computenormbackward(input:output:axes:outputgradient:generatinginputgradient:).md)
  Backpropogates gradients for the compute norm function.
- [func BNNSComputeNorm(UnsafeMutablePointer<BNNSNDArrayDescriptor>, UnsafePointer<BNNSNDArrayDescriptor>, BNNSNormType, UInt32) -> Int32](bnnscomputenorm(_:_:_:_:).md)
  Computes the specified norm over an entire tensor or the specified axes.
- [struct BNNSNormType](bnnsnormtype.md)
  Constants that describe norm types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnscomputenormbackward(_:_:_:_:_:_:))*