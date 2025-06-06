# setFillColor(_:)

**Framework**: Core Graphics  
**Kind**: method

Sets the current fill color.

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
func setFillColor(_ components: UnsafePointer<CGFloat>)
```

#### Discussion

The current fill color space must not be a pattern color space. For information on setting the fill color when using a pattern color space, see [`setFillPattern(_:colorComponents:)`](cgcontext/setfillpattern(_:colorcomponents:).md). Note that the preferred API to use is now [`setFillColor(_:)`](cgcontext/setfillcolor(_:)-8lhn8.md).

## Parameters

- `components`: An array of intensity values describing the color to set. The number of array elements must equal the number of components in the current fill color space, plus an additional component for the alpha value.

## See Also

- [func setFillColor(CGColor)](cgcontext/setfillcolor(_:)-8lhn8.md)
  Sets the current fill color in a graphics context, using a CGColor.
- [func setFillColor(cyan: CGFloat, magenta: CGFloat, yellow: CGFloat, black: CGFloat, alpha: CGFloat)](cgcontext/setfillcolor(cyan:magenta:yellow:black:alpha:).md)
  Sets the current fill color to a value in the DeviceCMYK color space.
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

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgcontext/setfillcolor(_:)-756dy)*