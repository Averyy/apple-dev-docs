# setShadow(offset:blur:)

**Framework**: Core Graphics  
**Kind**: method

Enables shadowing in a graphics context.

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
func setShadow(offset: CGSize, blur: CGFloat)
```

#### Discussion

Shadow parameters are part of the graphics state in a context. After shadowing is set, all objects drawn are shadowed using a black color with 1/3 alpha (in effect, RGBA = `{0, 0, 0, 1.0/3.0}`) in the DeviceRGB color space.

To turn off shadowing:

- Use the standard save/restore mechanism for the graphics state.
- Use [`setShadow(offset:blur:color:)`](cgcontext/setshadow(offset:blur:color:).md) to set the shadow color to a fully transparent color (or pass `NULL` as the color).

## Parameters

- `offset`: Specifies a translation of the context’s coordinate system, to establish an offset for the shadow (  specifies a light source immediately above the screen).
- `blur`: A non-negative number specifying the amount of blur.

## See Also

- [func setFillColor(CGColor)](cgcontext/setfillcolor(_:)-8lhn8.md)
  Sets the current fill color in a graphics context, using a CGColor.
- [func setFillColor(UnsafePointer<CGFloat>)](cgcontext/setfillcolor(_:)-756dy.md)
  Sets the current fill color.
- [func setFillColor(cyan: CGFloat, magenta: CGFloat, yellow: CGFloat, black: CGFloat, alpha: CGFloat)](cgcontext/setfillcolor(cyan:magenta:yellow:black:alpha:).md)
  Sets the current fill color to a value in the DeviceCMYK color space.
- [func setFillColor(gray: CGFloat, alpha: CGFloat)](cgcontext/setfillcolor(gray:alpha:).md)
  Sets the current fill color to a value in the DeviceGray color space.
- [func setFillColor(red: CGFloat, green: CGFloat, blue: CGFloat, alpha: CGFloat)](cgcontext/setfillcolor(red:green:blue:alpha:).md)
  Sets the current fill color to a value in the DeviceRGB color space.
- [func setFillColorSpace(CGColorSpace)](cgcontext/setfillcolorspace(_:).md)
  Sets the fill color space in a graphics context.
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

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgcontext/setshadow(offset:blur:))*