# init(color:)

**Framework**: Core Image  
**Kind**: init  
**Role**: Initializer

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS
- tvOS
- visionOS 1.0+

## Declaration

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS*

```swift
convenience init(color: UIColor)
```

*macOS*

```swift
convenience init?(color: NSColor)
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS*

```objc
- (instancetype) initWithColor:(UIColor *) color;
```

*macOS*

```objc
- (instancetype) initWithColor:(NSColor *) color;
```

## See Also

### Initializing Color Objects
- [init(cgColor: CGColor)](./init%28cgcolor%29-1hzk4.md)
  Create a Core Image color object with a Core Graphics color object.
- [convenience init(red: CGFloat, green: CGFloat, blue: CGFloat, alpha: CGFloat)](./init%28red,green,blue,alpha%29.md)
  Initialize a Core Image color object in the sRGB color space with the specified red, green, blue, and alpha component values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cicolor/init(color:))*