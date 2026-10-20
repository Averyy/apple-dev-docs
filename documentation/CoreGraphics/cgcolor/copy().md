# copy()

**Framework**: Core Graphics  
**Kind**: method  
**Role**: Instance Method

Creates a copy of an existing color.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.3+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func copy() -> CGColor?
```

```c
extern CGColorRefCGColorCreateCopy(CGColorRef color);
```

#### Return Value

A copy of the specified color. In Objective-C, you’re responsible for releasing this object using [`CGColorRelease`](../cgcolorrelease.md).

## See Also

### Creating Colors
- [func copy(alpha: CGFloat) -> CGColor?](./copy%28alpha%29.md)
  Creates a copy of an existing color, substituting a new alpha value.
- [init(genericCMYKCyan: CGFloat, magenta: CGFloat, yellow: CGFloat, black: CGFloat, alpha: CGFloat)](./init%28genericcmykcyan,magenta,yellow,black,alpha%29.md)
  Creates a color in the Generic CMYK color space.
- [init(gray: CGFloat, alpha: CGFloat)](./init%28gray,alpha%29.md)
  Creates a color in the Generic gray color space.
- [init(genericGrayGamma2_2Gray: CGFloat, alpha: CGFloat)](./init%28genericgraygamma2_2gray,alpha%29.md)
  Creates a color in the Generic gray color space with a gamma ramp of 2.2.
- [init(red: CGFloat, green: CGFloat, blue: CGFloat, alpha: CGFloat)](./init%28red,green,blue,alpha%29.md)
  Creates a color in the Generic RGB color space.
- [init(srgbRed: CGFloat, green: CGFloat, blue: CGFloat, alpha: CGFloat)](./init%28srgbred,green,blue,alpha%29.md)
  Creates a color in the sRGB color space.
- [init?(colorSpace: CGColorSpace, components: UnsafePointer<CGFloat>)](./init%28colorspace,components%29.md)
  Creates a color using a list of intensity values (including alpha) and an associated color space.
- [init?(patternSpace: CGColorSpace, pattern: CGPattern, components: UnsafePointer<CGFloat>)](./init%28patternspace,pattern,components%29.md)
  Creates a color using a list of intensity values (including alpha), a pattern color space, and a pattern.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgcolor/copy())*