# init(red:green:blue:alpha:)

**Framework**: Core Image  
**Kind**: init

Initialize a Core Image color object in the sRGB color space with the specified red, green, blue, and alpha component values.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
convenience init(red: CGFloat, green: CGFloat, blue: CGFloat, alpha: CGFloat)
```

#### Return Value

 An initialized [`CIColor`](cicolor.md) instance.

#### Discussion

On macOS before 10.10, the CIColor’s color space will be Generic RGB.

## Parameters

- `red`: The color’s unpremultiplied red component value between 0 and 1.
- `green`: The color’s unpremultiplied green component value between 0 and 1.
- `blue`: The color’s unpremultiplied blue component value between 0 and 1.
- `alpha`: The color’s alpha (opacity) value between 0 and 1.

## See Also

- [init(cgColor: CGColor)](cicolor/init(cgcolor:)-1hzk4.md)
  Create a Core Image color object with a Core Graphics color object.
- [convenience init(color: UIColor)](cicolor/init(color:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cicolor/init(red:green:blue:alpha:))*