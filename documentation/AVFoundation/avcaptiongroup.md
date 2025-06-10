# AVCaptionGroup

**Framework**: AVFoundation  
**Kind**: class

An object that represents zero or more captions that intersect in time.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 15.0+
- macOS 12.0+

## Declaration

```swift
class AVCaptionGroup
```

## Topics

### Creating a Caption Group
- [init(timeRange: CMTimeRange)](avcaptiongroup/init(timerange:).md)
  Creates a caption group with a time range.
- [init(captions: [AVCaption], timeRange: CMTimeRange)](avcaptiongroup/init(captions:timerange:).md)
  Creates a caption group with captions and a time range.
### Inspecting the Caption Group
- [var captions: [AVCaption]](avcaptiongroup/captions.md)
  The captions associated with the caption group.
- [var timeRange: CMTimeRange](avcaptiongroup/timerange.md)
  The time range of the caption group.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [AVAssetReaderOutput.SupportedPayload](avassetreaderoutput/supportedpayload.md)
- [CVarArg](../Swift/CVarArg.md)
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class AVCaptionGrouper](avcaptiongrouper.md)
  An object that analyzes the temporal overlaps of caption objects to create caption groups for each span of concurrent captions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcaptiongroup)*