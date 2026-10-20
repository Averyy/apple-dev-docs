# TVMediaItem.Highlight

**Framework**: TVMLKit  
**Kind**: class  
**Role**: Class

An object that describes a media item highlight.

**Availability**:
- tvOS 12.0+ - Deprecated in 18.0

> **Deprecated**: Please use SwiftUI or UIKit

## Declaration

```swift
class Highlight
```

```objc
@interface TVHighlight : NSObject
```

## Topics

### Accessing a Highlight
- [var highlightDescription: String?](./highlight/highlightdescription.md)
  A description for an individual highlight.
- [var imageURL: URL?](./highlight/imageurl.md)
  The URL for an image associated with a highlight.
- [var localizedName: String?](./highlight/localizedname.md)
  The name associated with a highlight.
- [var timeRange: TVMediaItem.TimeRange](./highlight/timerange.md)
  A time range that determines when a highlight begins and its duration.

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

### Accessing the Highlights
- [var localizedName: String?](./highlightgroup/localizedname.md)
  The name of a highlight group.
- [var highlights: [TVMediaItem.Highlight]](./highlightgroup/highlights.md)
  An array of the individual highlights that make up a group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmlkit/tvmediaitem/highlight)*