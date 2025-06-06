# colorSpace()

**Framework**: Quartz  
**Kind**: method  
**Required**: Yes

Returns the color space used by the rendering context.

**Availability**:
- macOS 10.4+

## Declaration

```swift
func colorSpace() -> Unmanaged<CGColorSpace>!
```

#### Return Value

An RGB color space; `NULL` if the custom patch execution mode is not consumer.

#### Discussion

If the method returns a color space, it must be an RGB color space.

## See Also

- [func userInfo() -> NSMutableDictionary!](qcplugincontext/userinfo.md)
  Returns a mutable dictionary that contains information that can be shared between all instances of the `QCPlugIn` subclass, running in the same Quartz Composer context.
- [func bounds() -> NSRect](qcplugincontext/bounds.md)
  Returns the bounds of the rendering context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/qcplugincontext/colorspace())*