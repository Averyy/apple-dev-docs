# TVMediaItem.TimeRange

**Framework**: TVMLKit  
**Kind**: class

An object that defines a time range in a media item.

**Availability**:
- tvOS 12.0+

## Declaration

```swift
class TimeRange
```

## Topics

### Defining the Time Range
- [var startTime: TimeInterval](tvmediaitem/timerange/starttime.md)
  The time in a media item that determines when a time range begins.
- [var endTime: TimeInterval](tvmediaitem/timerange/endtime.md)
  The time in a media item that determines when a time range ends.
- [var duration: TimeInterval](tvmediaitem/timerange/duration.md)
  The duration of a time range in a media item.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [var highlightGroups: [TVMediaItem.HighlightGroup]](tvmediaitem/highlightgroups.md)
  An array containing groups of individual highlights in a media item.
- [TVMediaItem.HighlightGroup](tvmediaitem/highlightgroup.md)
  A container for groups of highlights for a media item.
- [var interstitials: [TVMediaItem.TimeRange]](tvmediaitem/interstitials.md)
  An array of time intervals that indicate where to insert media items into another, single media item.
- [var resumeTime: TimeInterval](tvmediaitem/resumetime.md)
  The number of seconds from the beginning of a media item to the point where that media item begins playing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmlkit/tvmediaitem/timerange)*