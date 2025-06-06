# widthAnchor

**Framework**: AppKit  
**Kind**: property

A layout anchor representing the width of the view’s frame.

**Availability**:
- macOS 10.11+

## Declaration

```swift
@MainActor
var widthAnchor: NSLayoutDimension { get }
```

#### Discussion

Use this anchor to create constraints with the view’s width. You can only combine this anchor with other [`NSLayoutDimension`](https://developer.apple.com/documentation/UIKit/NSLayoutDimension) anchors. For more information, see [`NSLayoutAnchor`](https://developer.apple.com/documentation/UIKit/NSLayoutAnchor).

## See Also

- [var bottomAnchor: NSLayoutYAxisAnchor](nsview/bottomanchor.md)
  A layout anchor representing the bottom edge of the view’s frame.
- [var centerXAnchor: NSLayoutXAxisAnchor](nsview/centerxanchor.md)
  A layout anchor representing the horizontal center of the view’s frame.
- [var centerYAnchor: NSLayoutYAxisAnchor](nsview/centeryanchor.md)
  A layout anchor representing the vertical center of the view’s frame.
- [var firstBaselineAnchor: NSLayoutYAxisAnchor](nsview/firstbaselineanchor.md)
  A layout anchor representing the baseline for the topmost line of text in the view.
- [var heightAnchor: NSLayoutDimension](nsview/heightanchor.md)
  A layout anchor representing the height of the view’s frame.
- [var lastBaselineAnchor: NSLayoutYAxisAnchor](nsview/lastbaselineanchor.md)
  A layout anchor representing the baseline for the bottommost line of text in the view.
- [var leadingAnchor: NSLayoutXAxisAnchor](nsview/leadinganchor.md)
  A layout anchor representing the leading edge of the view’s frame.
- [var leftAnchor: NSLayoutXAxisAnchor](nsview/leftanchor.md)
  A layout anchor representing the left edge of the view’s frame.
- [var rightAnchor: NSLayoutXAxisAnchor](nsview/rightanchor.md)
  A layout anchor representing the right edge of the view’s frame.
- [var topAnchor: NSLayoutYAxisAnchor](nsview/topanchor.md)
  A layout anchor representing the top edge of the view’s frame.
- [var trailingAnchor: NSLayoutXAxisAnchor](nsview/trailinganchor.md)
  A layout anchor representing the trailing edge of the view’s frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/widthanchor)*