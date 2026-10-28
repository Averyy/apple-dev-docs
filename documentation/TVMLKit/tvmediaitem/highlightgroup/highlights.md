# highlights

**Framework**: TVMLKit  
**Kind**: property  
**Role**: Instance Property

An array of the individual highlights that make up a group.

**Availability**:
- tvOS 12.0+ - Deprecated in 18.0

> **Deprecated**: Please use SwiftUI or UIKit

## Declaration

```swift
var highlights: [TVMediaItem.Highlight] { get }
```

```objc
@property (nonatomic, strong, readonly) NSArray<TVHighlight *> * highlights;
```

## Discussion

The `highlights` property contains all of the highlights associated with a specific group. For example, all of the home runs hit during a single baseball game.

## See Also

### Accessing the Highlights
- [var localizedName: String?](./localizedname.md)
  The name of a highlight group.
- [TVMediaItem.Highlight](../highlight.md)
  An object that describes a media item highlight.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmlkit/tvmediaitem/highlightgroup/highlights)*