# constrainScroll(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns a scroll point adjusted from the proposed new origin, if necessary, to guarantee the view will lie within its document view.

**Availability**:
- macOS 10.0+ - Deprecated in 10.10

> **Deprecated**: Use [`constrainBoundsRect(_:)`](./constrainboundsrect%28_%29.md) instead.

## Declaration

```swift
func constrainScroll(_ newOrigin: NSPoint) -> NSPoint
```

```objc
- (NSPoint) constrainScrollPoint:(NSPoint) newOrigin;
```

## Return Value

A point which will guarantee the view will lie within its document view.

## Discussion

For example, if the x-coordinate of `newOrigin` lies to the left of the document view’s origin, then the x-coordinate returned is set to that of the x-coordinate of the document view’s origin.

## Parameters

- `newOrigin`: Origin proposed.

## See Also

### Scrolling
- [func scroll(to: NSPoint)](./scroll%28to%29.md)
  Changes the origin of the clip view’s bounds rectangle to `newOrigin`.
- [func autoscroll(with: NSEvent) -> Bool](./autoscroll%28with%29.md)
  Scrolls the clip view proportionally to `theEvent`’s distance outside of it.
- [func constrainBoundsRect(NSRect) -> NSRect](./constrainboundsrect%28_%29.md)
  Constrains the bounds of the clip view while the user is magnifying and scrolling.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsclipview/constrainscroll(_:))*