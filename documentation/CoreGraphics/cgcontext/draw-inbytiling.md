# draw(_:in:byTiling:)

**Framework**: Core Graphics  
**Kind**: method

Draws an image in the specified area.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst ?+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func draw(_ image: CGImage, in rect: CGRect, byTiling: Bool = false)
```

#### Discussion

This method scales the image (disproportionately, if necessary) to fit the bounds specified by the `rect` parameter.When the `byTiling` parameter is [`true`](https://developer.apple.com/documentation/swift/true), the image is tiled in user space—thus, unlike when drawing with patterns, the current transformation (see the [`ctm`](cgcontext/ctm.md) property) affects the final result.

## Parameters

- `image`: The image to draw.
- `rect`: The rectangle, in user space coordinates, in which to draw the image.
- `byTiling`: If   (the default), this method draws a single copy of the image in the area defined by the   parameter.

## See Also

- [func drawPDFPage(CGPDFPage)](cgcontext/drawpdfpage(_:).md)
  Draws the content of a PDF page into the current graphics context.
- [var interpolationQuality: CGInterpolationQuality](cgcontext/interpolationquality.md)
  Returns the current level of interpolation quality for a graphics context.
- [enum CGInterpolationQuality](cginterpolationquality.md)
  Levels of interpolation quality for rendering an image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgcontext/draw(_:in:bytiling:))*