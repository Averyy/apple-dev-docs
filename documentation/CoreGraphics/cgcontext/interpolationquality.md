# interpolationQuality

**Framework**: Core Graphics  
**Kind**: property

Returns the current level of interpolation quality for a graphics context.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.0+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var interpolationQuality: CGInterpolationQuality { get set }
```

#### Discussion

Interpolation quality is a graphics state parameter that provides a hint for the level of quality to use for image interpolation (for example, when scaling the image). Not all contexts support all interpolation quality levels.

## See Also

- [func draw(CGImage, in: CGRect, byTiling: Bool)](cgcontext/draw(_:in:bytiling:).md)
  Draws an image in the specified area.
- [func drawPDFPage(CGPDFPage)](cgcontext/drawpdfpage(_:).md)
  Draws the content of a PDF page into the current graphics context.
- [enum CGInterpolationQuality](cginterpolationquality.md)
  Levels of interpolation quality for rendering an image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgcontext/interpolationquality)*