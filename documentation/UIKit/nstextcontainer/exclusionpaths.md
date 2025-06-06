# exclusionPaths

**Framework**: UIKit  
**Kind**: property

An array of path objects that represents the regions where text doesn’t display in the text container.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var exclusionPaths: [UIBezierPath] { get set }
```

#### Discussion

The default value of this property is an empty array. Depending on the platform, you can assign an array of [`NSBezierPath`](https://developer.apple.com/documentation/AppKit/NSBezierPath) or [`UIBezierPath`](uibezierpath.md) objects to exclude text from one or more regions in the text container’s bounds. When the layout manager proposes a line fragment rectangle intersecting one of the regions defined by the exclusion paths, the text container returns an adjusted line fragment rectangle excluding that region.

## See Also

- [func lineFragmentRect(forProposedRect: CGRect, at: Int, writingDirection: NSWritingDirection, remaining: UnsafeMutablePointer<CGRect>?) -> CGRect](nstextcontainer/linefragmentrect(forproposedrect:at:writingdirection:remaining:).md)
  Returns the bounds of a line fragment rectangle inside the text container for the proposed rectangle.
- [var size: CGSize](nstextcontainer/size.md)
  The size of the text container’s bounding rectangle.
- [var lineBreakMode: NSLineBreakMode](nstextcontainer/linebreakmode.md)
  The behavior of the last line inside the text container.
- [var widthTracksTextView: Bool](nstextcontainer/widthtrackstextview.md)
  A Boolean that controls whether the text container adjusts the width of its bounding rectangle when its text view resizes.
- [var heightTracksTextView: Bool](nstextcontainer/heighttrackstextview.md)
  A Boolean that controls whether the text container adjusts the height of its bounding rectangle when its text view resizes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nstextcontainer/exclusionpaths)*