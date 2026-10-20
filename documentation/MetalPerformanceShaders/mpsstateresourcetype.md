# MPSStateResourceType

**Framework**: Metal Performance Shaders  
**Kind**: enum  
**Role**: Enumeration

Options for the underlying resource type for a state object.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
enum MPSStateResourceType
```

```c
enum MPSStateResourceType : NSUInteger;
```

## Topics

### Enumeration Cases
- [MPSStateResourceType.buffer](./mpsstateresourcetype/buffer.md)
- [MPSStateResourceType.none](./mpsstateresourcetype/none.md)
- [MPSStateResourceType.texture](./mpsstateresourcetype/texture.md)
### Initializers
- [init?(rawValue: UInt)](./mpsstateresourcetype/init%28rawvalue%29.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsstateresourcetype)*