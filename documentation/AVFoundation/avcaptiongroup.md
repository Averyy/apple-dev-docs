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

### Creating a caption group
- [init(timeRange: CMTimeRange)](avcaptiongroup/init(timerange:).md)
  Creates a caption group with a time range.
- [init(captions: [AVCaption], timeRange: CMTimeRange)](avcaptiongroup/init(captions:timerange:).md)
  Creates a caption group with captions and a time range.
### Inspecting the caption group
- [var captions: [AVCaption]](avcaptiongroup/captions.md)
  The captions associated with the caption group.
- [var timeRange: CMTimeRange](avcaptiongroup/timerange.md)
  The time range of the caption group.

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [AVAssetReaderOutput.SupportedPayload](avassetreaderoutput/supportedpayload.md)
- [CVarArg](../swift/cvararg.md)
- [Copyable](../swift/copyable.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Escapable](../swift/escapable.md)
- [Hashable](../swift/hashable.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [class AVCaptionGrouper](avcaptiongrouper.md)
  An object that analyzes the temporal overlaps of caption objects to create caption groups for each span of concurrent captions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcaptiongroup)*