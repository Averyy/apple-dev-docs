# MPSNNReduceColumnSum

**Framework**: Metal Performance Shaders  
**Kind**: class

A reduction filter that returns the sum of all values for each column in an image.

**Availability**:
- iOS 11.3+
- iPadOS 11.3+
- Mac Catalyst 13.0+
- macOS 10.13.4+
- tvOS 11.3+
- visionOS 1.0+

## Declaration

```swift
class MPSNNReduceColumnSum
```

## Topics

### Initializers
- [init?(coder: NSCoder, device: any MTLDevice)](mpsnnreducecolumnsum/init(coder:device:).md)
- [init(device: any MTLDevice)](mpsnnreducecolumnsum/init(device:).md)

## Relationships

### Inherits From
- [MPSNNReduceUnary](mpsnnreduceunary.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

## See Also

- [class MPSNNReduceRowMax](mpsnnreducerowmax.md)
  A reduction filter that returns the maximum value for each row in an image.
- [class MPSNNReduceRowMin](mpsnnreducerowmin.md)
  A reduction filter that returns the minimum value for each row in an image.
- [class MPSNNReduceRowSum](mpsnnreducerowsum.md)
  A reduction filter that returns the sum of all values for each row in an image.
- [class MPSNNReduceRowMean](mpsnnreducerowmean.md)
  A reduction filter that returns the mean value for each row in an image.
- [class MPSNNReduceColumnMax](mpsnnreducecolumnmax.md)
  A reduction filter that returns the maximum value for each column in an image.
- [class MPSNNReduceColumnMin](mpsnnreducecolumnmin.md)
  A reduction filter that returns the minimum value for each column in an image.
- [class MPSNNReduceColumnMean](mpsnnreducecolumnmean.md)
  A reduction filter that returns the mean value for each column in an image.
- [class MPSNNReduceFeatureChannelsMax](mpsnnreducefeaturechannelsmax.md)
  A reduction filter that returns the maximum value for each feature channel in an image.
- [class MPSNNReduceFeatureChannelsMin](mpsnnreducefeaturechannelsmin.md)
  A reduction filter that returns the minimum value for each feature channel in an image.
- [class MPSNNReduceFeatureChannelsSum](mpsnnreducefeaturechannelssum.md)
  A reduction filter that returns the sum of all values for each feature channel in an image.
- [class MPSNNReduceFeatureChannelsMean](mpsnnreducefeaturechannelsmean.md)
  A reduction filter that returns the mean value for each feature channel in an image.
- [class MPSNNReduceFeatureChannelsArgumentMax](mpsnnreducefeaturechannelsargumentmax.md)
  A reduction filter that returns the index of the location of the maximum value for each feature channel in an image.
- [class MPSNNReduceFeatureChannelsArgumentMin](mpsnnreducefeaturechannelsargumentmin.md)
  A reduction filter that returns the index of the location of the minimum value for each feature channel in an image.
- [class MPSNNReduceFeatureChannelsAndWeightsSum](mpsnnreducefeaturechannelsandweightssum.md)
  A reduction filter that returns the weighted sum of all values for each feature channel in an image.
- [class MPSNNReduceFeatureChannelsAndWeightsMean](mpsnnreducefeaturechannelsandweightsmean.md)
  A reduction filter that returns the weighted sum for each feature channel in an image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsnnreducecolumnsum)*