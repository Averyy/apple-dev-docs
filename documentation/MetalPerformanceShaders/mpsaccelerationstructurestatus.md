# MPSAccelerationStructureStatus

**Framework**: Metal Performance Shaders  
**Kind**: enum

Constants that indicate an acceleration structure build state.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.0+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+

## Declaration

```swift
enum MPSAccelerationStructureStatus
```

## Topics

### Enumeration Cases
- [MPSAccelerationStructureStatus.built](mpsaccelerationstructurestatus/built.md)
- [MPSAccelerationStructureStatus.unbuilt](mpsaccelerationstructurestatus/unbuilt.md)
### Initializers
- [init?(rawValue: UInt)](mpsaccelerationstructurestatus/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

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
- [struct MPSImageType](mpsimagetype.md)
  Options that define a Metal Performance Shaders image type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsaccelerationstructurestatus)*