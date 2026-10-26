# colorWithRed:green:blue:alpha:

**Framework**: Core Image  
**Kind**: method  
**Role**: Type Method

Create a Core Image color object in the sRGB color space with the specified red, green, blue, and alpha component values.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS
- visionOS 1.0+

## Declaration

```objc
+ (instancetype) colorWithRed:(CGFloat) red green:(CGFloat) green blue:(CGFloat) blue alpha:(CGFloat) alpha;
```

#### Return Value

 An autoreleased [`CIColor`](../cicolor.md) instance.

#### Discussion

On macOS before 10.10, the CIColor’s color space will be Generic RGB.

## Parameters

- `red`: The color’s unpremultiplied red component value between 0 and 1.
- `green`: The color’s unpremultiplied green component value between 0 and 1.
- `blue`: The color’s unpremultiplied blue component value between 0 and 1.
- `alpha`: The color’s alpha (opacity) value between 0 and 1.

## See Also

### Creating Color Objects
- [+ colorWithCGColor:](./colorwithcgcolor_.md)
  Create a Core Image color object with a Core Graphics color object.
- [convenience init(red: CGFloat, green: CGFloat, blue: CGFloat)](./init%28red,green,blue%29.md)
  Create a Core Image color object in the sRGB color space with the specified red, green, and blue component values.
- [convenience init(string: String)](./init%28string%29.md)
  Create a Core Image color object in the sRGB color space using a string containing the RGBA color component values.
- [convenience init?(red: CGFloat, green: CGFloat, blue: CGFloat, colorSpace: CGColorSpace)](./init%28red,green,blue,colorspace%29-2og6y.md)
  Create a Core Image color object with the specified red, green, and blue component values as measured in the specified color space.
- [convenience init?(red: CGFloat, green: CGFloat, blue: CGFloat, alpha: CGFloat, colorSpace: CGColorSpace)](./init%28red,green,blue,alpha,colorspace%29-5mvff.md)
  Create a Core Image color object with the specified red, green, blue, and alpha component values as measured in the specified color space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cicolor/colorwithred:green:blue:alpha:)*