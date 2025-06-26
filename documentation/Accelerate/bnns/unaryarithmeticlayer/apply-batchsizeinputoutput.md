# apply(batchSize:input:output:)

**Framework**: Accelerate  
**Kind**: method

Applies the layer to a set of input objects, writing the result to a set of output objects.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst ?+
- macOS 11.0+
- tvOS 14.0+
- watchOS 7.0+
- Unknown ?+ - Deprecated
- visionOS ?+

## Declaration

```swift
func apply(batchSize: Int, input: BNNSNDArrayDescriptor, output: BNNSNDArrayDescriptor) throws
```

## Parameters

- `batchSize`: The number of input-output pairs.
- `input`: The descriptor of the input.
- `output`: The descriptor of the output.

## See Also

- [func applyBackward(batchSize: Int, input: BNNSNDArrayDescriptor, output: BNNSNDArrayDescriptor, outputGradient: BNNSNDArrayDescriptor, generatingInputGradient: BNNSNDArrayDescriptor) throws](bnns/unaryarithmeticlayer/applybackward(batchsize:input:output:outputgradient:generatinginputgradient:).md)
  Applies the layer backward to generate input gradients.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnns/unaryarithmeticlayer/apply(batchsize:input:output:))*