# BNNS.NormalizationLayer

**Framework**: Accelerate  
**Kind**: class

A layer object that wraps a normalization filter and manages its deinitialization.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst ?+
- macOS 11.0+
- tvOS 14.0+
- visionOS ?+
- watchOS 7.0+

## Declaration

```swift
class NormalizationLayer
```

## Topics

### Creating a Normalization Layer
- [convenience init?(type: BNNS.NormalizationType, input: BNNSNDArrayDescriptor, output: BNNSNDArrayDescriptor, beta: BNNSNDArrayDescriptor, gamma: BNNSNDArrayDescriptor, momentum: Float, epsilon: Float, activation: BNNS.ActivationFunction, filterParameters: BNNSFilterParameters?)](bnns/normalizationlayer/init(type:input:output:beta:gamma:momentum:epsilon:activation:filterparameters:).md)
  Returns a new normalization layer.
### Specifying a Normalization Type
- [BNNS.NormalizationType](bnns/normalizationtype.md)
  Constants that describe normalization types.
### Applying a Normalization Layer
- [func apply(batchSize: Int, input: BNNSNDArrayDescriptor, output: BNNSNDArrayDescriptor, for: BNNS.LearningPhase) throws](bnns/normalizationlayer/apply(batchsize:input:output:for:).md)
  Applies the layer to a set of input objects, writing the result to a set of output objects.
- [func applyBackward(batchSize: Int, input: BNNSNDArrayDescriptor, output: BNNSNDArrayDescriptor, outputGradient: BNNSNDArrayDescriptor, generatingInputGradient: BNNSNDArrayDescriptor, generatingBetaGradient: BNNSNDArrayDescriptor?, generatingGammaGradient: BNNSNDArrayDescriptor?) throws](bnns/normalizationlayer/applybackward(batchsize:input:output:outputgradient:generatinginputgradient:generatingbetagradient:generatinggammagradient:).md)
  Applies the layer backward to generate input gradients.
### Specifying the Learning Phase
- [BNNS.LearningPhase](bnns/learningphase.md)
  Constants that describe the learning phase of a normalization operation.

## Relationships

### Inherits From
- [BNNS.Layer](bnns/layer.md)

## See Also

- [struct BNNSLayerParametersNormalization](bnnslayerparametersnormalization.md)
  A structure that contains the parameters of a normalization layer.
- [func BNNSFilterCreateLayerNormalization(BNNSFilterType, UnsafePointer<BNNSLayerParametersNormalization>, UnsafePointer<BNNSFilterParameters>?) -> BNNSFilter?](bnnsfiltercreatelayernormalization(_:_:_:).md)
  Returns a new normalization layer.
- [func BNNSNormalizationFilterApplyBatch(BNNSFilter?, Int, UnsafeRawPointer, Int, UnsafeMutableRawPointer, Int, Bool) -> Int32](bnnsnormalizationfilterapplybatch(_:_:_:_:_:_:_:).md)
  Applies a normalization filter to a set of input objects, writing the result to a set of output objects.
- [func BNNSNormalizationFilterApplyBackwardBatch(BNNSFilter?, Int, UnsafeMutablePointer<BNNSNDArrayDescriptor>?, Int, UnsafeRawPointer?, Int, UnsafeMutablePointer<BNNSNDArrayDescriptor>, Int, UnsafeMutablePointer<BNNSNDArrayDescriptor>?, UnsafeMutablePointer<BNNSNDArrayDescriptor>?) -> Int32](bnnsnormalizationfilterapplybackwardbatch(_:_:_:_:_:_:_:_:_:_:).md)
  Applies a normalization filter backward to generate gradients.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnns/normalizationlayer)*