# usingColorSpaceName(_:device:)

**Framework**: AppKit  
**Kind**: method

Creates a new color object for the same color, but in the specified color space and specific to the provided device.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func usingColorSpaceName(_ name: NSColorSpaceName?, device deviceDescription: [NSDeviceDescriptionKey : Any]?) -> NSColor?
```

#### Return Value

The new NSColor object or `nil` if the specified conversion cannot be done.

## Parameters

- `name`: The name of the color space containing the new   object. If   is  , the most appropriate color space is used.
- `deviceDescription`: If   is  , the current device (as obtained from the currently lockFocus’ed view’s window or, if printing, the current printer) is used.

## See Also

- [var colorSpaceName: NSColorSpaceName](nscolor/colorspacename.md)
  The name of the color space associated with the color.
- [class var ignoresAlpha: Bool](nscolor/ignoresalpha.md)
  A Boolean value that indicates whether the app supports alpha.
- [var colorSpaceName: NSColorSpaceName](nscolor/colorspacename.md)
  The name of the color space associated with the color.
- [func usingColorSpaceName(NSColorSpaceName) -> NSColor?](nscolor/usingcolorspacename(_:).md)
  Creates a new color object whose color is the same as the receiver’s, except that the new color object is in the specified color space.
- [class let currentControlTintDidChangeNotification: NSNotification.Name](nscolor/currentcontroltintdidchangenotification.md)
  Sent after the user changes control tint preference.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolor/usingcolorspacename(_:device:))*