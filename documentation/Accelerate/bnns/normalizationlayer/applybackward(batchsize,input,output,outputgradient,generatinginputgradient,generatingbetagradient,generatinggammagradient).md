# applyBackward(batchSize:input:output:outputGradient:generatingInputGradient:generatingBetaGradient:generatingGammaGradient:)

**Framework**: Accelerate  
**Kind**: method  
**Role**: Instance Method

Applies the layer backward to generate input gradients.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS
- watchOS 7.0+

> **Deprecated**: Use the BNNSGraph API instead.

## Declaration

```swift
func applyBackward(batchSize: Int, input: BNNSNDArrayDescriptor, output: BNNSNDArrayDescriptor, outputGradient: BNNSNDArrayDescriptor, generatingInputGradient inputGradient: BNNSNDArrayDescriptor, generatingBetaGradient betaGradient: BNNSNDArrayDescriptor? = nil, generatingGammaGradient gammaGradient: BNNSNDArrayDescriptor? = nil) throws
```

## Parameters

- `batchSize`: The number of input-output pairs.
- `input`: The descriptor of the input.
- `output`: The descriptor of the output.
- `outputGradient`: The descriptor of the output gradient.
- `inputGradient`: The descriptor of the input gradient.
- `betaGradient`: The descriptor of the beta gradient.
- `gammaGradient`: The descriptor of the gamma gradient.

## See Also

### Applying a Normalization Layer
- [func apply(batchSize: Int, input: BNNSNDArrayDescriptor, output: BNNSNDArrayDescriptor, for: BNNS.LearningPhase) throws](./apply%28batchsize,input,output,for%29.md)
  Applies the layer to a set of input objects, writing the result to a set of output objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnns/normalizationlayer/applybackward(batchsize:input:output:outputgradient:generatinginputgradient:generatingbetagradient:generatinggammagradient:))*