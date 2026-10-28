# init(colorsSpace:colors:locations:)

**Framework**: Core Graphics  
**Kind**: init  
**Role**: Initializer

Creates a gradient object from a color space and the provided color objects and locations.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
init?(colorsSpace space: CGColorSpace?, colors: CFArray, locations: UnsafePointer<CGFloat>?)
```

```c
extern CGGradientRefCGGradientCreateWithColors(CGColorSpaceRef space, CFArrayRef colors, const CGFloat *locations);
```

## Return Value

A [`CGGradient`](../cggradient.md) object.

## Parameters

- `space`: The color space to use for the gradient. You cannot use a pattern or indexed color space.
- `colors`: A non-empty array of [`CGColor`](../cgcolor.md) objects that should be in the color space specified by `space`. If `space` is not `NULL`, each color will be converted (if necessary) to that color space and the gradient will drawn in that color space. Otherwise, each color will be converted to and drawn in the GenericRGB color space.
- `locations`: The location for each color provided in `colors`; each location must be a [`CGFloat`](../../CoreFoundation/cgfloat-swift.struct.md) value in the range of `0` to `1`, inclusive. If `0` and `1` are not in the `locations` array, Quartz uses the colors provided that are closest to `0` and `1` for those locations.

  If `locations` is `NULL`, the first color in `colors` is assigned to location `0`, the last color in `colors` is assigned to location `1`, and intervening colors are assigned locations that are at equal intervals in between.

  The `locations` array should contain the same number of items as the `colors` array.

## See Also

### Related Documentation
- [func drawRadialGradient(CGGradient, startCenter: CGPoint, startRadius: CGFloat, endCenter: CGPoint, endRadius: CGFloat, options: CGGradientDrawingOptions)](../cgcontext/drawradialgradient%28_,startcenter,startradius,endcenter,endradius,options%29.md)
  Paints a gradient fill that varies along the area defined by the provided starting and ending circles.
- [func drawLinearGradient(CGGradient, start: CGPoint, end: CGPoint, options: CGGradientDrawingOptions)](../cgcontext/drawlineargradient%28_,start,end,options%29.md)
  Paints a gradient fill that varies along the line defined by the provided starting and ending points.
### Creating Gradient Instances
- [init?(colorSpace: CGColorSpace, colorComponents: UnsafePointer<CGFloat>, locations: UnsafePointer<CGFloat>?, count: Int)](./init%28colorspace,colorcomponents,locations,count%29.md)
  Creates a CGGradient object from a color space and the provided color components and locations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cggradient/init(colorsspace:colors:locations:))*