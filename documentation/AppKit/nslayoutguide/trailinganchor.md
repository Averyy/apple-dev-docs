# trailingAnchor

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A layout anchor representing the trailing edge of the layout guide’s frame.

**Availability**:
- macOS 10.11+

## Declaration

```swift
var trailingAnchor: NSLayoutXAxisAnchor { get }
```

```objc
@property (strong, readonly) NSLayoutXAxisAnchor * trailingAnchor;
```

#### Discussion

Use this anchor to create constraints with the layout guide’s trailing edge. You can combine this anchor only with a subset of the [`NSLayoutXAxisAnchor`](../../UIKit/nslayoutxaxisanchor.md) anchors. You can combine a [`trailingAnchor`](./trailinganchor.md) with another `trailingAnchor`, a `leadingAnchor`, or a `centerXAnchor`. For more information, see [`NSLayoutAnchor`](../../UIKit/nslayoutanchor.md).

## See Also

### Creating Constraints Using Layout Anchors
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
- [var rightAnchor: NSLayoutXAxisAnchor](./rightanchor.md)
  A layout anchor representing the right edge of the layout guide’s frame.
- [var topAnchor: NSLayoutYAxisAnchor](./topanchor.md)
  A layout anchor representing the top edge of the layout guide’s frame.
- [var widthAnchor: NSLayoutDimension](./widthanchor.md)
  A layout anchor representing the width of the layout guide’s frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nslayoutguide/trailinganchor)*