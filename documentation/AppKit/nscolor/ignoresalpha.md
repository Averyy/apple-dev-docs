# ignoresAlpha

**Framework**: AppKit  
**Kind**: property

A Boolean value that indicates whether the app supports alpha.

**Availability**:
- macOS 10.0+

## Declaration

```swift
@MainActor
class var ignoresAlpha: Bool { get set }
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if the app doesn’t support alpha; otherwise, [`false`](https://developer.apple.com/documentation/Swift/false).

#### Discussion

The system consults this global value when the app imports alpha (for instance, through color dragging). By default this property is [`false`](https://developer.apple.com/documentation/Swift/false); meaning the system supports the alpha component for colors globally. To ignore alpha for an app, invoke the `setIgnoresAlpha` method with a parameter of [`true`](https://developer.apple.com/documentation/Swift/true). This value also determines whether the color panel has an opacity slider.

This method provides a global approach for removing alpha, which might not always be appropriate. Apps that need to disable alpha can use more fine-grained APIs for individual controls, such as [`showsAlpha`](nscolorpanel/showsalpha.md) and [`supportsAlpha`](nscolorwell/supportsalpha.md).

In macOS 13 and earlier, the default value is [`true`](https://developer.apple.com/documentation/Swift/true). This property is deprecated as of macOS 14.

## See Also

- [var alphaComponent: CGFloat](nscolor/alphacomponent.md)
  The alpha (opacity) component value of the color.
- [var colorSpaceName: NSColorSpaceName](nscolor/colorspacename.md)
  The name of the color space associated with the color.
- [func usingColorSpaceName(NSColorSpaceName) -> NSColor?](nscolor/usingcolorspacename(_:).md)
  Creates a new color object whose color is the same as the receiver’s, except that the new color object is in the specified color space.
- [func usingColorSpaceName(NSColorSpaceName?, device: [NSDeviceDescriptionKey : Any]?) -> NSColor?](nscolor/usingcolorspacename(_:device:).md)
  Creates a new color object for the same color, but in the specified color space and specific to the provided device.
- [class let currentControlTintDidChangeNotification: NSNotification.Name](nscolor/currentcontroltintdidchangenotification.md)
  Sent after the user changes control tint preference.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolor/ignoresalpha)*