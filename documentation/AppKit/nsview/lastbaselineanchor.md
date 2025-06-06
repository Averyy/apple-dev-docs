# lastBaselineAnchor

**Framework**: AppKit  
**Kind**: property

A layout anchor representing the baseline for the bottommost line of text in the view.

**Availability**:
- macOS 10.11+

## Declaration

```swift
@MainActor
var lastBaselineAnchor: NSLayoutYAxisAnchor { get }
```

#### Discussion

For views with multiple lines of text, this anchor represents the baseline of the bottom row of text. Use this anchor to create constraints with this baseline. You can only combine this anchor with other [`NSLayoutYAxisAnchor`](https://developer.apple.com/documentation/UIKit/NSLayoutYAxisAnchor) anchors. For more information, see [`NSLayoutAnchor`](https://developer.apple.com/documentation/UIKit/NSLayoutAnchor).

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
- [var widthAnchor: NSLayoutDimension](nsview/widthanchor.md)
  A layout anchor representing the width of the view’s frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/lastbaselineanchor)*