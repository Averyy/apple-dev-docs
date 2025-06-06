# init(genericCMYKCyan:magenta:yellow:black:alpha:)

**Framework**: Core Graphics  
**Kind**: init

Creates a color in the Generic CMYK color space.

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
init(genericCMYKCyan cyan: CGFloat, magenta: CGFloat, yellow: CGFloat, black: CGFloat, alpha: CGFloat)
```

#### Return Value

A color object.

## Parameters

- `cyan`: A cyan value (  -  ).
- `magenta`: A magenta value (  -  ).
- `yellow`: A yellow value (  -  ).
- `black`: A black value (  -  ).
- `alpha`: An alpha value  .

## See Also

- [func copy() -> CGColor?](cgcolor/copy.md)
  Creates a copy of an existing color.
- [func copy(alpha: CGFloat) -> CGColor?](cgcolor/copy(alpha:).md)
  Creates a copy of an existing color, substituting a new alpha value.
- [init(gray: CGFloat, alpha: CGFloat)](cgcolor/init(gray:alpha:).md)
  Creates a color in the Generic gray color space.
- [init(genericGrayGamma2_2Gray: CGFloat, alpha: CGFloat)](cgcolor/init(genericgraygamma2_2gray:alpha:).md)
  Creates a color in the Generic gray color space with a gamma ramp of 2.2.
- [init(red: CGFloat, green: CGFloat, blue: CGFloat, alpha: CGFloat)](cgcolor/init(red:green:blue:alpha:).md)
  Creates a color in the Generic RGB color space.
- [init(srgbRed: CGFloat, green: CGFloat, blue: CGFloat, alpha: CGFloat)](cgcolor/init(srgbred:green:blue:alpha:).md)
  Creates a color in the sRGB color space.
- [init?(colorSpace: CGColorSpace, components: UnsafePointer<CGFloat>)](cgcolor/init(colorspace:components:).md)
  Creates a color using a list of intensity values (including alpha) and an associated color space.
- [init?(patternSpace: CGColorSpace, pattern: CGPattern, components: UnsafePointer<CGFloat>)](cgcolor/init(patternspace:pattern:components:).md)
  Creates a color using a list of intensity values (including alpha), a pattern color space, and a pattern.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgcolor/init(genericcmykcyan:magenta:yellow:black:alpha:))*