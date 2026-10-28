# safeAreaRect

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A rectangle in the view’s coordinate system that contains the unobscured portion of the view.

**Availability**:
- macOS 11.0+

## Declaration

```swift
var safeAreaRect: NSRect { get }
```

```objc
@property (readonly) NSRect safeAreaRect;
```

## Discussion

The safe area of a view reflects the area not covered by navigation bars, tab bars, toolbars, and other ancestor views that might obscure the current view. Draw content inside this rectangle to ensure it isn’t covered by other content.

## See Also

### Respecting the View’s Safe Area
- [var safeAreaInsets: NSEdgeInsets](./safeareainsets.md)
  The distances from the edges of your view that define the safe area.
- [var additionalSafeAreaInsets: NSEdgeInsets](./additionalsafeareainsets.md)
  Custom insets that you specify to modify your view’s safe area
- [var safeAreaLayoutGuide: NSLayoutGuide](./safearealayoutguide.md)
  The layout guide you use to position content inside your view’s safe area.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/safearearect)*