# scroll(to:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Changes the origin of the clip view’s bounds rectangle to `newOrigin`.

**Availability**:
- macOS

## Declaration

```swift
func scroll(to newOrigin: NSPoint)
```

```objc
- (void) scrollToPoint:(NSPoint) newOrigin;
```

## See Also

### Scrolling
- [func autoscroll(with: NSEvent) -> Bool](./autoscroll%28with%29.md)
  Scrolls the clip view proportionally to `theEvent`’s distance outside of it.
- [func constrainBoundsRect(NSRect) -> NSRect](./constrainboundsrect%28_%29.md)
  Constrains the bounds of the clip view while the user is magnifying and scrolling.
- [func constrainScroll(NSPoint) -> NSPoint](./constrainscroll%28_%29.md)
  Returns a scroll point adjusted from the proposed new origin, if necessary, to guarantee the view will lie within its document view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsclipview/scroll(to:))*