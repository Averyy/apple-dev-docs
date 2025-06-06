# bounds()

**Framework**: Quartz  
**Kind**: method  
**Required**: Yes

Returns the bounds of the rendering context.

**Availability**:
- macOS 10.4+

## Declaration

```swift
func bounds() -> NSRect
```

#### Return Value

The bounds of the rendering context expressed in Quartz Composer units.

## See Also

- [func userInfo() -> NSMutableDictionary!](qcplugincontext/userinfo.md)
  Returns a mutable dictionary that contains information that can be shared between all instances of the `QCPlugIn` subclass, running in the same Quartz Composer context.
- [func colorSpace() -> Unmanaged<CGColorSpace>!](qcplugincontext/colorspace.md)
  Returns the color space used by the rendering context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/qcplugincontext/bounds())*