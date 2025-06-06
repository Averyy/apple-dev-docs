# init(colorSpace:colorComponents:locations:count:)

**Framework**: Core Graphics  
**Kind**: init

Creates a CGGradient object from a color space and the provided color components and locations.

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
init?(colorSpace space: CGColorSpace, colorComponents components: UnsafePointer<CGFloat>, locations: UnsafePointer<CGFloat>?, count: Int)
```

#### Return Value

A CGGradient object.

## Parameters

- `space`: The color space to use for the gradient. You cannot use a pattern or indexed color space.
- `components`: The number of items in this array should be the product of   and the number of components in the color space. For example, if the color space is an RGBA color space and you want to use two colors in the gradient (one for a starting location and another for an ending location), then you need to provide 8 values in  —red, green, blue, and alpha values for the first color, followed by red, green, blue, and alpha values for the second color.
- `locations`: If    is  , the first color in    is assigned to location  , the last color in   is assigned to location  , and intervening colors are assigned locations that are at equal intervals in between.
- `count`: The number of locations provided in the   parameters.

## See Also

- [func drawRadialGradient(CGGradient, startCenter: CGPoint, startRadius: CGFloat, endCenter: CGPoint, endRadius: CGFloat, options: CGGradientDrawingOptions)](cgcontext/drawradialgradient(_:startcenter:startradius:endcenter:endradius:options:).md)
  Paints a gradient fill that varies along the area defined by the provided starting and ending circles.
- [Quartz 2D Programming Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/drawingwithquartz2d/Introduction/Introduction.html#//apple_ref/doc/uid/TP30001066)
- [func drawLinearGradient(CGGradient, start: CGPoint, end: CGPoint, options: CGGradientDrawingOptions)](cgcontext/drawlineargradient(_:start:end:options:).md)
  Paints a gradient fill that varies along the line defined by the provided starting and ending points.
- [init?(colorsSpace: CGColorSpace?, colors: CFArray, locations: UnsafePointer<CGFloat>?)](cggradient/init(colorsspace:colors:locations:).md)
  Creates a gradient object from a color space and the provided color objects and locations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cggradient/init(colorspace:colorcomponents:locations:count:))*