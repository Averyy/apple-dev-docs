# shadowBlurRadius

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The blur radius of the shadow.

**Availability**:
- macOS 10.0+

## Declaration

```swift
var shadowBlurRadius: CGFloat { get set }
```

```objc
@property CGFloat shadowBlurRadius;
```

#### Discussion

This property contains the shadow’s blur radius, as measured in the default user coordinate space. A value of `0` produces no blur, while larger values produce an increasingly large blurred shadow. This value must not be negative. The default value is `0`.

## See Also

### Managing a shadow
- [var shadowOffset: CGSize](./shadowoffset.md)
  The shadow’s relative position, which you specify with horizontal and vertical offset values.
- [var shadowColor: NSColor?](./shadowcolor.md)
  The color of the shadow.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsshadow/shadowblurradius)*