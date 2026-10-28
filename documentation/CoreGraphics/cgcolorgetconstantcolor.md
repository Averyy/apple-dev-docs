# CGColorGetConstantColor

**Framework**: Core Graphics  
**Kind**: func  
**Role**: Function

Returns a color object that represents a constant color.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 10.5+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```c
extern CGColorRefCGColorGetConstantColor(CFStringRef colorName);
```

## Return Value

A color object.

## Discussion

As this function is not a “Copy” or “Create” function, it does not necessarily return a new reference each time it’s called. As a consequence, you should not release the returned value. However, colors returned from this function can be retained and released in a properly nested fashion, just as any other Core Foundation type can.

## Parameters

- `colorName`: A color name. You can pass any of constants in [Getting System Colors](./cgcolor.md#Getting-System-Colors).

## See Also

### Creating Colors
- [func copy() -> CGColor?](./cgcolor/copy%28%29.md)
  Creates a copy of an existing color.
- [func copy(alpha: CGFloat) -> CGColor?](./cgcolor/copy%28alpha%29.md)
  Creates a copy of an existing color, substituting a new alpha value.
- [init(genericCMYKCyan: CGFloat, magenta: CGFloat, yellow: CGFloat, black: CGFloat, alpha: CGFloat)](./cgcolor/init%28genericcmykcyan,magenta,yellow,black,alpha%29.md)
  Creates a color in the Generic CMYK color space.
- [init(gray: CGFloat, alpha: CGFloat)](./cgcolor/init%28gray,alpha%29.md)
  Creates a color in the Generic gray color space.
- [init(genericGrayGamma2_2Gray: CGFloat, alpha: CGFloat)](./cgcolor/init%28genericgraygamma2_2gray,alpha%29.md)
  Creates a color in the Generic gray color space with a gamma ramp of 2.2.
- [init(red: CGFloat, green: CGFloat, blue: CGFloat, alpha: CGFloat)](./cgcolor/init%28red,green,blue,alpha%29.md)
  Creates a color in the Generic RGB color space.
- [init(srgbRed: CGFloat, green: CGFloat, blue: CGFloat, alpha: CGFloat)](./cgcolor/init%28srgbred,green,blue,alpha%29.md)
  Creates a color in the sRGB color space.
- [init?(colorSpace: CGColorSpace, components: UnsafePointer<CGFloat>)](./cgcolor/init%28colorspace,components%29.md)
  Creates a color using a list of intensity values (including alpha) and an associated color space.
- [init?(patternSpace: CGColorSpace, pattern: CGPattern, components: UnsafePointer<CGFloat>)](./cgcolor/init%28patternspace,pattern,components%29.md)
  Creates a color using a list of intensity values (including alpha), a pattern color space, and a pattern.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgcolorgetconstantcolor)*