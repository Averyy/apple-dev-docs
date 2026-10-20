# named

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

Catalog name and color name components

**Availability**:
- macOS

## Declaration

```swift
static let named: NSColorSpaceName
```

```c
extern NSColorSpaceName NSNamedColorSpace;
```

#### Discussion

The components of this color space are indexes into lists or catalogs of prepared colors. The catalogs of named colors come with lookup tables that are able to generate the correct color on a given device.

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
- [static let deviceRGB: NSColorSpaceName](./devicergb.md)
  Device-dependent color space with red, green, blue, and alpha components.
- [static let deviceWhite: NSColorSpaceName](./devicewhite.md)
  Device-dependent color space with white and alpha components (pure white is 1.0)
- [static let pattern: NSColorSpaceName](./pattern.md)
  Pattern image (tiled)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolorspacename/named)*