# MPSRayMaskOperator

**Framework**: Metal Performance Shaders  
**Kind**: enum  
**Role**: Enumeration

**Availability**:
- iOS 13.0+ - Deprecated in 17.0
- iPadOS 13.0+ - Deprecated in 17.0
- Mac Catalyst 13.0+ - Deprecated in 17.0
- macOS 10.15+ - Deprecated in 14.0
- tvOS 13.0+ - Deprecated in 17.0
- visionOS 1.0+ - Deprecated in 1.0

## Declaration

```swift
enum MPSRayMaskOperator
```

```c
enum MPSRayMaskOperator : NSUInteger;
```

## Topics

### Enumeration Cases
- [MPSRayMaskOperator.and](./mpsraymaskoperator/and.md)
- [MPSRayMaskOperator.equal](./mpsraymaskoperator/equal.md)
- [MPSRayMaskOperator.greaterThan](./mpsraymaskoperator/greaterthan.md)
- [MPSRayMaskOperator.greaterThanOrEqualTo](./mpsraymaskoperator/greaterthanorequalto.md)
- [MPSRayMaskOperator.lessThan](./mpsraymaskoperator/lessthan.md)
- [MPSRayMaskOperator.lessThanOrEqualTo](./mpsraymaskoperator/lessthanorequalto.md)
- [MPSRayMaskOperator.notAnd](./mpsraymaskoperator/notand.md)
- [MPSRayMaskOperator.notEqual](./mpsraymaskoperator/notequal.md)
- [MPSRayMaskOperator.notOr](./mpsraymaskoperator/notor.md)
- [MPSRayMaskOperator.notXor](./mpsraymaskoperator/notxor.md)
- [MPSRayMaskOperator.or](./mpsraymaskoperator/or.md)
- [MPSRayMaskOperator.xor](./mpsraymaskoperator/xor.md)
### Initializers
- [init?(rawValue: UInt)](./mpsraymaskoperator/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Enumerations
- [enum MPSAccelerationStructureStatus](./mpsaccelerationstructurestatus.md)
  Constants that indicate an acceleration structure build state.
- [struct MPSAccelerationStructureUsage](./mpsaccelerationstructureusage.md)
  Options that describe how an acceleration structure will be used.
- [struct MPSAliasingStrategy](./mpsaliasingstrategy.md)
- [enum MPSBoundingBoxIntersectionTestType](./mpsboundingboxintersectiontesttype.md)
  Options for the intersection test type for a ray intersector bounding box.
- [struct MPSCNNBatchNormalizationFlags](./mpscnnbatchnormalizationflags.md)
  Options that define how statistics are calculated during batch normalization.
- [struct MPSCNNConvolutionGradientOption](./mpscnnconvolutiongradientoption.md)
  Options that control which gradient to compute during backward propagation.
- [enum MPSCNNConvolutionWeightsLayout](./mpscnnconvolutionweightslayout.md)
- [enum MPSCNNLossType](./mpscnnlosstype.md)
  Constants that indicate supported loss filter types.
- [enum MPSCNNReductionType](./mpscnnreductiontype.md)
  Constants that indicate supported reduction types.
- [enum MPSCNNWeightsQuantizationType](./mpscnnweightsquantizationtype.md)
  Options that specify the type of quantization used to generate unsigned integer weights.
- [struct MPSCustomKernelIndex](./mpscustomkernelindex.md)
- [struct MPSDeviceCapsValues](./mpsdevicecapsvalues.md)
- [struct MPSDeviceOptions](./mpsdeviceoptions.md)
- [enum MPSFloatDataTypeBit](./mpsfloatdatatypebit.md)
- [enum MPSFloatDataTypeShift](./mpsfloatdatatypeshift.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsraymaskoperator)*