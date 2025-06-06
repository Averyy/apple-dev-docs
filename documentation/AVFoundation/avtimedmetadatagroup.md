# AVTimedMetadataGroup

**Framework**: AVFoundation  
**Kind**: class

A collection of metadata items that are valid for use during a specific time range.

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
class AVTimedMetadataGroup
```

## Mentions

- [Presenting Chapter Markers](presenting-chapter-markers.md)

#### Overview

For example, `AVTimedMetadataGroups` are used to represent chapters, optionally containing metadata items for chapter titles and chapter images.

## Topics

### Creating a Timed Metadata Group
- [init(items: [AVMetadataItem], timeRange: CMTimeRange)](avtimedmetadatagroup/init(items:timerange:).md)
  Creates a timed metadata group initialized with the given metadata items.
- [init?(sampleBuffer: CMSampleBuffer)](avtimedmetadatagroup/init(samplebuffer:).md)
  Creates a timed metadata group with a sample buffer.
### Accessing Group Attributes
- [var items: [AVMetadataItem]](avtimedmetadatagroup/items.md)
  An array of metadata items in the timed metadata group.
- [var timeRange: CMTimeRange](avtimedmetadatagroup/timerange.md)
  The time range for the timed metadata.
### Creating a Format Description
- [func copyFormatDescription() -> CMMetadataFormatDescription?](avtimedmetadatagroup/copyformatdescription.md)
  Creates a format description based on the receiver’s items.

## Relationships

### Inherits From
- [AVMetadataGroup](avmetadatagroup.md)
### Inherited By
- [AVMutableTimedMetadataGroup](avmutabletimedmetadatagroup.md)
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

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avtimedmetadatagroup)*