# setFillColor(cyan:magenta:yellow:black:alpha:)

**Framework**: Core Graphics  
**Kind**: method

Sets the current fill color to a value in the DeviceCMYK color space.

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
func setFillColor(cyan: CGFloat, magenta: CGFloat, yellow: CGFloat, black: CGFloat, alpha: CGFloat)
```

#### Discussion

Core Graphics provides convenience functions for each of the device color spaces that allow you to set the fill or stroke color space and the fill or stroke color with one function call.

When you call this function, two things happen:

- Core Graphics sets the current fill color space to DeviceCMYK.
- Core Graphics sets the current fill color to the value specified by the `cyan`, `magenta`, `yellow`, `black`, and `alpha` parameters.

## Parameters

- `cyan`: The cyan intensity value for the color to set. The DeviceCMYK color space permits the specification of a value ranging from 0.0 (does not absorb the secondary color) to 1.0 (fully absorbs the secondary color).
- `magenta`: The magenta intensity value for the color to set. The DeviceCMYK color space permits the specification of a value ranging from 0.0 (does not absorb the secondary color) to 1.0 (fully absorbs the secondary color).
- `yellow`: The yellow intensity value for the color to set. The DeviceCMYK color space permits the specification of a value ranging from 0.0 (does not absorb the secondary color) to 1.0 (fully absorbs the secondary color).
- `black`: The black intensity value for the color to set. The DeviceCMYK color space permits the specification of a value ranging from 0.0 (does not absorb the secondary color) to 1.0 (fully absorbs the secondary color).
- `alpha`: A value that specifies the opacity level. Values can range from   (transparent) to   (opaque). Values outside this range are clipped to   or  .

## See Also

- [func setFillColor(CGColor)](cgcontext/setfillcolor(_:)-8lhn8.md)
  Sets the current fill color in a graphics context, using a CGColor.
- [func setFillColor(UnsafePointer<CGFloat>)](cgcontext/setfillcolor(_:)-756dy.md)
  Sets the current fill color.
- [func setFillColor(gray: CGFloat, alpha: CGFloat)](cgcontext/setfillcolor(gray:alpha:).md)
  Sets the current fill color to a value in the DeviceGray color space.
- [func setFillColor(red: CGFloat, green: CGFloat, blue: CGFloat, alpha: CGFloat)](cgcontext/setfillcolor(red:green:blue:alpha:).md)
  Sets the current fill color to a value in the DeviceRGB color space.
- [func setFillColorSpace(CGColorSpace)](cgcontext/setfillcolorspace(_:).md)
  Sets the fill color space in a graphics context.
- [func setShadow(offset: CGSize, blur: CGFloat)](cgcontext/setshadow(offset:blur:).md)
  Enables shadowing in a graphics context.
- [func setShadow(offset: CGSize, blur: CGFloat, color: CGColor?)](cgcontext/setshadow(offset:blur:color:).md)
  Enables shadowing with color a graphics context.
- [func setStrokeColor(CGColor)](cgcontext/setstrokecolor(_:)-1sskg.md)
  Sets the current stroke color in a context, using a CGColor.
- [func setStrokeColor(UnsafePointer<CGFloat>)](cgcontext/setstrokecolor(_:)-4pd8p.md)
  Sets the current stroke color.
- [func setStrokeColor(cyan: CGFloat, magenta: CGFloat, yellow: CGFloat, black: CGFloat, alpha: CGFloat)](cgcontext/setstrokecolor(cyan:magenta:yellow:black:alpha:).md)
  Sets the current stroke color to a value in the DeviceCMYK color space.
- [func setStrokeColor(gray: CGFloat, alpha: CGFloat)](cgcontext/setstrokecolor(gray:alpha:).md)
  Sets the current stroke color to a value in the DeviceGray color space.
- [func setStrokeColor(red: CGFloat, green: CGFloat, blue: CGFloat, alpha: CGFloat)](cgcontext/setstrokecolor(red:green:blue:alpha:).md)
  Sets the current stroke color to a value in the DeviceRGB color space.
- [func setStrokeColorSpace(CGColorSpace)](cgcontext/setstrokecolorspace(_:).md)
  Sets the stroke color space in a graphics context.
- [func setStrokePattern(CGPattern, colorComponents: UnsafePointer<CGFloat>)](cgcontext/setstrokepattern(_:colorcomponents:).md)
  Sets the stroke pattern in the specified graphics context.
- [func setAlpha(CGFloat)](cgcontext/setalpha(_:).md)
  Sets the opacity level for objects drawn in a graphics context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgcontext/setfillcolor(cyan:magenta:yellow:black:alpha:))*