# highlightGroups

**Framework**: TVMLKit  
**Kind**: property  
**Role**: Instance Property

An array containing groups of individual highlights in a media item.

**Availability**:
- tvOS 12.0+ - Deprecated in 18.0

> **Deprecated**: Please use SwiftUI or UIKit

## Declaration

```swift
var highlightGroups: [TVMediaItem.HighlightGroup] { get }
```

```objc
@property (nonatomic, strong, readonly) NSArray<TVHighlightGroup *> * highlightGroups;
```

## Discussion

The `highlightGroups` property enables you to show several groups [`highlights`](./highlightgroup/highlights.md) from a stream. Each highlight group in the array contains a list of highlights. Each highlight is an object with the following properties: [`highlightDescription`](./highlight/highlightdescription.md), [`localizedName`](./highlight/localizedname.md), [`imageURL`](./highlight/imageurl.md), and [`TVMediaItem.TimeRange`](./timerange.md).

For example, consider a video of a baseball game, which is the media item. You can create a highlight group containing the video for each home run —each highlight— in the game. You create another highlight group containing all of the errors. You put these highlight groups into the [`highlightGroups`](./highlightgroups.md) property.

## See Also

### Setting Timing Options
- [TVMediaItem.HighlightGroup](./highlightgroup.md)
  A container for groups of highlights for a media item.
- [var interstitials: [TVMediaItem.TimeRange]](./interstitials.md)
  An array of time intervals that indicate where to insert media items into another, single media item.
- [TVMediaItem.TimeRange](./timerange.md)
  An object that defines a time range in a media item.
- [var resumeTime: TimeInterval](./resumetime.md)
  The number of seconds from the beginning of a media item to the point where that media item begins playing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmlkit/tvmediaitem/highlightgroups)*