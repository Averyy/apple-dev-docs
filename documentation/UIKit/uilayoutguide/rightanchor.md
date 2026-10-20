# rightAnchor

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A layout anchor representing the right edge of the layout guide’s frame.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var rightAnchor: NSLayoutXAxisAnchor { get }
```

```objc
@property (nonatomic, strong, readonly) NSLayoutXAxisAnchor * rightAnchor;
```

#### Discussion

Use this anchor to create constraints with the layout guide’s right edge. You can only combine this anchor with a subset of the [`NSLayoutXAxisAnchor`](../nslayoutxaxisanchor.md) anchors. You can combine a [`rightAnchor`](./rightanchor.md) with another `rightAnchor`, a `leftAnchor`, or a `centerXAnchor`. For more information, see [`NSLayoutAnchor`](../nslayoutanchor.md).

## See Also

### Creating constraints using layout anchors
- [var bottomAnchor: NSLayoutYAxisAnchor](./bottomanchor.md)
  A layout anchor representing the bottom edge of the layout guide’s frame.
- [var centerXAnchor: NSLayoutXAxisAnchor](./centerxanchor.md)
  A layout anchor representing the horizontal center of the layout guide’s frame.
- [var centerYAnchor: NSLayoutYAxisAnchor](./centeryanchor.md)
  A layout anchor representing the vertical center of the layout guide’s frame.
- [var heightAnchor: NSLayoutDimension](./heightanchor.md)
  A layout anchor representing the height of the layout guide’s frame.
- [var leadingAnchor: NSLayoutXAxisAnchor](./leadinganchor.md)
  A layout anchor representing the leading edge of the layout guide’s frame.
- [var leftAnchor: NSLayoutXAxisAnchor](./leftanchor.md)
  A layout anchor representing the left edge of the layout guide’s frame.
- [var topAnchor: NSLayoutYAxisAnchor](./topanchor.md)
  A layout anchor representing the top edge of the layout guide’s frame.
- [var trailingAnchor: NSLayoutXAxisAnchor](./trailinganchor.md)
  A layout anchor representing the trailing edge of the layout guide’s frame.
- [var widthAnchor: NSLayoutDimension](./widthanchor.md)
  A layout anchor representing the width of the layout guide’s frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uilayoutguide/rightanchor)*