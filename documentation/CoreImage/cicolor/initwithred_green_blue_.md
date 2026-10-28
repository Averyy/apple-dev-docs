# initWithRed:green:blue:

**Framework**: Core Image  
**Kind**: method  
**Role**: Instance Method

Initialize a Core Image color object in the sRGB color space with the specified red, green, and blue component values.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```objc
- (instancetype) initWithRed:(CGFloat) red green:(CGFloat) green blue:(CGFloat) blue;
```

## Return Value

 An initialized [`CIColor`](../cicolor.md) instance.

## Discussion

On macOS before 10.10, the CIColor’s color space will be Generic RGB.

## Parameters

- `red`: The color’s unpremultiplied red component value between 0 and 1.
- `green`: The color’s unpremultiplied green component value between 0 and 1.
- `blue`: The color’s unpremultiplied blue component value between 0 and 1.

## See Also

### Initializing Color Objects
- [init(cgColor: CGColor)](./init%28cgcolor%29-1hzk4.md)
  Create a Core Image color object with a Core Graphics color object.
- [convenience init(color: UIColor)](./init%28color%29.md)
- [convenience init(red: CGFloat, green: CGFloat, blue: CGFloat, alpha: CGFloat)](./init%28red,green,blue,alpha%29.md)
  Initialize a Core Image color object in the sRGB color space with the specified red, green, blue, and alpha component values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cicolor/initwithred:green:blue:)*