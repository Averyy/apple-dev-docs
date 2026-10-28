# setStrokeColorSpace(_:)

**Framework**: Core Graphics  
**Kind**: method  
**Role**: Instance Method

Sets the stroke color space in a graphics context.

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
func setStrokeColorSpace(_ space: CGColorSpace)
```

```c
extern void CGContextSetStrokeColorSpace(CGContextRef c, CGColorSpaceRef space);
```

## Discussion

As a side effect when you call this function, Core Graphics assigns an appropriate initial value to the stroke color, based on the color space you specify. To change this value, call [`setStrokeColor(_:)`](./setstrokecolor%28_%29-4pd8p.md). Note that the preferred API is now [`setStrokeColor(_:)`](./setstrokecolor%28_%29-1sskg.md).

## Parameters

- `space`: The new stroke color space. The color space is retained; upon return, you may safely release it.

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
- [func setStrokeColor(red: CGFloat, green: CGFloat, blue: CGFloat, alpha: CGFloat)](./setstrokecolor%28red,green,blue,alpha%29.md)
  Sets the current stroke color to a value in the DeviceRGB color space.
- [func setStrokePattern(CGPattern, colorComponents: UnsafePointer<CGFloat>)](./setstrokepattern%28_,colorcomponents%29.md)
  Sets the stroke pattern in the specified graphics context.
- [func setAlpha(CGFloat)](./setalpha%28_%29.md)
  Sets the opacity level for objects drawn in a graphics context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgcontext/setstrokecolorspace(_:))*