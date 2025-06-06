# draw(in:from:operation:fraction:respectFlipped:hints:)

**Framework**: AppKit  
**Kind**: method

Draws all or part of the image in the specified rectangle respecting the hints and the orientation of the current coordinate system.

**Availability**:
- macOS 10.6+

## Declaration

```swift
func draw(in dstSpacePortionRect: NSRect, from srcSpacePortionRect: NSRect, operation op: NSCompositingOperation, fraction requestedAlpha: CGFloat, respectFlipped respectContextIsFlipped: Bool, hints: [NSImageRep.HintKey : Any]?)
```

#### Discussion

If the `srcSpacePortionRect` and `dstSpacePortionRect` rectangles have different sizes, the source portion of the image is scaled to fit the specified destination rectangle.

## Parameters

- `dstSpacePortionRect`: The rectangle in which to draw the image, specified in the current coordinate system.
- `srcSpacePortionRect`: The source rectangle specifying the portion of the image you want to draw. The coordinates of this rectangle must be specified using the image’s own coordinate system. If you pass in  , the entire image is drawn.
- `op`: The compositing operation to use when drawing the image. See the   constants.
- `requestedAlpha`: The alpha of the image, specified as a value from 0.0 to 1.0. Specifying a value of 0.0 draws the image as fully transparent while a value of 1.0 draws the image as fully opaque. Values greater than 1.0 are interpreted as 1.0.
- `respectContextIsFlipped`:   if the drawing should respect the context flipped state, otherwise  .
- `hints`: An optional dictionary of hints that provide more context for selecting or generating the image. See   for a summary of the possible key-value pairs.

## See Also

- [func draw(in: NSRect)](nsimage/draw(in:).md)
  Draws the image in the specified rectangle.
- [func draw(at: NSPoint, from: NSRect, operation: NSCompositingOperation, fraction: CGFloat)](nsimage/draw(at:from:operation:fraction:).md)
  Draws all or part of the image at the specified point in the current coordinate system.
- [func draw(in: NSRect, from: NSRect, operation: NSCompositingOperation, fraction: CGFloat)](nsimage/draw(in:from:operation:fraction:).md)
  Draws all or part of the image in the specified rectangle in the current coordinate system.
- [func drawRepresentation(NSImageRep, in: NSRect) -> Bool](nsimage/drawrepresentation(_:in:).md)
  Draws the image using the specified image representation object.
- [enum NSCompositingOperation](nscompositingoperation.md)
  Constants that describe compositing operators in terms of source and destination images, each having an opaque and transparent region.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsimage/draw(in:from:operation:fraction:respectflipped:hints:))*