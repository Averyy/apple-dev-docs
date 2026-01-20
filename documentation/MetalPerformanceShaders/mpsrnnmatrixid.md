# MPSRNNMatrixId

**Framework**: Metal Performance Shaders  
**Kind**: enum

Options that define which matrix is copied in or out of a trainable RNN layer.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
enum MPSRNNMatrixId
```

## Topics

### Enumeration Cases
- [MPSRNNMatrixId.SingleGateInputWeights](mpsrnnmatrixid/singlegateinputweights.md)
- [MPSRNNMatrixId.gruInputGateBiasTerms](mpsrnnmatrixid/gruinputgatebiasterms.md)
- [MPSRNNMatrixId.gruInputGateInputWeights](mpsrnnmatrixid/gruinputgateinputweights.md)
- [MPSRNNMatrixId.gruInputGateRecurrentWeights](mpsrnnmatrixid/gruinputgaterecurrentweights.md)
- [MPSRNNMatrixId.gruOutputGateBiasTerms](mpsrnnmatrixid/gruoutputgatebiasterms.md)
- [MPSRNNMatrixId.gruOutputGateInputGateWeights](mpsrnnmatrixid/gruoutputgateinputgateweights.md)
- [MPSRNNMatrixId.gruOutputGateInputWeights](mpsrnnmatrixid/gruoutputgateinputweights.md)
- [MPSRNNMatrixId.gruOutputGateRecurrentWeights](mpsrnnmatrixid/gruoutputgaterecurrentweights.md)
- [MPSRNNMatrixId.gruRecurrentGateBiasTerms](mpsrnnmatrixid/grurecurrentgatebiasterms.md)
- [MPSRNNMatrixId.gruRecurrentGateInputWeights](mpsrnnmatrixid/grurecurrentgateinputweights.md)
- [MPSRNNMatrixId.gruRecurrentGateRecurrentWeights](mpsrnnmatrixid/grurecurrentgaterecurrentweights.md)
- [MPSRNNMatrixId.lstmForgetGateBiasTerms](mpsrnnmatrixid/lstmforgetgatebiasterms.md)
- [MPSRNNMatrixId.lstmForgetGateInputWeights](mpsrnnmatrixid/lstmforgetgateinputweights.md)
- [MPSRNNMatrixId.lstmForgetGateMemoryWeights](mpsrnnmatrixid/lstmforgetgatememoryweights.md)
- [MPSRNNMatrixId.lstmForgetGateRecurrentWeights](mpsrnnmatrixid/lstmforgetgaterecurrentweights.md)
- [MPSRNNMatrixId.lstmInputGateBiasTerms](mpsrnnmatrixid/lstminputgatebiasterms.md)
- [MPSRNNMatrixId.lstmInputGateInputWeights](mpsrnnmatrixid/lstminputgateinputweights.md)
- [MPSRNNMatrixId.lstmInputGateMemoryWeights](mpsrnnmatrixid/lstminputgatememoryweights.md)
- [MPSRNNMatrixId.lstmInputGateRecurrentWeights](mpsrnnmatrixid/lstminputgaterecurrentweights.md)
- [MPSRNNMatrixId.lstmMemoryGateBiasTerms](mpsrnnmatrixid/lstmmemorygatebiasterms.md)
- [MPSRNNMatrixId.lstmMemoryGateInputWeights](mpsrnnmatrixid/lstmmemorygateinputweights.md)
- [MPSRNNMatrixId.lstmMemoryGateMemoryWeights](mpsrnnmatrixid/lstmmemorygatememoryweights.md)
- [MPSRNNMatrixId.lstmMemoryGateRecurrentWeights](mpsrnnmatrixid/lstmmemorygaterecurrentweights.md)
- [MPSRNNMatrixId.lstmOutputGateBiasTerms](mpsrnnmatrixid/lstmoutputgatebiasterms.md)
- [MPSRNNMatrixId.lstmOutputGateInputWeights](mpsrnnmatrixid/lstmoutputgateinputweights.md)
- [MPSRNNMatrixId.lstmOutputGateMemoryWeights](mpsrnnmatrixid/lstmoutputgatememoryweights.md)
- [MPSRNNMatrixId.lstmOutputGateRecurrentWeights](mpsrnnmatrixid/lstmoutputgaterecurrentweights.md)
- [MPSRNNMatrixId.singleGateBiasTerms](mpsrnnmatrixid/singlegatebiasterms.md)
- [MPSRNNMatrixId.singleGateRecurrentWeights](mpsrnnmatrixid/singlegaterecurrentweights.md)
### Initializers
- [init?(rawValue: UInt)](mpsrnnmatrixid/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [enum MPSAccelerationStructureStatus](mpsaccelerationstructurestatus.md)
  Constants that indicate an acceleration structure build state.
- [struct MPSAccelerationStructureUsage](mpsaccelerationstructureusage.md)
  Options that describe how an acceleration structure will be used.
- [struct MPSAliasingStrategy](mpsaliasingstrategy.md)
- [enum MPSBoundingBoxIntersectionTestType](mpsboundingboxintersectiontesttype.md)
  Options for the intersection test type for a ray intersector bounding box.
- [struct MPSCNNBatchNormalizationFlags](mpscnnbatchnormalizationflags.md)
  Options that define how statistics are calculated during batch normalization.
- [struct MPSCNNConvolutionGradientOption](mpscnnconvolutiongradientoption.md)
  Options that control which gradient to compute during backward propagation.
- [enum MPSCNNConvolutionWeightsLayout](mpscnnconvolutionweightslayout.md)
- [enum MPSCNNLossType](mpscnnlosstype.md)
  Constants that indicate supported loss filter types.
- [enum MPSCNNReductionType](mpscnnreductiontype.md)
  Constants that indicate supported reduction types.
- [enum MPSCNNWeightsQuantizationType](mpscnnweightsquantizationtype.md)
  Options that specify the type of quantization used to generate unsigned integer weights.
- [struct MPSCustomKernelIndex](mpscustomkernelindex.md)
- [struct MPSDeviceCapsValues](mpsdevicecapsvalues.md)
- [struct MPSDeviceOptions](mpsdeviceoptions.md)
- [enum MPSFloatDataTypeBit](mpsfloatdatatypebit.md)
- [enum MPSFloatDataTypeShift](mpsfloatdatatypeshift.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsrnnmatrixid)*