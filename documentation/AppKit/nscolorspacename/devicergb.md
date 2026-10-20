# deviceRGB

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

Device-dependent color space with red, green, blue, and alpha components.

**Availability**:
- macOS

## Declaration

```swift
static let deviceRGB: NSColorSpaceName
```

```c
extern NSColorSpaceName NSDeviceRGBColorSpace;
```

#### Discussion

You can also create a color with HSB (hue, saturation, brightness) and alpha components and can extract these components.

## See Also

### Color Space Names
- [static let calibratedRGB: NSColorSpaceName](./calibratedrgb.md)
  Calibrated color space with red, green, blue, and alpha components.
- [static let calibratedWhite: NSColorSpaceName](./calibratedwhite.md)
  Calibrated color space with white and alpha components (pure white is 1.0)
- [static let custom: NSColorSpaceName](./custom.md)
  Custom `NSColorSpace` object and floating-point components describing a color in that space
- [static let deviceCMYK: NSColorSpaceName](./devicecmyk.md)
  Device-dependent color space with cyan, magenta, yellow, black, and alpha components
- [static let deviceWhite: NSColorSpaceName](./devicewhite.md)
  Device-dependent color space with white and alpha components (pure white is 1.0)
- [static let named: NSColorSpaceName](./named.md)
  Catalog name and color name components
- [static let pattern: NSColorSpaceName](./pattern.md)
  Pattern image (tiled)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolorspacename/devicergb)*