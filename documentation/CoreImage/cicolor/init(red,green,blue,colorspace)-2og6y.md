# init(red:green:blue:colorSpace:)

**Framework**: Core Image  
**Kind**: init  
**Role**: Initializer

Create a Core Image color object with the specified red, green, and blue component values as measured in the specified color space.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 10.0+
- visionOS 1.0+

## Declaration

```swift
convenience init?(red: CGFloat, green: CGFloat, blue: CGFloat, colorSpace: CGColorSpace)
```

```objc
+ (instancetype) colorWithRed:(CGFloat) red green:(CGFloat) green blue:(CGFloat) blue colorSpace:(CGColorSpaceRef) colorSpace;
```

## Return Value

 An autoreleased [`CIColor`](../cicolor.md) instance.

## Discussion

This will return `null` if the `CGColorSpace` is not `kCGColorSpaceModelRGB`.

The RGB values can be outside the `0...1` range if the `CGColorSpace` is unclamped.

## Parameters

- `red`: The color’s unpremultiplied red component value.
- `green`: The color’s unpremultiplied green component value.
- `blue`: The color’s unpremultiplied blue component value.
- `colorSpace`: The color’s `CGColorSpace` which must have `kCGColorSpaceModelRGB`.

## See Also

### Creating Color Objects
- [convenience init(red: CGFloat, green: CGFloat, blue: CGFloat)](./init%28red,green,blue%29.md)
  Create a Core Image color object in the sRGB color space with the specified red, green, and blue component values.
- [convenience init(string: String)](./init%28string%29.md)
  Create a Core Image color object in the sRGB color space using a string containing the RGBA color component values.
- [convenience init?(red: CGFloat, green: CGFloat, blue: CGFloat, alpha: CGFloat, colorSpace: CGColorSpace)](./init%28red,green,blue,alpha,colorspace%29-5mvff.md)
  Create a Core Image color object with the specified red, green, blue, and alpha component values as measured in the specified color space.
- [+ colorWithCGColor:](./colorwithcgcolor_.md)
  Create a Core Image color object with a Core Graphics color object.
- [+ colorWithRed:green:blue:alpha:](./colorwithred_green_blue_alpha_.md)
  Create a Core Image color object in the sRGB color space with the specified red, green, blue, and alpha component values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cicolor/init(red:green:blue:colorspace:)-2og6y)*