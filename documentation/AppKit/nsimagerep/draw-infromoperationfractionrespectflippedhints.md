# draw(in:from:operation:fraction:respectFlipped:hints:)

**Framework**: AppKit  
**Kind**: method

Draws all or part of the image in the specified rectangle in the current coordinate system.

**Availability**:
- macOS 10.6+

## Declaration

```swift
func draw(in dstSpacePortionRect: NSRect, from srcSpacePortionRect: NSRect, operation op: NSCompositingOperation, fraction requestedAlpha: CGFloat, respectFlipped respectContextIsFlipped: Bool, hints: [NSImageRep.HintKey : Any]?) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if the image was successfully drawn; otherwise, [`false`](https://developer.apple.com/documentation/Swift/false).

#### Discussion

If the `srcSpacePortionRect` and `dstSpacePortionRect` rectangles have different sizes, the source portion of the image is scaled to fit the specified destination rectangle.

## Parameters

- `dstSpacePortionRect`: The rectangle in which to draw the image, specified in the current coordinate system.
- `srcSpacePortionRect`: The source rectangle specifying the portion of the image you want to draw. The coordinates of this rectangle must be specified using the image’s own coordinate system. If you pass in  , the entire image is drawn.
- `op`: The compositing operation to use when drawing the image. See the   constants.
- `requestedAlpha`: The opacity of the image, specified as a value from 0.0 to 1.0. Specifying a value of 0.0 draws the image as fully transparent while a value of 1.0 draws the image as fully opaque. Values greater than 1.0 are interpreted as 1.0.
- `respectContextIsFlipped`:   if the flipped context of the receiver should be respected, otherwise  .
- `hints`: An optional dictionary of hints that provide more context for selecting or generating the image. See   for possible values.

## See Also

- [func draw() -> Bool](nsimagerep/draw.md)
  Implemented by subclasses to draw the image in the current coordinate system.
- [func draw(at: NSPoint) -> Bool](nsimagerep/draw(at:).md)
  Draws the image representation’s image data at the specified point in the current coordinate system.
- [func draw(in: NSRect) -> Bool](nsimagerep/draw(in:).md)
  Draws the image, scaling it (as needed) to fit the specified rectangle.
- [NSImageRep.HintKey](nsimagerep/hintkey.md)
  Constants for the keys to include in a hints dictionary when drawing the image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsimagerep/draw(in:from:operation:fraction:respectflipped:hints:))*