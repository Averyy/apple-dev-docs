# image

**Framework**: AppKit  
**Kind**: property

The receiver’s image.

**Availability**:
- macOS ?+

## Declaration

```swift
var image: NSImage { get set }
```

#### Discussion

The image used to draw the marker must be appropriate for the orientation of the ruler. Markers may need to look different on a horizontal ruler than on a vertical ruler, and the ruler view neither scales nor rotates the images.

## See Also

- [var imageOrigin: NSPoint](nsrulermarker/imageorigin.md)
  The point in the receiver’s image that is positioned at the receiver’s location on the ruler view.
- [var imageRectInRuler: NSRect](nsrulermarker/imagerectinruler.md)
  The rectangle occupied by the receiver’s image.
- [var thicknessRequiredInRuler: CGFloat](nsrulermarker/thicknessrequiredinruler.md)
  The amount of the receiver’s image that’s displayed above or to the left of the ruler view’s baseline.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsrulermarker/image)*