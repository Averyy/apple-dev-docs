# AVDateRangeMetadataGroup

**Framework**: AVFoundation  
**Kind**: class

A collection of metadata items that are valid for use within a specific date range.

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
class AVDateRangeMetadataGroup
```

## Topics

### Creating a Date Range Group
- [init(items: [AVMetadataItem], start: Date, end: Date?)](avdaterangemetadatagroup/init(items:start:end:).md)
  Initializes an instance of `AVDateRangeMetadataGroup` with a collection of metadata items.
### Accessing the Metadata
- [var items: [AVMetadataItem]](avdaterangemetadatagroup/items.md)
  An array of associated metadata items.
### Accessing the Date Range
- [var startDate: Date](avdaterangemetadatagroup/startdate.md)
  The start date for the metadata date range group.
- [var endDate: Date?](avdaterangemetadatagroup/enddate.md)
  The end date for the metadata date range group.

## Relationships

### Inherits From
- [AVMetadataGroup](avmetadatagroup.md)
### Inherited By
- [AVMutableDateRangeMetadataGroup](avmutabledaterangemetadatagroup.md)
### Conforms To
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
- [class AVMutableTimedMetadataGroup](avmutabletimedmetadatagroup.md)
  A mutable collection of metadata items that are valid for use during a specific time range.
- [class AVMutableDateRangeMetadataGroup](avmutabledaterangemetadatagroup.md)
  A mutable collection of metadata items that are valid for use within a specific range of dates.
- [class AVPlayerItemMediaDataCollector](avplayeritemmediadatacollector.md)
  The abstract base for media data collectors.
- [class AVPlayerItemMetadataCollector](avplayeritemmetadatacollector.md)
  An object used to capture the date range metadata defined for an HTTP Live Streaming asset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avdaterangemetadatagroup)*