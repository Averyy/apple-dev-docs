# shadowColor

**Framework**: UIKit  
**Kind**: property

The color of the shadow.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var shadowColor: Any? { get set }
```

#### Discussion

The default shadow color is black with an alpha of 1/3. If you set this property to `nil`, the shadow is not drawn. The color you specify must be convertible to an RGBA color and may contain alpha information.

## See Also

- [var shadowOffset: CGSize](nsshadow/shadowoffset.md)
  The shadow’s relative position, which you specify with horizontal and vertical offset values.
- [var shadowBlurRadius: CGFloat](nsshadow/shadowblurradius.md)
  The blur radius of the shadow.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nsshadow/shadowcolor)*