# draw(_:)

**Framework**: AppKit  
**Kind**: method

Draws the receiver’s image that appears in the supplied rectangle.

**Availability**:
- macOS ?+

## Declaration

```swift
func draw(_ rect: NSRect)
```

## Parameters

- `rect`: The rectangle to be drawn, in the ruler view’s coordinate system.

## See Also

- [var imageRectInRuler: NSRect](nsrulermarker/imagerectinruler.md)
  The rectangle occupied by the receiver’s image.
- [var isDragging: Bool](nsrulermarker/isdragging.md)
  A Boolean that indicates whether the receiver is being dragged.
- [func trackMouse(with: NSEvent, adding: Bool) -> Bool](nsrulermarker/trackmouse(with:adding:).md)
  Handles user manipulation of the receiver in its ruler view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsrulermarker/draw(_:))*