# MPSNNReduceUnary

**Framework**: Metal Performance Shaders  
**Kind**: class  
**Role**: Class

The base class for unary reduction filters.

**Availability**:
- iOS 11.3+
- iPadOS 11.3+
- Mac Catalyst 13.0+
- macOS 10.13.4+
- tvOS 11.3+
- visionOS 1.0+

## Declaration

```swift
class MPSNNReduceUnary
```

```objc
@interface MPSNNReduceUnary : MPSCNNKernel
```

## Topics

### Instance Properties
- [var clipRectSource: MTLRegion](./mpsnnreduceunary/cliprectsource.md)
- [var offset: MPSOffset](./mpsnnreduceunary/offset.md)

## Relationships

### Inherits From
- [MPSCNNKernel](./mpscnnkernel.md)
### Inherited By
- [MPSNNReduceColumnMax](./mpsnnreducecolumnmax.md)
- [MPSNNReduceColumnMean](./mpsnnreducecolumnmean.md)
- [MPSNNReduceColumnMin](./mpsnnreducecolumnmin.md)
- [MPSNNReduceColumnSum](./mpsnnreducecolumnsum.md)
- [MPSNNReduceFeatureChannelsArgumentMax](./mpsnnreducefeaturechannelsargumentmax.md)
- [MPSNNReduceFeatureChannelsArgumentMin](./mpsnnreducefeaturechannelsargumentmin.md)
- [MPSNNReduceFeatureChannelsMax](./mpsnnreducefeaturechannelsmax.md)
- [MPSNNReduceFeatureChannelsMean](./mpsnnreducefeaturechannelsmean.md)
- [MPSNNReduceFeatureChannelsMin](./mpsnnreducefeaturechannelsmin.md)
- [MPSNNReduceFeatureChannelsSum](./mpsnnreducefeaturechannelssum.md)
- [MPSNNReduceRowMax](./mpsnnreducerowmax.md)
- [MPSNNReduceRowMean](./mpsnnreducerowmean.md)
- [MPSNNReduceRowMin](./mpsnnreducerowmin.md)
- [MPSNNReduceRowSum](./mpsnnreducerowsum.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### Reduction Layers
- [class MPSNNReduceRowMax](./mpsnnreducerowmax.md)
  A reduction filter that returns the maximum value for each row in an image.
- [class MPSNNReduceRowMin](./mpsnnreducerowmin.md)
  A reduction filter that returns the minimum value for each row in an image.
- [class MPSNNReduceRowSum](./mpsnnreducerowsum.md)
  A reduction filter that returns the sum of all values for each row in an image.
- [class MPSNNReduceRowMean](./mpsnnreducerowmean.md)
  A reduction filter that returns the mean value for each row in an image.
- [class MPSNNReduceColumnMax](./mpsnnreducecolumnmax.md)
  A reduction filter that returns the maximum value for each column in an image.
- [class MPSNNReduceColumnMin](./mpsnnreducecolumnmin.md)
  A reduction filter that returns the minimum value for each column in an image.
- [class MPSNNReduceColumnSum](./mpsnnreducecolumnsum.md)
  A reduction filter that returns the sum of all values for each column in an image.
- [class MPSNNReduceColumnMean](./mpsnnreducecolumnmean.md)
  A reduction filter that returns the mean value for each column in an image.
- [class MPSNNReduceFeatureChannelsMax](./mpsnnreducefeaturechannelsmax.md)
  A reduction filter that returns the maximum value for each feature channel in an image.
- [class MPSNNReduceFeatureChannelsMin](./mpsnnreducefeaturechannelsmin.md)
  A reduction filter that returns the minimum value for each feature channel in an image.
- [class MPSNNReduceFeatureChannelsSum](./mpsnnreducefeaturechannelssum.md)
  A reduction filter that returns the sum of all values for each feature channel in an image.
- [class MPSNNReduceFeatureChannelsMean](./mpsnnreducefeaturechannelsmean.md)
  A reduction filter that returns the mean value for each feature channel in an image.
- [class MPSNNReduceFeatureChannelsArgumentMax](./mpsnnreducefeaturechannelsargumentmax.md)
  A reduction filter that returns the index of the location of the maximum value for each feature channel in an image.
- [class MPSNNReduceFeatureChannelsArgumentMin](./mpsnnreducefeaturechannelsargumentmin.md)
  A reduction filter that returns the index of the location of the minimum value for each feature channel in an image.
- [class MPSNNReduceFeatureChannelsAndWeightsSum](./mpsnnreducefeaturechannelsandweightssum.md)
  A reduction filter that returns the weighted sum of all values for each feature channel in an image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsnnreduceunary)*