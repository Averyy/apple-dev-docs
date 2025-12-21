# computeNormBackward(input:output:axes:outputGradient:generatingInputGradient:)

**Framework**: Accelerate  
**Kind**: method

Backpropogates gradients for the compute norm function.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst ?+
- macOS 12.0+
- tvOS 15.0+
- visionOS ?+
- watchOS 8.0+

## Declaration

```swift
static func computeNormBackward(input: BNNSNDArrayDescriptor, output: BNNSNDArrayDescriptor, axes: [Int]? = nil, outputGradient: BNNSNDArrayDescriptor, generatingInputGradient inputGradient: BNNSNDArrayDescriptor) throws
```

## Parameters

- `input`: The descriptor of the input.
- `output`: The descriptor of the output.
- `axes`: The indices of the axes over which the function computes the norm. Set to   to specify that the function computes the norm over the entire tensor.
- `outputGradient`: The descriptor of the output delta.
- `inputGradient`: The descriptor of the input delta.

## See Also

- [static func computeNorm(input: BNNSNDArrayDescriptor, output: BNNSNDArrayDescriptor, axes: [Int]?) throws](bnns/computenorm(input:output:axes:).md)
  Computes the Euclidean norm and writes the result to the output tensor.
- [func BNNSComputeNorm(UnsafeMutablePointer<BNNSNDArrayDescriptor>, UnsafePointer<BNNSNDArrayDescriptor>, BNNSNormType, UInt32) -> Int32](bnnscomputenorm(_:_:_:_:).md)
  Computes the specified norm over an entire tensor or the specified axes.
- [func BNNSComputeNormBackward(UnsafeRawPointer, UnsafeMutablePointer<BNNSNDArrayDescriptor>, UnsafeRawPointer, UnsafePointer<BNNSNDArrayDescriptor>, BNNSNormType, UInt32) -> Int32](bnnscomputenormbackward(_:_:_:_:_:_:).md)
  Backpropogates gradients for the compute norm function.
- [struct BNNSNormType](bnnsnormtype.md)
  Constants that describe norm types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnns/computenormbackward(input:output:axes:outputgradient:generatinginputgradient:))*