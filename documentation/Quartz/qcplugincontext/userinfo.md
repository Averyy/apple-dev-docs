# userInfo()

**Framework**: Quartz  
**Kind**: method  
**Required**: Yes

Returns a mutable dictionary that contains information that can be shared between all instances of the `QCPlugIn` subclass, running in the same Quartz Composer context.

**Availability**:
- macOS 10.4+

## Declaration

```swift
func userInfo() -> NSMutableDictionary!
```

#### Return Value

A mutable dictionary.

#### Discussion

When you add information to the dictionary, make sure that you use unique keys, such as `com.myCompany.foo`. You can use this dictionary to cache data that you want to share.

## See Also

- [func bounds() -> NSRect](qcplugincontext/bounds.md)
  Returns the bounds of the rendering context.
- [func colorSpace() -> Unmanaged<CGColorSpace>!](qcplugincontext/colorspace.md)
  Returns the color space used by the rendering context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/qcplugincontext/userinfo())*