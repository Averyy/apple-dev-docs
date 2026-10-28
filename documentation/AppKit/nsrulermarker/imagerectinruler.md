# imageRectInRuler

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The rectangle occupied by the receiver’s image.

**Availability**:
- macOS

## Declaration

```swift
var imageRectInRuler: NSRect { get }
```

```objc
@property (readonly) NSRect imageRectInRuler;
```

## Discussion

The rectangle occupied by the receiver’s image, in the ruler view’s coordinate system, accounting for whether the ruler view’s coordinate system is flipped.

## See Also

### Related Documentation
- [func draw(NSRect)](./draw%28_%29.md)
  Draws the receiver’s image that appears in the supplied rectangle.
### Setting the image
- [var image: NSImage](./image.md)
  The receiver’s image.
- [var imageOrigin: NSPoint](./imageorigin.md)
  The point in the receiver’s image that is positioned at the receiver’s location on the ruler view.
- [var thicknessRequiredInRuler: CGFloat](./thicknessrequiredinruler.md)
  The amount of the receiver’s image that’s displayed above or to the left of the ruler view’s baseline.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsrulermarker/imagerectinruler)*