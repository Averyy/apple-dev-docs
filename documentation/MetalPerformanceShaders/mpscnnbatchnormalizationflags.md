# MPSCNNBatchNormalizationFlags

**Framework**: Metal Performance Shaders  
**Kind**: struct  
**Role**: Structure

Options that define how statistics are calculated during batch normalization.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
struct MPSCNNBatchNormalizationFlags
```

```c
enum MPSCNNBatchNormalizationFlags : NSUInteger;
```

## Topics

### Initializers
- [init(rawValue: UInt)](./mpscnnbatchnormalizationflags/init%28rawvalue%29.md)
### Type Properties
- [static var CalculateStatisticsAutomatic: MPSCNNBatchNormalizationFlags](./mpscnnbatchnormalizationflags/calculatestatisticsautomatic.md)
- [static var Default: MPSCNNBatchNormalizationFlags](./mpscnnbatchnormalizationflags/default.md)
- [static var calculateStatisticsAlways: MPSCNNBatchNormalizationFlags](./mpscnnbatchnormalizationflags/calculatestatisticsalways.md)
- [static var calculateStatisticsMask: MPSCNNBatchNormalizationFlags](./mpscnnbatchnormalizationflags/calculatestatisticsmask.md)
- [static var calculateStatisticsNever: MPSCNNBatchNormalizationFlags](./mpscnnbatchnormalizationflags/calculatestatisticsnever.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../Swift/optionset.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [SetAlgebra](../Swift/setalgebra.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnbatchnormalizationflags)*