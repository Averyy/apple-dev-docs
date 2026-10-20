# draw(in:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Draws the image in the specified rectangle.

**Availability**:
- macOS 10.9+

## Declaration

```swift
func draw(in rect: NSRect)
```

```objc
- (void) drawInRect:(NSRect) rect;
```

#### Discussion

This method draws the entire image in the specified rectangle, scaling the image as needed. The method composites the image using the [`NSCompositeSourceOver`](../nscompositesourceover.md) operation

## Parameters

- `rect`: The rectangle in which to draw the image, specified in the current coordinate system.

## See Also

### Drawing Images
- [func draw(at: NSPoint, from: NSRect, operation: NSCompositingOperation, fraction: CGFloat)](./draw%28at,from,operation,fraction%29.md)
  Draws all or part of the image at the specified point in the current coordinate system.
- [func draw(in: NSRect, from: NSRect, operation: NSCompositingOperation, fraction: CGFloat)](./draw%28in,from,operation,fraction%29.md)
  Draws all or part of the image in the specified rectangle in the current coordinate system.
- [func draw(in: NSRect, from: NSRect, operation: NSCompositingOperation, fraction: CGFloat, respectFlipped: Bool, hints: [NSImageRep.HintKey : Any]?)](./draw%28in,from,operation,fraction,respectflipped,hints%29.md)
  Draws all or part of the image in the specified rectangle respecting the hints and the orientation of the current coordinate system.
- [func drawRepresentation(NSImageRep, in: NSRect) -> Bool](./drawrepresentation%28_,in%29.md)
  Draws the image using the specified image representation object.
- [enum NSCompositingOperation](../nscompositingoperation.md)
  Constants that describe compositing operators in terms of source and destination images, each having an opaque and transparent region.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsimage/draw(in:))*