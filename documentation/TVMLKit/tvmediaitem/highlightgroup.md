# TVMediaItem.HighlightGroup

**Framework**: TVMLKit  
**Kind**: class

A container for groups of highlights for a media item.

**Availability**:
- tvOS 12.0+

## Declaration

```swift
class HighlightGroup
```

## Topics

### Accessing the Highlights
- [var localizedName: String?](tvmediaitem/highlightgroup/localizedname.md)
  The name of a highlight group.
- [var highlights: [TVMediaItem.Highlight]](tvmediaitem/highlightgroup/highlights.md)
  An array of the individual highlights that make up a group.
- [TVMediaItem.Highlight](tvmediaitem/highlight.md)
  An object that describes a media item highlight.

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
- [var interstitials: [TVMediaItem.TimeRange]](tvmediaitem/interstitials.md)
  An array of time intervals that indicate where to insert media items into another, single media item.
- [TVMediaItem.TimeRange](tvmediaitem/timerange.md)
  An object that defines a time range in a media item.
- [var resumeTime: TimeInterval](tvmediaitem/resumetime.md)
  The number of seconds from the beginning of a media item to the point where that media item begins playing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmlkit/tvmediaitem/highlightgroup)*