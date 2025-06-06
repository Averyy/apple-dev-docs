# imageRectInRuler

**Framework**: AppKit  
**Kind**: property

The rectangle occupied by the receiver’s image.

**Availability**:
- macOS ?+

## Declaration

```swift
var imageRectInRuler: NSRect { get }
```

#### Discussion

The rectangle occupied by the receiver’s image, in the ruler view’s coordinate system, accounting for whether the ruler view’s coordinate system is flipped.

## See Also

- [func draw(NSRect)](nsrulermarker/draw(_:).md)
  Draws the receiver’s image that appears in the supplied rectangle.
- [var image: NSImage](nsrulermarker/image.md)
  The receiver’s image.
- [var imageOrigin: NSPoint](nsrulermarker/imageorigin.md)
  The point in the receiver’s image that is positioned at the receiver’s location on the ruler view.
- [var thicknessRequiredInRuler: CGFloat](nsrulermarker/thicknessrequiredinruler.md)
  The amount of the receiver’s image that’s displayed above or to the left of the ruler view’s baseline.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsrulermarker/imagerectinruler)*