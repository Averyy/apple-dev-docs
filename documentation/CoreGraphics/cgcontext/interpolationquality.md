# interpolationQuality

**Framework**: Core Graphics  
**Kind**: property  
**Role**: Instance Property

Returns the current level of interpolation quality for a graphics context.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.0+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var interpolationQuality: CGInterpolationQuality { get set }
```

```c
extern CGInterpolationQuality CGContextGetInterpolationQuality(CGContextRef c);
```

#### Discussion

Interpolation quality is a graphics state parameter that provides a hint for the level of quality to use for image interpolation (for example, when scaling the image). Not all contexts support all interpolation quality levels.

## See Also

### Drawing Images and PDF Content
- [func draw(CGImage, in: CGRect, byTiling: Bool)](./draw%28_,in,bytiling%29.md)
  Draws an image in the specified area.
- [func drawPDFPage(CGPDFPage)](./drawpdfpage%28_%29.md)
  Draws the content of a PDF page into the current graphics context.
- [enum CGInterpolationQuality](../cginterpolationquality.md)
  Levels of interpolation quality for rendering an image.
- [CGContextDrawTiledImage](../cgcontextdrawtiledimage.md)
  Repeatedly draws an image, scaled to the provided rectangle, to fill the current clip region.
- [CGContextDrawImage](../cgcontextdrawimage.md)
  Draws an image into a graphics context.
### Related Documentation
- [CGContextSetInterpolationQuality](../cgcontextsetinterpolationquality.md)
  Sets the level of interpolation quality for a graphics context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgcontext/interpolationquality)*