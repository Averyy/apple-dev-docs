# BNNS.FusedFullyConnectedNormalizationLayer

**Framework**: Accelerate  
**Kind**: class

A layer object that wraps a fused, fully connected normalization layer and manages its deinitialization.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS ?+
- watchOS 7.0+
- Unknown ?+ - Deprecated
- Mac Catalyst ?+

## Declaration

```swift
class FusedFullyConnectedNormalizationLayer
```

## Topics

### Creating a Fused, Fully Connected Normalization Layer
- [convenience init?(input: BNNSNDArrayDescriptor, output: BNNSNDArrayDescriptor, fullyConnectedWeights: BNNSNDArrayDescriptor, fullyConnectedBias: BNNSNDArrayDescriptor?, normalization: BNNS.NormalizationType, normalizationBeta: BNNSNDArrayDescriptor, normalizationGamma: BNNSNDArrayDescriptor, normalizationMomentum: Float, normalizationEpsilon: Float, normalizationActivation: BNNS.ActivationFunction, filterParameters: BNNSFilterParameters?)](bnns/fusedfullyconnectednormalizationlayer/init(input:output:fullyconnectedweights:fullyconnectedbias:normalization:normalizationbeta:normalizationgamma:normalizationmomentum:normalizationepsilon:normalizationactivation:filterparameters:).md)
  Returns a new fused, fully connected normalization layer.
### Applying a Fused Layer
- [func apply(batchSize: Int, input: BNNSNDArrayDescriptor, output: BNNSNDArrayDescriptor, for: BNNS.LearningPhase) throws](bnns/fusedlayer/apply(batchsize:input:output:for:).md)
  Applies the layer to a set of input objects, writing the result to a set of output objects.
### Specifying the Learning Phase
- [BNNS.LearningPhase](bnns/learningphase.md)
  Constants that describe the learning phase of a normalization operation.

## Relationships

### Inherits From
- [BNNS.FusedLayer](bnns/fusedlayer.md)

## See Also

- [protocol FusableLayerParameters](fusablelayerparameters.md)
- [class FusedParametersLayer](bnns/fusedparameterslayer.md)
  A layer object that wraps a fused layer and manages its deinitialization.
- [class FusedConvolutionNormalizationLayer](bnns/fusedconvolutionnormalizationlayer.md)
  A layer object that wraps a fused, convolution normalization layer and manages its deinitialization.
- [struct BNNSFilterType](bnnsfiltertype.md)
  Constants that define the component filters of a fused layer.
- [func BNNSFilterCreateFusedLayer(Int, UnsafePointer<BNNSFilterType>, UnsafeMutablePointer<UnsafeRawPointer>, UnsafePointer<BNNSFilterParameters>?) -> BNNSFilter?](bnnsfiltercreatefusedlayer(_:_:_:_:).md)
  Returns a new fused layer.
- [func BNNSFusedFilterApplyBatch(BNNSFilter?, Int, UnsafeRawPointer, Int, UnsafeMutableRawPointer, Int, Bool) -> Int32](bnnsfusedfilterapplybatch(_:_:_:_:_:_:_:).md)
  Applies a fused filter to a set of input objects, writing the result to a set of output objects.
- [func BNNSFusedFilterApplyMultiInputBatch(BNNSFilter?, Int, Int, UnsafeMutablePointer<UnsafeRawPointer>, UnsafePointer<Int>, UnsafeMutableRawPointer, Int, Bool) -> Int32](bnnsfusedfilterapplymultiinputbatch(_:_:_:_:_:_:_:_:).md)
  Applies a multiple-input fused filter to a set of input objects, writing the result to a set of output objects.
- [func BNNSFusedFilterApplyBackwardBatch(BNNSFilter?, Int, UnsafeRawPointer?, Int, UnsafeMutablePointer<BNNSNDArrayDescriptor>?, Int, UnsafeRawPointer?, Int, UnsafeMutablePointer<BNNSNDArrayDescriptor>, Int, UnsafeMutablePointer<UnsafeMutablePointer<BNNSNDArrayDescriptor>?>?) -> Int32](bnnsfusedfilterapplybackwardbatch(_:_:_:_:_:_:_:_:_:_:_:).md)
  Applies a fused filter backward to generate input gradients.
- [func BNNSFusedFilterApplyBackwardMultiInputBatch(BNNSFilter?, Int, Int, UnsafeMutablePointer<UnsafeRawPointer?>?, UnsafePointer<Int>?, UnsafeMutablePointer<UnsafeMutablePointer<BNNSNDArrayDescriptor>>, UnsafePointer<Int>, UnsafeRawPointer?, Int, UnsafeMutablePointer<BNNSNDArrayDescriptor>, Int, UnsafeMutablePointer<UnsafeMutablePointer<BNNSNDArrayDescriptor>?>?) -> Int32](bnnsfusedfilterapplybackwardmultiinputbatch(_:_:_:_:_:_:_:_:_:_:_:_:).md)
  Applies a multiple-input fused filter backward to generate input gradients.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnns/fusedfullyconnectednormalizationlayer)*