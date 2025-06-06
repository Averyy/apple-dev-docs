# interstitials

**Framework**: TVMLKit  
**Kind**: property

An array of time intervals that indicate where to insert media items into another, single media item.

**Availability**:
- tvOS 12.0+

## Declaration

```swift
var interstitials: [TVMediaItem.TimeRange] { get }
```

#### Discussion

The `Interstitials` property defines points within a [`TVMediaItem`](tvmediaitem.md) object where you can insert another media item; for example, a short ad. Each time range in the array contains two properties: [`startTime`](tvmediaitem/timerange/starttime.md) and [`duration`](tvmediaitem/timerange/duration.md). The `startTime` is the length of time from the beginning of a media item, in seconds. The `duration` is the length of the interstitial, in seconds. Both properties are required. A common use for these objects is to define when and where ads are to be played during a stream.

## See Also

- [var highlightGroups: [TVMediaItem.HighlightGroup]](tvmediaitem/highlightgroups.md)
  An array containing groups of individual highlights in a media item.
- [TVMediaItem.HighlightGroup](tvmediaitem/highlightgroup.md)
  A container for groups of highlights for a media item.
- [TVMediaItem.TimeRange](tvmediaitem/timerange.md)
  An object that defines a time range in a media item.
- [var resumeTime: TimeInterval](tvmediaitem/resumetime.md)
  The number of seconds from the beginning of a media item to the point where that media item begins playing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmlkit/tvmediaitem/interstitials)*