# currentControlTintDidChangeNotification

**Framework**: AppKit  
**Kind**: property

Sent after the user changes control tint preference.

**Availability**:
- macOS 10.0+

## Declaration

```swift
class let currentControlTintDidChangeNotification: NSNotification.Name
```

#### Discussion

The notification object is `NSApp`. This notification does not contain a `userInfo` dictionary.

## See Also

- [class var ignoresAlpha: Bool](nscolor/ignoresalpha.md)
  A Boolean value that indicates whether the app supports alpha.
- [var colorSpaceName: NSColorSpaceName](nscolor/colorspacename.md)
  The name of the color space associated with the color.
- [func usingColorSpaceName(NSColorSpaceName) -> NSColor?](nscolor/usingcolorspacename(_:).md)
  Creates a new color object whose color is the same as the receiver’s, except that the new color object is in the specified color space.
- [func usingColorSpaceName(NSColorSpaceName?, device: [NSDeviceDescriptionKey : Any]?) -> NSColor?](nscolor/usingcolorspacename(_:device:).md)
  Creates a new color object for the same color, but in the specified color space and specific to the provided device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolor/currentcontroltintdidchangenotification)*