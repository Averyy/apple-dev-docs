# init(red:green:blue:alpha:)

**Framework**: Core Graphics  
**Kind**: init  
**Role**: Initializer

Creates a color in the Generic RGB color space.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
init(red: CGFloat, green: CGFloat, blue: CGFloat, alpha: CGFloat)
```

```c
extern CGColorRefCGColorCreateGenericRGB(CGFloat red, CGFloat green, CGFloat blue, CGFloat alpha);
```

#### Return Value

A color object.

## Parameters

- `red`: A red component value (`0.0` - `1.0`).
- `green`: A green component value (`0.0` - `1.0`).
- `blue`: A blue component value (`0.0` - `1.0`).
- `alpha`: An alpha value (`0.0` - `1.0`).

## See Also

### Creating Colors
- [func copy() -> CGColor?](./copy%28%29.md)
  Creates a copy of an existing color.
- [func copy(alpha: CGFloat) -> CGColor?](./copy%28alpha%29.md)
  Creates a copy of an existing color, substituting a new alpha value.
- [init(genericCMYKCyan: CGFloat, magenta: CGFloat, yellow: CGFloat, black: CGFloat, alpha: CGFloat)](./init%28genericcmykcyan,magenta,yellow,black,alpha%29.md)
  Creates a color in the Generic CMYK color space.
- [init(gray: CGFloat, alpha: CGFloat)](./init%28gray,alpha%29.md)
  Creates a color in the Generic gray color space.
- [init(genericGrayGamma2_2Gray: CGFloat, alpha: CGFloat)](./init%28genericgraygamma2_2gray,alpha%29.md)
  Creates a color in the Generic gray color space with a gamma ramp of 2.2.
- [init(srgbRed: CGFloat, green: CGFloat, blue: CGFloat, alpha: CGFloat)](./init%28srgbred,green,blue,alpha%29.md)
  Creates a color in the sRGB color space.
- [init?(colorSpace: CGColorSpace, components: UnsafePointer<CGFloat>)](./init%28colorspace,components%29.md)
  Creates a color using a list of intensity values (including alpha) and an associated color space.
- [init?(patternSpace: CGColorSpace, pattern: CGPattern, components: UnsafePointer<CGFloat>)](./init%28patternspace,pattern,components%29.md)
  Creates a color using a list of intensity values (including alpha), a pattern color space, and a pattern.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgcolor/init(red:green:blue:alpha:))*