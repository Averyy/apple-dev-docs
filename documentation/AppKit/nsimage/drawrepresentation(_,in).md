# drawRepresentation(_:in:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Draws the image using the specified image representation object.

**Availability**:
- macOS

## Declaration

```swift
func drawRepresentation(_ imageRep: NSImageRep, in rect: NSRect) -> Bool
```

```objc
- (BOOL) drawRepresentation:(NSImageRep *) imageRep inRect:(NSRect) rect;
```

#### Return Value

[`true`](../../Swift/true.md) if the image was successfully drawn; otherwise, returns [`false`](../../Swift/false.md).

#### Discussion

This method fills the specified rectangle with the image’s current background color and then sends a message to the specified image representation asking if to draw itself. If the image supports the ability to scale itself when it is resized, this method sends a [`draw(in:)`](../nsimagerep/draw%28in%29.md) message; otherwise, it sends a [`draw(at:)`](../nsimagerep/draw%28at%29.md) message.

You should not call this method directly; an `NSImage` object uses it to cache and print its image representations. You can override this method to change the way images are rendered into their caches and onto the printed page. For example, you could scale or rotate the coordinate system before sending this message to `super` to continue rendering the image representation.

If the background color is fully transparent and the image data is not being cached, the specified rectangle is not to be filled before the representation draws.

## Parameters

- `imageRep`: The image representation object to be drawn.
- `rect`: The rectangle in which to draw the image representation, specified in the current coordinate system.

## See Also

### Related Documentation
- [var backgroundColor: NSColor](./backgroundcolor.md)
  The background color for the image.
### Drawing Images
- [func draw(in: NSRect)](./draw%28in%29.md)
  Draws the image in the specified rectangle.
- [func draw(at: NSPoint, from: NSRect, operation: NSCompositingOperation, fraction: CGFloat)](./draw%28at,from,operation,fraction%29.md)
  Draws all or part of the image at the specified point in the current coordinate system.
- [func draw(in: NSRect, from: NSRect, operation: NSCompositingOperation, fraction: CGFloat)](./draw%28in,from,operation,fraction%29.md)
  Draws all or part of the image in the specified rectangle in the current coordinate system.
- [func draw(in: NSRect, from: NSRect, operation: NSCompositingOperation, fraction: CGFloat, respectFlipped: Bool, hints: [NSImageRep.HintKey : Any]?)](./draw%28in,from,operation,fraction,respectflipped,hints%29.md)
  Draws all or part of the image in the specified rectangle respecting the hints and the orientation of the current coordinate system.
- [enum NSCompositingOperation](../nscompositingoperation.md)
  Constants that describe compositing operators in terms of source and destination images, each having an opaque and transparent region.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsimage/drawrepresentation(_:in:))*