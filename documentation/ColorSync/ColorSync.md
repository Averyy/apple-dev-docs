# ColorSync

**Framework**: ColorSync  
**Kind**: module

Reproduce colors accurately across a range of input, output, and display devices.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

#### Overview

ColorSync is the color-management engine on Apple platforms. For most apps, color management happens automatically through higher-level frameworks such as [`Core Graphics`](https://developer.apple.com/documentation/coregraphics) and [`Core Image`](https://developer.apple.com/documentation/coreimage). Use ColorSync directly when your app needs to manage color itself; for example, a professional photo, print, or video app that builds custom transforms, or a tool that inspects and calibrates the profiles assigned to devices and displays.

> **Note**: To pass a profile to Core Graphics, create a [`CGColorSpace`](https://developer.apple.com/documentation/coregraphics/cgcolorspace) from a [`ColorSyncProfile`](colorsyncprofile.md) with [`CGColorSpaceCreateWithColorSyncProfile(_:_:)`](https://developer.apple.com/documentation/coregraphics/cgcolorspacecreatewithcolorsyncprofile(_:_:)).

A [`ColorSyncProfile`](colorsyncprofile.md) describes the color behavior of a device or a working color space, and a [`ColorSyncTransform`](colorsynctransform.md) converts color from one profile to another. Use ColorSync to match color across color spaces and to read, author, and embed the International Color Consortium (ICC) profiles that describe them. You can also create Headroom Adaptive Gain Curve (HAGC) metadata, which controls how the system adapts HDR content when a display can’t show its full brightness range.

## Topics

### Color conversion
- [Color transforms](color-transforms.md)
  Convert color from one profile’s color space to another.
- [Pixel format and data layout](pixel-format.md)
  Describe the memory layout of the pixel buffers a color transform reads and writes.
### Profile and HDR metadata
- [Color profiles](color-profiles.md)
  Work with the ICC profiles that describe device and working color spaces.
- [Headroom Adaptive Gain Curve](headroom-adaptive-gain-curve.md)
  Work with SMPTE ST 2094-50 tone-mapping metadata shared between HDR stills and video.
### System color management
- [Color devices](color-devices.md)
  Manage the color profiles assigned to displays, printers, scanners, and cameras.
- [Color management modules](color-management-modules.md)
  Work with the Color Management Modules that perform color conversions.
### Supporting types and conventions
- [Supporting types and conventions](supporting-types-and-conventions.md)
  Reference the signatures and conventions that support the color-management APIs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/ColorSync)*