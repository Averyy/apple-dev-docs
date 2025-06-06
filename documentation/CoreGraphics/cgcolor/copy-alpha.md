# copy(alpha:)

**Framework**: Core Graphics  
**Kind**: method

Creates a copy of an existing color, substituting a new alpha value.

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
func copy(alpha: CGFloat) -> CGColor?
```

#### Return Value

A copy of the specified color, using the specified alpha value. In Objective-C, you’re responsible for releasing this object using [`CGColorRelease`](cgcolorrelease.md).

## Parameters

- `alpha`: A value that specifies the desired opacity of the copy. Values outside the range   are clamped to   or  .

## See Also

- [func copy() -> CGColor?](cgcolor/copy.md)
  Creates a copy of an existing color.
- [init(genericCMYKCyan: CGFloat, magenta: CGFloat, yellow: CGFloat, black: CGFloat, alpha: CGFloat)](cgcolor/init(genericcmykcyan:magenta:yellow:black:alpha:).md)
  Creates a color in the Generic CMYK color space.
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

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgcolor/copy(alpha:))*