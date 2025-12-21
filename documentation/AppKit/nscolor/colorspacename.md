# colorSpaceName

**Framework**: AppKit  
**Kind**: property

The name of the color space associated with the color.

**Availability**:
- macOS 10.0+

## Declaration

```swift
var colorSpaceName: NSColorSpaceName { get }
```

## See Also

- [func usingColorSpaceName(NSColorSpaceName) -> NSColor?](nscolor/usingcolorspacename(_:).md)
  Creates a new color object whose color is the same as the receiver’s, except that the new color object is in the specified color space.
- [func usingColorSpaceName(NSColorSpaceName?, device: [NSDeviceDescriptionKey : Any]?) -> NSColor?](nscolor/usingcolorspacename(_:device:).md)
  Creates a new color object for the same color, but in the specified color space and specific to the provided device.
- [class var ignoresAlpha: Bool](nscolor/ignoresalpha.md)
  A Boolean value that indicates whether the app supports alpha.
- [func usingColorSpaceName(NSColorSpaceName) -> NSColor?](nscolor/usingcolorspacename(_:).md)
  Creates a new color object whose color is the same as the receiver’s, except that the new color object is in the specified color space.
- [func usingColorSpaceName(NSColorSpaceName?, device: [NSDeviceDescriptionKey : Any]?) -> NSColor?](nscolor/usingcolorspacename(_:device:).md)
  Creates a new color object for the same color, but in the specified color space and specific to the provided device.
- [class let currentControlTintDidChangeNotification: NSNotification.Name](nscolor/currentcontroltintdidchangenotification.md)
  Sent after the user changes control tint preference.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolor/colorspacename)*