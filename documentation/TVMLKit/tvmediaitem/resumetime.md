# resumeTime

**Framework**: TVMLKit  
**Kind**: property  
**Role**: Instance Property

The number of seconds from the beginning of a media item to the point where that media item begins playing.

**Availability**:
- tvOS 12.0+ - Deprecated in 18.0

> **Deprecated**: Please use SwiftUI or UIKit

## Declaration

```swift
var resumeTime: TimeInterval { get }
```

```objc
@property (nonatomic, assign, readonly) NSTimeInterval resumeTime;
```

## See Also

### Setting Timing Options
- [var highlightGroups: [TVMediaItem.HighlightGroup]](./highlightgroups.md)
  An array containing groups of individual highlights in a media item.
- [TVMediaItem.HighlightGroup](./highlightgroup.md)
  A container for groups of highlights for a media item.
- [var interstitials: [TVMediaItem.TimeRange]](./interstitials.md)
  An array of time intervals that indicate where to insert media items into another, single media item.
- [TVMediaItem.TimeRange](./timerange.md)
  An object that defines a time range in a media item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmlkit/tvmediaitem/resumetime)*