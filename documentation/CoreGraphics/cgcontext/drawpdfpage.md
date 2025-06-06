# drawPDFPage(_:)

**Framework**: Core Graphics  
**Kind**: method

Draws the content of a PDF page into the current graphics context.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.3+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func drawPDFPage(_ page: CGPDFPage)
```

#### Discussion

This function works in conjunction with the [`CGPDFPage`](cgpdfpage.md) type to draw individual PDF pages into a context.

## Parameters

- `page`: A Core Graphics PDF page.

## See Also

- [func draw(CGImage, in: CGRect, byTiling: Bool)](cgcontext/draw(_:in:bytiling:).md)
  Draws an image in the specified area.
- [var interpolationQuality: CGInterpolationQuality](cgcontext/interpolationquality.md)
  Returns the current level of interpolation quality for a graphics context.
- [enum CGInterpolationQuality](cginterpolationquality.md)
  Levels of interpolation quality for rendering an image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgcontext/drawpdfpage(_:))*