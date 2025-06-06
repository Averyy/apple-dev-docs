# exclusionPaths

**Framework**: AppKit  
**Kind**: property

An array of path objects that represents the regions where text doesn’t display in the text container.

**Availability**:
- macOS 10.11+

## Declaration

```swift
var exclusionPaths: [NSBezierPath] { get set }
```

#### Discussion

The default value of this property is an empty array. Depending on the platform, you can assign an array of [`NSBezierPath`](nsbezierpath.md) or [`UIBezierPath`](https://developer.apple.com/documentation/UIKit/UIBezierPath) objects to exclude text from one or more regions in the text container’s bounds. When the layout manager proposes a line fragment rectangle intersecting one of the regions defined by the exclusion paths, the text container returns an adjusted line fragment rectangle excluding that region.

## See Also

- [var size: CGSize](nstextcontainer/size.md)
  The size of the text container’s bounding rectangle.
- [var lineBreakMode: NSLineBreakMode](nstextcontainer/linebreakmode.md)
  The behavior of the last line inside the text container.
- [var widthTracksTextView: Bool](nstextcontainer/widthtrackstextview.md)
  A Boolean that controls whether the text container adjusts the width of its bounding rectangle when its text view resizes.
- [var heightTracksTextView: Bool](nstextcontainer/heighttrackstextview.md)
  A Boolean that controls whether the text container adjusts the height of its bounding rectangle when its text view resizes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextcontainer/exclusionpaths)*