# init(red:green:blue:alpha:colorSpace:)

**Framework**: Core Image  
**Kind**: init

Create a Core Image color object with the specified red, green, blue, and alpha component values as measured in the specified color space.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- visionOS 1.0+

## Declaration

```swift
convenience init?(red: CGFloat, green: CGFloat, blue: CGFloat, alpha: CGFloat, colorSpace: CGColorSpace)
```

#### Return Value

 An autoreleased [`CIColor`](cicolor.md) instance.

#### Discussion

This will return `null` if the `CGColorSpace` is not `kCGColorSpaceModelRGB`.

The RGB values can be outside the `0...1` range if the `CGColorSpace` is unclamped.

## Parameters

- `red`: The color’s unpremultiplied red component value.
- `green`: The color’s unpremultiplied green component value.
- `blue`: The color’s unpremultiplied blue component value.
- `alpha`: The color’s alpha (opacity) value between 0 and 1.
- `colorSpace`: The color’s `CGColorSpace` which must have `kCGColorSpaceModelRGB`.

## See Also

- [convenience init(red: CGFloat, green: CGFloat, blue: CGFloat)](cicolor/init(red:green:blue:).md)
  Create a Core Image color object in the sRGB color space with the specified red, green, and blue component values.
- [convenience init(string: String)](cicolor/init(string:).md)
  Create a Core Image color object in the sRGB color space using a string containing the RGBA color component values.
- [convenience init?(red: CGFloat, green: CGFloat, blue: CGFloat, colorSpace: CGColorSpace)](cicolor/init(red:green:blue:colorspace:)-2og6y.md)
  Create a Core Image color object with the specified red, green, and blue component values as measured in the specified color space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cicolor/init(red:green:blue:alpha:colorspace:)-5mvff)*