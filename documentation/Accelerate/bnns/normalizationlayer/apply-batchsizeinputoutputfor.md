# apply(batchSize:input:output:for:)

**Framework**: Accelerate  
**Kind**: method

Applies the layer to a set of input objects, writing the result to a set of output objects.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst ?+
- macOS 11.0+
- tvOS 14.0+
- visionOS ?+
- watchOS 7.0+
- Unknown ?+ - Deprecated

## Declaration

```swift
func apply(batchSize: Int, input: BNNSNDArrayDescriptor, output: BNNSNDArrayDescriptor, for learningPhase: BNNS.LearningPhase) throws
```

## Parameters

- `batchSize`: The number of input-output pairs.
- `input`: The descriptor of the input.
- `output`: The descriptor of the output.
- `learningPhase`: An enumeration that specifies whether the function call context is training or inference.

## See Also

- [func applyBackward(batchSize: Int, input: BNNSNDArrayDescriptor, output: BNNSNDArrayDescriptor, outputGradient: BNNSNDArrayDescriptor, generatingInputGradient: BNNSNDArrayDescriptor, generatingBetaGradient: BNNSNDArrayDescriptor?, generatingGammaGradient: BNNSNDArrayDescriptor?) throws](bnns/normalizationlayer/applybackward(batchsize:input:output:outputgradient:generatinginputgradient:generatingbetagradient:generatinggammagradient:).md)
  Applies the layer backward to generate input gradients.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnns/normalizationlayer/apply(batchsize:input:output:for:))*