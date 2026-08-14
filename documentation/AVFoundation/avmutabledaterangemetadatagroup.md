# AVMutableDateRangeMetadataGroup

**Framework**: AVFoundation  
**Kind**: class

A mutable collection of metadata items that are valid for use within a specific range of dates.

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
class AVMutableDateRangeMetadataGroup
```

## Topics

### Configuring the metadata
- [var items: [AVMetadataItem]](avmutabledaterangemetadatagroup/items.md)
  An array of associated metadata items.
### Configuring the date range
- [var startDate: Date](avmutabledaterangemetadatagroup/startdate.md)
  The start date for the metadata date range group.
- [var endDate: Date?](avmutabledaterangemetadatagroup/enddate.md)
  The end date for the metadata date range group.

## Relationships

### Inherits From
- [AVDateRangeMetadataGroup](avdaterangemetadatagroup.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCopying](../foundation/nscopying.md)
- [NSMutableCopying](../foundation/nsmutablecopying.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## See Also

- [Presenting chapter markers](presenting-chapter-markers.md)
  Add chapter markers to enable users to quickly navigate your content.
- [class AVMetadataGroup](avmetadatagroup.md)
  A collection of metadata items associated with a timeline segment.
- [class AVTimedMetadataGroup](avtimedmetadatagroup.md)
  A collection of metadata items that are valid for use during a specific time range.
- [class AVMutableTimedMetadataGroup](avmutabletimedmetadatagroup.md)
  A mutable collection of metadata items that are valid for use during a specific time range.
- [class AVDateRangeMetadataGroup](avdaterangemetadatagroup.md)
  A collection of metadata items that are valid for use within a specific date range.
- [class AVPlayerItemMediaDataCollector](avplayeritemmediadatacollector.md)
  The abstract base for media data collectors.
- [class AVPlayerItemMetadataCollector](avplayeritemmetadatacollector.md)
  An object used to capture the date range metadata defined for an HTTP Live Streaming asset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmutabledaterangemetadatagroup)*