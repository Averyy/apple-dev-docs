# bottomAnchor

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A layout anchor representing the bottom edge of the layout guide’s frame.

**Availability**:
- macOS 10.11+

## Declaration

```swift
var bottomAnchor: NSLayoutYAxisAnchor { get }
```

```objc
@property (strong, readonly) NSLayoutYAxisAnchor * bottomAnchor;
```

#### Discussion

Use this anchor to create constraints with the layout guide’s bottom edge. You can combine this anchor only with other [`NSLayoutYAxisAnchor`](../../UIKit/nslayoutyaxisanchor.md) anchors. For more information, see [`NSLayoutAnchor`](../../UIKit/nslayoutanchor.md).

## See Also

### Creating Constraints Using Layout Anchors
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
- [var trailingAnchor: NSLayoutXAxisAnchor](./trailinganchor.md)
  A layout anchor representing the trailing edge of the layout guide’s frame.
- [var widthAnchor: NSLayoutDimension](./widthanchor.md)
  A layout anchor representing the width of the layout guide’s frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nslayoutguide/bottomanchor)*