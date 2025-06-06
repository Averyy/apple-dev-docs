# init(colorsSpace:colors:locations:)

**Framework**: Core Graphics  
**Kind**: init

Creates a gradient object from a color space and the provided color objects and locations.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
init?(colorsSpace space: CGColorSpace?, colors: CFArray, locations: UnsafePointer<CGFloat>?)
```

#### Return Value

A [`CGGradient`](cggradient.md) object.

## Parameters

- `space`: The color space to use for the gradient. You cannot use a pattern or indexed color space.
- `colors`: A non-empty array of   objects that should be in the color space specified by  . If   is not  , each color will be converted (if necessary) to that color space and the gradient will drawn in that color space. Otherwise, each color will be converted to and drawn in the GenericRGB color space.
- `locations`: The   array should contain the same number of items as the   array.

## See Also

- [func drawRadialGradient(CGGradient, startCenter: CGPoint, startRadius: CGFloat, endCenter: CGPoint, endRadius: CGFloat, options: CGGradientDrawingOptions)](cgcontext/drawradialgradient(_:startcenter:startradius:endcenter:endradius:options:).md)
  Paints a gradient fill that varies along the area defined by the provided starting and ending circles.
- [func drawLinearGradient(CGGradient, start: CGPoint, end: CGPoint, options: CGGradientDrawingOptions)](cgcontext/drawlineargradient(_:start:end:options:).md)
  Paints a gradient fill that varies along the line defined by the provided starting and ending points.
- [init?(colorSpace: CGColorSpace, colorComponents: UnsafePointer<CGFloat>, locations: UnsafePointer<CGFloat>?, count: Int)](cggradient/init(colorspace:colorcomponents:locations:count:).md)
  Creates a CGGradient object from a color space and the provided color components and locations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cggradient/init(colorsspace:colors:locations:))*