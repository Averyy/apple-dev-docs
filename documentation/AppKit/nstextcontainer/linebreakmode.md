# lineBreakMode

**Framework**: AppKit  
**Kind**: property

The behavior of the last line inside the text container.

**Availability**:
- macOS 10.11+

## Declaration

```swift
var lineBreakMode: NSLineBreakMode { get set }
```

#### Discussion

The [`NSLineBreakMode`](nslinebreakmode.md) constants specify what happens when a line is too long for its container. For example, wrapping can occur on word boundaries (the default) or character boundaries, or the line can be clipped or truncated. The default value of this property is [`NSLineBreakMode.byWordWrapping`](nslinebreakmode/bywordwrapping.md).

## See Also

- [var size: CGSize](nstextcontainer/size.md)
  The size of the text container’s bounding rectangle.
- [var exclusionPaths: [NSBezierPath]](nstextcontainer/exclusionpaths.md)
  An array of path objects that represents the regions where text doesn’t display in the text container.
- [var widthTracksTextView: Bool](nstextcontainer/widthtrackstextview.md)
  A Boolean that controls whether the text container adjusts the width of its bounding rectangle when its text view resizes.
- [var heightTracksTextView: Bool](nstextcontainer/heighttrackstextview.md)
  A Boolean that controls whether the text container adjusts the height of its bounding rectangle when its text view resizes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextcontainer/linebreakmode)*