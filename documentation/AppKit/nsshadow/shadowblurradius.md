# shadowBlurRadius

**Framework**: AppKit  
**Kind**: property

The blur radius of the shadow.

**Availability**:
- macOS 10.0+

## Declaration

```swift
var shadowBlurRadius: CGFloat { get set }
```

#### Discussion

This property contains the shadow’s blur radius, as measured in the default user coordinate space. A value of `0` produces no blur, while larger values produce an increasingly large blurred shadow. This value must not be negative. The default value is `0`.

## See Also

- [var shadowOffset: NSSize](nsshadow/shadowoffset.md)
  The shadow’s relative position, which you specify with horizontal and vertical offset values.
- [var shadowColor: NSColor?](nsshadow/shadowcolor.md)
  The color of the shadow.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsshadow/shadowblurradius)*