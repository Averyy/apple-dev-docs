# draw(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Draws the receiver’s image that appears in the supplied rectangle.

**Availability**:
- macOS

## Declaration

```swift
func draw(_ rect: NSRect)
```

```objc
- (void) drawRect:(NSRect) rect;
```

## Parameters

- `rect`: The rectangle to be drawn, in the ruler view’s coordinate system.

## See Also

### Related Documentation
- [var imageRectInRuler: NSRect](./imagerectinruler.md)
  The rectangle occupied by the receiver’s image.
### Drawing and event handling
- [var isDragging: Bool](./isdragging.md)
  A Boolean that indicates whether the receiver is being dragged.
- [func trackMouse(with: NSEvent, adding: Bool) -> Bool](./trackmouse%28with,adding%29.md)
  Handles user manipulation of the receiver in its ruler view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsrulermarker/draw(_:))*