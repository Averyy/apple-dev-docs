# NSColorSpaceName

**Framework**: AppKit  
**Kind**: struct

Constants that specify color space names.

**Availability**:
- macOS ?+

## Declaration

```swift
struct NSColorSpaceName
```

## Topics

### Color Space Names
- [static let calibratedRGB: NSColorSpaceName](nscolorspacename/calibratedrgb.md)
  Calibrated color space with red, green, blue, and alpha components.
- [static let calibratedWhite: NSColorSpaceName](nscolorspacename/calibratedwhite.md)
  Calibrated color space with white and alpha components (pure white is 1.0)
- [static let custom: NSColorSpaceName](nscolorspacename/custom.md)
  Custom `NSColorSpace` object and floating-point components describing a color in that space
- [static let deviceCMYK: NSColorSpaceName](nscolorspacename/devicecmyk.md)
  Device-dependent color space with cyan, magenta, yellow, black, and alpha components
- [static let deviceRGB: NSColorSpaceName](nscolorspacename/devicergb.md)
  Device-dependent color space with red, green, blue, and alpha components.
- [static let deviceWhite: NSColorSpaceName](nscolorspacename/devicewhite.md)
  Device-dependent color space with white and alpha components (pure white is 1.0)
- [static let named: NSColorSpaceName](nscolorspacename/named.md)
  Catalog name and color name components
- [static let pattern: NSColorSpaceName](nscolorspacename/pattern.md)
  Pattern image (tiled)
### Getting the Number of Components
- [var numberOfColorComponents: Int](nscolorspacename/numberofcolorcomponents.md)
  Returns the number of color components in the specified color space.
### Initializers
- [init(rawValue: String)](nscolorspacename/init(rawvalue:).md)
  Creates a new instance with the specified raw value.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var type: NSColor.ColorType](nscolor/type.md)
  The type of the color object.
- [func usingType(NSColor.ColorType) -> NSColor?](nscolor/usingtype(_:).md)
  Returns a version of the color object that is compatible with the specified color type.
- [NSColor.ColorType](nscolor/colortype.md)
  Constants that indicate the color’s type, and which methods may be called on the color object.
- [var colorSpace: NSColorSpace](nscolor/colorspace.md)
  The color space associated with the color.
- [var colorSpaceName: NSColorSpaceName](nscolor/colorspacename.md)
  The name of the color space associated with the color.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolorspacename)*