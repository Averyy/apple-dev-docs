# lastBaselineAnchor

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A layout anchor representing the baseline for the bottommost line of text in the view.

**Availability**:
- macOS 10.11+

## Declaration

```swift
var lastBaselineAnchor: NSLayoutYAxisAnchor { get }
```

```objc
@property (strong, readonly) NSLayoutYAxisAnchor * lastBaselineAnchor;
```

#### Discussion

For views with multiple lines of text, this anchor represents the baseline of the bottom row of text. Use this anchor to create constraints with this baseline. You can only combine this anchor with other [`NSLayoutYAxisAnchor`](../../UIKit/nslayoutyaxisanchor.md) anchors. For more information, see [`NSLayoutAnchor`](../../UIKit/nslayoutanchor.md).

## See Also

### Creating Constraints Using Layout Anchors
- [var bottomAnchor: NSLayoutYAxisAnchor](./bottomanchor.md)
  A layout anchor representing the bottom edge of the view’s frame.
- [var centerXAnchor: NSLayoutXAxisAnchor](./centerxanchor.md)
  A layout anchor representing the horizontal center of the view’s frame.
- [var centerYAnchor: NSLayoutYAxisAnchor](./centeryanchor.md)
  A layout anchor representing the vertical center of the view’s frame.
- [var firstBaselineAnchor: NSLayoutYAxisAnchor](./firstbaselineanchor.md)
  A layout anchor representing the baseline for the topmost line of text in the view.
- [var heightAnchor: NSLayoutDimension](./heightanchor.md)
  A layout anchor representing the height of the view’s frame.
- [var leadingAnchor: NSLayoutXAxisAnchor](./leadinganchor.md)
  A layout anchor representing the leading edge of the view’s frame.
- [var leftAnchor: NSLayoutXAxisAnchor](./leftanchor.md)
  A layout anchor representing the left edge of the view’s frame.
- [var rightAnchor: NSLayoutXAxisAnchor](./rightanchor.md)
  A layout anchor representing the right edge of the view’s frame.
- [var topAnchor: NSLayoutYAxisAnchor](./topanchor.md)
  A layout anchor representing the top edge of the view’s frame.
- [var trailingAnchor: NSLayoutXAxisAnchor](./trailinganchor.md)
  A layout anchor representing the trailing edge of the view’s frame.
- [var widthAnchor: NSLayoutDimension](./widthanchor.md)
  A layout anchor representing the width of the view’s frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/lastbaselineanchor)*