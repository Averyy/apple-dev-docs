# colorSpaceName

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The name of the color space associated with the color.

**Availability**:
- macOS 10.0+ - Deprecated in 10.14

> **Deprecated**: Use -type and NSColorType instead

## Declaration

```swift
var colorSpaceName: NSColorSpaceName { get }
```

```objc
@property (copy, readonly) NSColorSpaceName colorSpaceName;
```

## See Also

### Related Documentation
- [func usingColorSpaceName(NSColorSpaceName) -> NSColor?](./usingcolorspacename%28_%29.md)
  Creates a new color object whose color is the same as the receiver’s, except that the new color object is in the specified color space.
- [func usingColorSpaceName(NSColorSpaceName?, device: [NSDeviceDescriptionKey : Any]?) -> NSColor?](./usingcolorspacename%28_,device%29.md)
  Creates a new color object for the same color, but in the specified color space and specific to the provided device.
### Deprecated properties
- [class var ignoresAlpha: Bool](./ignoresalpha.md)
  A Boolean value that indicates whether the app supports alpha.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolor/colorspacename)*