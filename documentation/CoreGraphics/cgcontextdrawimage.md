# CGContextDrawImage

**Framework**: Core Graphics  
**Kind**: func  
**Role**: Function

Draws an image into a graphics context.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.0+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```c
extern void CGContextDrawImage(CGContextRef c, CGRect rect, CGImageRef image);
```

#### Discussion

The image is scaled—disproportionately, if necessary—to fit the bounds specified by the `rect` parameter.

## Parameters

- `c`: The graphics context in which to draw the image.
- `rect`: The location and dimensions in user space of the bounding box in which to draw the image.
- `image`: The image to draw.

## See Also

### Drawing Images and PDF Content
- [CGContextDrawTiledImage](./cgcontextdrawtiledimage.md)
  Repeatedly draws an image, scaled to the provided rectangle, to fill the current clip region.
- [func drawPDFPage(CGPDFPage)](./cgcontext/drawpdfpage%28_%29.md)
  Draws the content of a PDF page into the current graphics context.
- [var interpolationQuality: CGInterpolationQuality](./cgcontext/interpolationquality.md)
  Returns the current level of interpolation quality for a graphics context.
- [CGContextSetInterpolationQuality](./cgcontextsetinterpolationquality.md)
  Sets the level of interpolation quality for a graphics context.
- [enum CGInterpolationQuality](./cginterpolationquality.md)
  Levels of interpolation quality for rendering an image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgcontextdrawimage)*