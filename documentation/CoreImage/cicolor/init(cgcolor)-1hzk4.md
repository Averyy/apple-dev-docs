# init(cgColor:)

**Framework**: Core Image  
**Kind**: init  
**Role**: Initializer

Create a Core Image color object with a Core Graphics color object.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS
- visionOS 1.0+

## Declaration

```swift
init(cgColor color: CGColor)
```

```objc
- (instancetype) initWithCGColor:(CGColorRef) color;
```

#### Return Value

 An initialized [`CIColor`](../cicolor.md) instance.

## See Also

### Initializing Color Objects
- [convenience init(color: UIColor)](./init%28color%29.md)
- [convenience init(red: CGFloat, green: CGFloat, blue: CGFloat, alpha: CGFloat)](./init%28red,green,blue,alpha%29.md)
  Initialize a Core Image color object in the sRGB color space with the specified red, green, blue, and alpha component values.
- [- initWithRed:green:blue:](./initwithred_green_blue_.md)
  Initialize a Core Image color object in the sRGB color space with the specified red, green, and blue component values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cicolor/init(cgcolor:)-1hzk4)*