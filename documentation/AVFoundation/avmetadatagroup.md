# AVMetadataGroup

**Framework**: AVFoundation  
**Kind**: class

A collection of metadata items associated with a timeline segment.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class AVMetadataGroup
```

## Topics

### Inspecting the metadata group
- [var items: [AVMetadataItem]](avmetadatagroup/items.md)
  The array of metadata items associated with the metadata group.
- [var uniqueID: String?](avmetadatagroup/uniqueid.md)
  The unique identifier for the metadata group.
- [var classifyingLabel: String?](avmetadatagroup/classifyinglabel.md)
  The classifying label associated with the metadata group.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [AVDateRangeMetadataGroup](avdaterangemetadatagroup.md)
- [AVTimedMetadataGroup](avtimedmetadatagroup.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [Presenting chapter markers](presenting-chapter-markers.md)
  Add chapter markers to enable users to quickly navigate your content.
- [class AVTimedMetadataGroup](avtimedmetadatagroup.md)
  A collection of metadata items that are valid for use during a specific time range.
- [class AVMutableTimedMetadataGroup](avmutabletimedmetadatagroup.md)
  A mutable collection of metadata items that are valid for use during a specific time range.
- [class AVDateRangeMetadataGroup](avdaterangemetadatagroup.md)
  A collection of metadata items that are valid for use within a specific date range.
- [class AVMutableDateRangeMetadataGroup](avmutabledaterangemetadatagroup.md)
  A mutable collection of metadata items that are valid for use within a specific range of dates.
- [class AVPlayerItemMediaDataCollector](avplayeritemmediadatacollector.md)
  The abstract base for media data collectors.
- [class AVPlayerItemMetadataCollector](avplayeritemmetadatacollector.md)
  An object used to capture the date range metadata defined for an HTTP Live Streaming asset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmetadatagroup)*