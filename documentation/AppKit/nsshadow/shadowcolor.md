# shadowColor

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The color of the shadow.

**Availability**:
- macOS 10.0+

## Declaration

```swift
@NSCopying
var shadowColor: NSColor? { get set }
```

```objc
@property (copy, nullable) NSColor * shadowColor;
```

## Discussion

The default shadow color is black with an alpha of 1/3. If you set this property to `nil`, the shadow is not drawn. The color you specify must be convertible to an RGBA color and may contain alpha information.

## See Also

### Managing a shadow
- [var shadowOffset: CGSize](./shadowoffset.md)
  The shadow’s relative position, which you specify with horizontal and vertical offset values.
- [var shadowBlurRadius: CGFloat](./shadowblurradius.md)
  The blur radius of the shadow.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsshadow/shadowcolor)*