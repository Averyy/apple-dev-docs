# setStrokeColor(red:green:blue:alpha:)

**Framework**: Core Graphics  
**Kind**: method  
**Role**: Instance Method

Sets the current stroke color to a value in the DeviceRGB color space.

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
func setStrokeColor(red: CGFloat, green: CGFloat, blue: CGFloat, alpha: CGFloat)
```

```c
extern void CGContextSetRGBStrokeColor(CGContextRef c, CGFloat red, CGFloat green, CGFloat blue, CGFloat alpha);
```

## Discussion

When you call this function, two things happen:

- Core Graphics sets the current stroke color space to DeviceRGB.
- Core Graphics sets the current stroke color to the value specified by the `red`, `green`, `blue`, and `alpha` parameters.

## Parameters

- `red`: The red intensity value for the color to set. The DeviceRGB color space permits the specification of a value ranging from `0.0` (zero intensity) to `1.0` (full intensity).
- `green`: The green intensity value for the color to set. The DeviceRGB color space permits the specification of a value ranging from `0.0` (zero intensity) to `1.0` (full intensity).
- `blue`: The blue intensity value for the color to set. The DeviceRGB color space permits the specification of a value ranging from `0.0` (zero intensity) to `1.0` (full intensity).
- `alpha`: A value that specifies the opacity level. Values can range from `0.0` (transparent) to `1.0` (opaque). Values outside this range are clipped to `0.0` or `1.0`.

## See Also

### Setting Fill, Stroke, and Shadow Colors
- [func setFillColor(CGColor)](./setfillcolor%28_%29-8lhn8.md)
  Sets the current fill color in a graphics context, using a CGColor.
- [func setFillColor(UnsafePointer<CGFloat>)](./setfillcolor%28_%29-756dy.md)
  Sets the current fill color.
- [func setFillColor(cyan: CGFloat, magenta: CGFloat, yellow: CGFloat, black: CGFloat, alpha: CGFloat)](./setfillcolor%28cyan,magenta,yellow,black,alpha%29.md)
  Sets the current fill color to a value in the DeviceCMYK color space.
- [func setFillColor(gray: CGFloat, alpha: CGFloat)](./setfillcolor%28gray,alpha%29.md)
  Sets the current fill color to a value in the DeviceGray color space.
- [func setFillColor(red: CGFloat, green: CGFloat, blue: CGFloat, alpha: CGFloat)](./setfillcolor%28red,green,blue,alpha%29.md)
  Sets the current fill color to a value in the DeviceRGB color space.
- [func setFillColorSpace(CGColorSpace)](./setfillcolorspace%28_%29.md)
  Sets the fill color space in a graphics context.
- [func setShadow(offset: CGSize, blur: CGFloat)](./setshadow%28offset,blur%29.md)
  Enables shadowing in a graphics context.
- [func setShadow(offset: CGSize, blur: CGFloat, color: CGColor?)](./setshadow%28offset,blur,color%29.md)
  Enables shadowing with color a graphics context.
- [func setStrokeColor(CGColor)](./setstrokecolor%28_%29-1sskg.md)
  Sets the current stroke color in a context, using a CGColor.
- [func setStrokeColor(UnsafePointer<CGFloat>)](./setstrokecolor%28_%29-4pd8p.md)
  Sets the current stroke color.
- [func setStrokeColor(cyan: CGFloat, magenta: CGFloat, yellow: CGFloat, black: CGFloat, alpha: CGFloat)](./setstrokecolor%28cyan,magenta,yellow,black,alpha%29.md)
  Sets the current stroke color to a value in the DeviceCMYK color space.
- [func setStrokeColor(gray: CGFloat, alpha: CGFloat)](./setstrokecolor%28gray,alpha%29.md)
  Sets the current stroke color to a value in the DeviceGray color space.
- [func setStrokeColorSpace(CGColorSpace)](./setstrokecolorspace%28_%29.md)
  Sets the stroke color space in a graphics context.
- [func setStrokePattern(CGPattern, colorComponents: UnsafePointer<CGFloat>)](./setstrokepattern%28_,colorcomponents%29.md)
  Sets the stroke pattern in the specified graphics context.
- [func setAlpha(CGFloat)](./setalpha%28_%29.md)
  Sets the opacity level for objects drawn in a graphics context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgcontext/setstrokecolor(red:green:blue:alpha:))*