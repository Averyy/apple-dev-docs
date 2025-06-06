# constrainScroll(_:)

**Framework**: AppKit  
**Kind**: method

Returns a scroll point adjusted from the proposed new origin, if necessary, to guarantee the view will lie within its document view.

**Availability**:
- macOS 10.0+

## Declaration

```swift
@MainActor
func constrainScroll(_ newOrigin: NSPoint) -> NSPoint
```

#### Return Value

A point which will guarantee the view will lie within its document view.

#### Discussion

For example, if the x-coordinate of `newOrigin` lies to the left of the document view’s origin, then the x-coordinate returned is set to that of the x-coordinate of the document view’s origin.

## Parameters

- `newOrigin`: Origin proposed.

## See Also

- [func scroll(to: NSPoint)](nsclipview/scroll(to:).md)
  Changes the origin of the clip view’s bounds rectangle to `newOrigin`.
- [func autoscroll(with: NSEvent) -> Bool](nsclipview/autoscroll(with:).md)
  Scrolls the clip view proportionally to `theEvent`’s distance outside of it.
- [func constrainBoundsRect(NSRect) -> NSRect](nsclipview/constrainboundsrect(_:).md)
  Constrains the bounds of the clip view while the user is magnifying and scrolling.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsclipview/constrainscroll(_:))*