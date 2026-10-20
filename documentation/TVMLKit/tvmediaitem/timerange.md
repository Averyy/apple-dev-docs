# TVMediaItem.TimeRange

**Framework**: TVMLKit  
**Kind**: class  
**Role**: Class

An object that defines a time range in a media item.

**Availability**:
- tvOS 12.0+ - Deprecated in 18.0

> **Deprecated**: Please use SwiftUI or UIKit

## Declaration

```swift
class TimeRange
```

```objc
@interface TVTimeRange : NSObject
```

## Topics

### Defining the Time Range
- [var startTime: TimeInterval](./timerange/starttime.md)
  The time in a media item that determines when a time range begins.
- [var endTime: TimeInterval](./timerange/endtime.md)
  The time in a media item that determines when a time range ends.
- [var duration: TimeInterval](./timerange/duration.md)
  The duration of a time range in a media item.

## Relationships

### Inherits From
- [NSObject](../../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../../Swift/cvararg.md)
- [CustomDebugStringConvertible](../../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../../Swift/customstringconvertible.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [NSObjectProtocol](../../ObjectiveC/nsobjectprotocol.md)

## See Also

### Setting Timing Options
- [var highlightGroups: [TVMediaItem.HighlightGroup]](./highlightgroups.md)
  An array containing groups of individual highlights in a media item.
- [TVMediaItem.HighlightGroup](./highlightgroup.md)
  A container for groups of highlights for a media item.
- [var interstitials: [TVMediaItem.TimeRange]](./interstitials.md)
  An array of time intervals that indicate where to insert media items into another, single media item.
- [var resumeTime: TimeInterval](./resumetime.md)
  The number of seconds from the beginning of a media item to the point where that media item begins playing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmlkit/tvmediaitem/timerange)*