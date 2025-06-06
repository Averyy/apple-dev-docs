# scroll(to:)

**Framework**: AppKit  
**Kind**: method

Changes the origin of the clip view’s bounds rectangle to `newOrigin`.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func scroll(to newOrigin: NSPoint)
```

## See Also

- [func autoscroll(with: NSEvent) -> Bool](nsclipview/autoscroll(with:).md)
  Scrolls the clip view proportionally to `theEvent`’s distance outside of it.
- [func constrainScroll(NSPoint) -> NSPoint](nsclipview/constrainscroll(_:).md)
  Returns a scroll point adjusted from the proposed new origin, if necessary, to guarantee the view will lie within its document view.
- [func constrainBoundsRect(NSRect) -> NSRect](nsclipview/constrainboundsrect(_:).md)
  Constrains the bounds of the clip view while the user is magnifying and scrolling.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsclipview/scroll(to:))*