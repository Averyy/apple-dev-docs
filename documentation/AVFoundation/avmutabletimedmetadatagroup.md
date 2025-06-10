# AVMutableTimedMetadataGroup

**Framework**: AVFoundation  
**Kind**: class

A mutable collection of metadata items that are valid for use during a specific time range.

**Availability**:
- iOS 4.3+
- iPadOS 4.3+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
class AVMutableTimedMetadataGroup
```

## Topics

### Configuring the Group
- [var items: [AVMetadataItem]](avmutabletimedmetadatagroup/items.md)
  An array of metadata items in the timed metadata group.
- [var timeRange: CMTimeRange](avmutabletimedmetadatagroup/timerange.md)
  The time range of the timed metadata.

## Relationships

### Inherits From
- [AVTimedMetadataGroup](avtimedmetadatagroup.md)
### Conforms To
- [AVAssetReaderOutput.SupportedPayload](avassetreaderoutput/supportedpayload.md)
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSMutableCopying](../Foundation/NSMutableCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [Presenting Chapter Markers](presenting-chapter-markers.md)
  Add chapter markers to enable users to quickly navigate your content.
- [class AVMetadataGroup](avmetadatagroup.md)
  A collection of metadata items associated with a timeline segment.
- [class AVTimedMetadataGroup](avtimedmetadatagroup.md)
  A collection of metadata items that are valid for use during a specific time range.
- [class AVDateRangeMetadataGroup](avdaterangemetadatagroup.md)
  A collection of metadata items that are valid for use within a specific date range.
- [class AVMutableDateRangeMetadataGroup](avmutabledaterangemetadatagroup.md)
  A mutable collection of metadata items that are valid for use within a specific range of dates.
- [class AVPlayerItemMediaDataCollector](avplayeritemmediadatacollector.md)
  The abstract base for media data collectors.
- [class AVPlayerItemMetadataCollector](avplayeritemmetadatacollector.md)
  An object used to capture the date range metadata defined for an HTTP Live Streaming asset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmutabletimedmetadatagroup)*