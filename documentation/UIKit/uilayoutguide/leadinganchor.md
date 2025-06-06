# leadingAnchor

**Framework**: UIKit  
**Kind**: property

A layout anchor representing the leading edge of the layout guide’s frame.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var leadingAnchor: NSLayoutXAxisAnchor { get }
```

#### Discussion

Use this anchor to create constraints with the layout guide’s leading edge. You can combine this anchor only with a subset of the [`NSLayoutXAxisAnchor`](nslayoutxaxisanchor.md) anchors. You can combine a [`leadingAnchor`](uilayoutguide/leadinganchor.md) with another `leadingAnchor`, a `trailingAnchor`, or a `centerXAnchor`. For more information, see [`NSLayoutAnchor`](nslayoutanchor.md).

## See Also

- [var bottomAnchor: NSLayoutYAxisAnchor](uilayoutguide/bottomanchor.md)
  A layout anchor representing the bottom edge of the layout guide’s frame.
- [var centerXAnchor: NSLayoutXAxisAnchor](uilayoutguide/centerxanchor.md)
  A layout anchor representing the horizontal center of the layout guide’s frame.
- [var centerYAnchor: NSLayoutYAxisAnchor](uilayoutguide/centeryanchor.md)
  A layout anchor representing the vertical center of the layout guide’s frame.
- [var heightAnchor: NSLayoutDimension](uilayoutguide/heightanchor.md)
  A layout anchor representing the height of the layout guide’s frame.
- [var leftAnchor: NSLayoutXAxisAnchor](uilayoutguide/leftanchor.md)
  A layout anchor representing the left edge of the layout guide’s frame.
- [var rightAnchor: NSLayoutXAxisAnchor](uilayoutguide/rightanchor.md)
  A layout anchor representing the right edge of the layout guide’s frame.
- [var topAnchor: NSLayoutYAxisAnchor](uilayoutguide/topanchor.md)
  A layout anchor representing the top edge of the layout guide’s frame.
- [var trailingAnchor: NSLayoutXAxisAnchor](uilayoutguide/trailinganchor.md)
  A layout anchor representing the trailing edge of the layout guide’s frame.
- [var widthAnchor: NSLayoutDimension](uilayoutguide/widthanchor.md)
  A layout anchor representing the width of the layout guide’s frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uilayoutguide/leadinganchor)*