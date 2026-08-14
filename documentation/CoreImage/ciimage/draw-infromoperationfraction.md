# draw(in:from:operation:fraction:)

**Framework**: Core Image  
**Kind**: method

Draws all or part of the image in the specified rectangle in the current coordinate system

**Availability**:
- macOS ?+

## Declaration

```swift
func draw(in rect: NSRect, from fromRect: NSRect, operation op: NSCompositingOperation, fraction delta: CGFloat)
```

#### Discussion

If the `srcRect` and `dstRect` rectangles have different sizes, the source portion of the image is scaled to fit the specified destination rectangle. The image is otherwise positioned and oriented using the current coordinate system.

## Parameters

- `rect`: The rectangle in which to draw the image.
- `fromRect`: The source rectangle specifying the portion of the image you want to draw. The coordinates of this rectangle must be specified using the image’s own coordinate system.
- `op`: The compositing operation to use when drawing the image. For details, see [`NSCompositingOperation`](https://developer.apple.com/documentation/appkit/nscompositingoperation).
- `delta`: The opacity of the image, specified as a value from `0.0` to `1.0`. Specifying a value of `0.0` draws the image as fully transparent while a value of `1.0` draws the image as fully opaque. Values greater than `1.0` are interpreted as `1.0`.

## See Also

- [func draw(at: NSPoint, from: NSRect, operation: NSCompositingOperation, fraction: CGFloat)](ciimage/draw(at:from:operation:fraction:).md)
  Draws all or part of the image at the specified point in the current coordinate system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciimage/draw(in:from:operation:fraction:))*