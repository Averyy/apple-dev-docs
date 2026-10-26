# CGContextDrawTiledImage

**Framework**: Core Graphics  
**Kind**: func  
**Role**: Function

Repeatedly draws an image, scaled to the provided rectangle, to fill the current clip region.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```c
extern void CGContextDrawTiledImage(CGContextRef c, CGRect rect, CGImageRef image);
```

#### Discussion

Core Graphics draws the scaled image starting at the origin of the rectangle in user space, then moves to a new point (horizontally by the width of the tile and/or vertically by the height of the tile), draws the scaled image, moves again, draws again, and so on, until the current clip region is tiled with copies of the image. Unlike patterns, the image is tiled in user space, so transformations applied to the CTM affect the final result.

## Parameters

- `c`: The graphics context in which to draw the image.
- `rect`: A rectangle that specifies the origin and size of the destination tile. The image is scaled—disproportionately, if necessary—to fit the bounds specified by the `rect` parameter.
- `image`: The image to draw.

## See Also

### Drawing Images and PDF Content
- [CGContextDrawImage](./cgcontextdrawimage.md)
  Draws an image into a graphics context.
- [func drawPDFPage(CGPDFPage)](./cgcontext/drawpdfpage%28_%29.md)
  Draws the content of a PDF page into the current graphics context.
- [var interpolationQuality: CGInterpolationQuality](./cgcontext/interpolationquality.md)
  Returns the current level of interpolation quality for a graphics context.
- [CGContextSetInterpolationQuality](./cgcontextsetinterpolationquality.md)
  Sets the level of interpolation quality for a graphics context.
- [enum CGInterpolationQuality](./cginterpolationquality.md)
  Levels of interpolation quality for rendering an image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgcontextdrawtiledimage)*