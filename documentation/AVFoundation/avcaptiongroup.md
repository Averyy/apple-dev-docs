# AVCaptionGroup

**Framework**: AVFoundation  
**Kind**: class  
**Role**: Class

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

```objc
@interface AVCaptionGroup : NSObject
```

## Topics

### Creating a caption group
- [init(timeRange: CMTimeRange)](./avcaptiongroup/init%28timerange%29.md)
  Creates a caption group with a time range.
- [init(captions: [AVCaption], timeRange: CMTimeRange)](./avcaptiongroup/init%28captions,timerange%29.md)
  Creates a caption group with captions and a time range.
### Inspecting the caption group
- [var captions: [AVCaption]](./avcaptiongroup/captions.md)
  The captions associated with the caption group.
- [var timeRange: CMTimeRange](./avcaptiongroup/timerange.md)
  The time range of the caption group.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [AVAssetReaderOutput.SupportedPayload](./avassetreaderoutput/supportedpayload.md)
- [CVarArg](../Swift/cvararg.md)
- [Copyable](../Swift/copyable.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Escapable](../Swift/escapable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Groups
- [class AVCaptionGrouper](./avcaptiongrouper.md)
  An object that analyzes the temporal overlaps of caption objects to create caption groups for each span of concurrent captions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcaptiongroup)*