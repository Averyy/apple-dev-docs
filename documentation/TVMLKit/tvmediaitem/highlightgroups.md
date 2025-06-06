# highlightGroups

**Framework**: TVMLKit  
**Kind**: property

An array containing groups of individual highlights in a media item.

**Availability**:
- tvOS 12.0+

## Declaration

```swift
var highlightGroups: [TVMediaItem.HighlightGroup] { get }
```

#### Discussion

The `highlightGroups` property enables you to show several groups [`highlights`](tvmediaitem/highlightgroup/highlights.md) from a stream. Each highlight group in the array contains a list of highlights. Each highlight is an object with the following properties: [`highlightDescription`](tvmediaitem/highlight/highlightdescription.md), [`localizedName`](tvmediaitem/highlight/localizedname.md), [`imageURL`](tvmediaitem/highlight/imageurl.md), and [`TVMediaItem.TimeRange`](tvmediaitem/timerange.md).

For example, consider a video of a baseball game, which is the media item. You can create a highlight group containing the video for each home run —each highlight— in the game. You create another highlight group containing all of the errors. You put these highlight groups into the [`highlightGroups`](tvmediaitem/highlightgroups.md) property.

## See Also

- [TVMediaItem.HighlightGroup](tvmediaitem/highlightgroup.md)
  A container for groups of highlights for a media item.
- [var interstitials: [TVMediaItem.TimeRange]](tvmediaitem/interstitials.md)
  An array of time intervals that indicate where to insert media items into another, single media item.
- [TVMediaItem.TimeRange](tvmediaitem/timerange.md)
  An object that defines a time range in a media item.
- [var resumeTime: TimeInterval](tvmediaitem/resumetime.md)
  The number of seconds from the beginning of a media item to the point where that media item begins playing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmlkit/tvmediaitem/highlightgroups)*