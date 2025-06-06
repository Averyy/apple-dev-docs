# rightAnchor

**Framework**: AppKit  
**Kind**: property

A layout anchor representing the right edge of the layout guide’s frame.

**Availability**:
- macOS 10.11+

## Declaration

```swift
var rightAnchor: NSLayoutXAxisAnchor { get }
```

#### Discussion

Use this anchor to create constraints with the layout guide’s right edge. You can combine this anchor only with a subset of the [`NSLayoutXAxisAnchor`](https://developer.apple.com/documentation/UIKit/NSLayoutXAxisAnchor) anchors. You can combine a [`rightAnchor`](nslayoutguide/rightanchor.md) with another `rightAnchor`, a `leftAnchor`, or a `centerXAnchor`. For more information, see [`NSLayoutAnchor`](https://developer.apple.com/documentation/UIKit/NSLayoutAnchor).

## See Also

- [var bottomAnchor: NSLayoutYAxisAnchor](nslayoutguide/bottomanchor.md)
  A layout anchor representing the bottom edge of the layout guide’s frame.
- [var centerXAnchor: NSLayoutXAxisAnchor](nslayoutguide/centerxanchor.md)
  A layout anchor representing the horizontal center of the layout guide’s frame.
- [var centerYAnchor: NSLayoutYAxisAnchor](nslayoutguide/centeryanchor.md)
  A layout anchor representing the vertical center of the layout guide’s frame.
- [var heightAnchor: NSLayoutDimension](nslayoutguide/heightanchor.md)
  A layout anchor representing the height of the layout guide’s frame.
- [var leadingAnchor: NSLayoutXAxisAnchor](nslayoutguide/leadinganchor.md)
  A layout anchor representing the leading edge of the layout guide’s frame.
- [var leftAnchor: NSLayoutXAxisAnchor](nslayoutguide/leftanchor.md)
  A layout anchor representing the left edge of the layout guide’s frame.
- [var topAnchor: NSLayoutYAxisAnchor](nslayoutguide/topanchor.md)
  A layout anchor representing the top edge of the layout guide’s frame.
- [var trailingAnchor: NSLayoutXAxisAnchor](nslayoutguide/trailinganchor.md)
  A layout anchor representing the trailing edge of the layout guide’s frame.
- [var widthAnchor: NSLayoutDimension](nslayoutguide/widthanchor.md)
  A layout anchor representing the width of the layout guide’s frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nslayoutguide/rightanchor)*