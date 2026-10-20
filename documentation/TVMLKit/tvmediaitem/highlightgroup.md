# TVMediaItem.HighlightGroup

**Framework**: TVMLKit  
**Kind**: class  
**Role**: Class

A container for groups of highlights for a media item.

**Availability**:
- tvOS 12.0+ - Deprecated in 18.0

> **Deprecated**: Please use SwiftUI or UIKit

## Declaration

```swift
class HighlightGroup
```

```objc
@interface TVHighlightGroup : NSObject
```

## Topics

### Accessing the Highlights
- [var localizedName: String?](./highlightgroup/localizedname.md)
  The name of a highlight group.
- [var highlights: [TVMediaItem.Highlight]](./highlightgroup/highlights.md)
  An array of the individual highlights that make up a group.
- [TVMediaItem.Highlight](./highlight.md)
  An object that describes a media item highlight.

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
- [var interstitials: [TVMediaItem.TimeRange]](./interstitials.md)
  An array of time intervals that indicate where to insert media items into another, single media item.
- [TVMediaItem.TimeRange](./timerange.md)
  An object that defines a time range in a media item.
- [var resumeTime: TimeInterval](./resumetime.md)
  The number of seconds from the beginning of a media item to the point where that media item begins playing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmlkit/tvmediaitem/highlightgroup)*