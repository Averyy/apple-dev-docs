# init(red:green:blue:alpha:colorSpace:)

**Framework**: Core Image  
**Kind**: init

Initialize a Core Image color object with the specified red, green, and blue component values as measured in the specified color space.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
convenience init?(red: CGFloat, green: CGFloat, blue: CGFloat, alpha: CGFloat, colorSpace: CGColorSpace)
```

#### Return Value

 An initialized [`CIColor`](cicolor.md) instance.

#### Discussion

This will return null if the `CGColorSpace` is not `kCGColorSpaceModelRGB`. The RGB values can be outside the `0...1` range if the `CGColorSpace` is unclamped.

## Parameters

- `red`: The color’s unpremultiplied red component value.
- `green`: The color’s unpremultiplied green component value.
- `blue`: The color’s unpremultiplied blue component value.
- `alpha`: The color’s alpha (opacity) value between 0 and 1.
- `colorSpace`: The color’s   which must have  .

## See Also

- [init(cgColor: CGColor)](cicolor/init(cgcolor:).md)
  Create a Core Image color object with a Core Graphics color object.
- [convenience init(color: UIColor)](cicolor/init(color:).md)
- [convenience init(red: CGFloat, green: CGFloat, blue: CGFloat, alpha: CGFloat)](cicolor/init(red:green:blue:alpha:).md)
  Initialize a Core Image color object in the sRGB color space with the specified red, green, blue, and alpha component values.
- [convenience init?(red: CGFloat, green: CGFloat, blue: CGFloat, colorSpace: CGColorSpace)](cicolor/init(red:green:blue:colorspace:).md)
  Initialize a Core Image color object with the specified red, green, and blue component values as measured in the specified color space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cicolor/init(red:green:blue:alpha:colorspace:))*