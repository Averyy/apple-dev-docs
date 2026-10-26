# CGContextSetInterpolationQuality

**Framework**: Core Graphics  
**Kind**: func  
**Role**: Function

Sets the level of interpolation quality for a graphics context.

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
extern void CGContextSetInterpolationQuality(CGContextRef c, CGInterpolationQuality quality);
```

#### Discussion

Interpolation quality is merely a hint to the context—not all contexts support all interpolation quality levels.

## Parameters

- `c`: The graphics context to modify.
- `quality`: A constant that specifies the required level of interpolation quality. For possible values, see [`CGInterpolationQuality`](./cginterpolationquality.md).

## See Also

### Drawing Images and PDF Content
- [CGContextDrawTiledImage](./cgcontextdrawtiledimage.md)
  Repeatedly draws an image, scaled to the provided rectangle, to fill the current clip region.
- [CGContextDrawImage](./cgcontextdrawimage.md)
  Draws an image into a graphics context.
- [func drawPDFPage(CGPDFPage)](./cgcontext/drawpdfpage%28_%29.md)
  Draws the content of a PDF page into the current graphics context.
- [var interpolationQuality: CGInterpolationQuality](./cgcontext/interpolationquality.md)
  Returns the current level of interpolation quality for a graphics context.
- [enum CGInterpolationQuality](./cginterpolationquality.md)
  Levels of interpolation quality for rendering an image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgcontextsetinterpolationquality)*