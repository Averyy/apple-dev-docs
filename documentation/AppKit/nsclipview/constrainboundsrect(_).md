# constrainBoundsRect(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Constrains the bounds of the clip view while the user is magnifying and scrolling.

**Availability**:
- macOS 10.9+

## Declaration

```swift
func constrainBoundsRect(_ proposedBounds: NSRect) -> NSRect
```

```objc
- (NSRect) constrainBoundsRect:(NSRect) proposedBounds;
```

#### Return Value

A bounds rectangle.

#### Discussion

Note that you can move an implementation of the deprecated [`constrainScroll(_:)`](./constrainscroll%28_%29.md) to this method by adjusting the origin of `proposedBounds` (instead of using the `newOrigin` parameter in `-constrainScrollPoint:`). To preserve compatibility, if a subclass overrides `-constrainScrollPoint:`, the default behavior of [`constrainBoundsRect(_:)`](./constrainboundsrect%28_%29.md) will be to use that `-constrainScrollPoint:` to adjust the origin of `proposedBounds`, and to not change the size.

## Parameters

- `proposedBounds`: The bounds to use to ensure that the view will still lie within its document view.

## See Also

### Scrolling
- [func scroll(to: NSPoint)](./scroll%28to%29.md)
  Changes the origin of the clip view’s bounds rectangle to `newOrigin`.
- [func autoscroll(with: NSEvent) -> Bool](./autoscroll%28with%29.md)
  Scrolls the clip view proportionally to `theEvent`’s distance outside of it.
- [func constrainScroll(NSPoint) -> NSPoint](./constrainscroll%28_%29.md)
  Returns a scroll point adjusted from the proposed new origin, if necessary, to guarantee the view will lie within its document view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsclipview/constrainboundsrect(_:))*