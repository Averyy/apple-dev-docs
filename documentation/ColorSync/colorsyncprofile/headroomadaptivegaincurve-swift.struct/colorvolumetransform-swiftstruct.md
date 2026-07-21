# ColorSyncProfile.HeadroomAdaptiveGainCurve.ColorVolumeTransform

**Framework**: ColorSync  
**Kind**: struct

A color volume transform that maps HDR content into a display’s dynamic range.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
struct ColorVolumeTransform
```

#### Overview

A color volume transform can override the standard HDR reference white and, optionally, supply headroom-adaptive tone mapping.

## Topics

### Structures
- [ColorSyncProfile.HeadroomAdaptiveGainCurve.ColorVolumeTransform.ToneMapping](colorsyncprofile/headroomadaptivegaincurve-swift.struct/colorvolumetransform-swift.struct/tonemapping.md)
  Headroom-adaptive tone mapping that adjusts HDR content to the display’s available headroom.
### Initializers
- [init(customHDRReferenceWhite: Float?, adaptiveToneMapping: ColorSyncProfile.HeadroomAdaptiveGainCurve.ColorVolumeTransform.ToneMapping?) throws](colorsyncprofile/headroomadaptivegaincurve-swift.struct/colorvolumetransform-swift.struct/init(customhdrreferencewhite:adaptivetonemapping:).md)
  Creates a color volume transform.
### Instance Properties
- [var adaptiveToneMapping: ColorSyncProfile.HeadroomAdaptiveGainCurve.ColorVolumeTransform.ToneMapping?](colorsyncprofile/headroomadaptivegaincurve-swift.struct/colorvolumetransform-swift.struct/adaptivetonemapping.md)
  The adaptive tone mapping to apply, if any.
- [var customHDRReferenceWhite: Float?](colorsyncprofile/headroomadaptivegaincurve-swift.struct/colorvolumetransform-swift.struct/customhdrreferencewhite.md)
  A custom HDR reference white value, if specified.

## See Also

- [ColorSyncProfile.HeadroomAdaptiveGainCurve](colorsyncprofile/headroomadaptivegaincurve-swift.struct.md)
  Headroom Adaptive Gain Curve metadata that describes how to tone map a profile’s HDR content to the dynamic range available on the display.
- [ColorSyncProfile.HeadroomAdaptiveGainCurve.ColorVolumeTransform.ToneMapping](colorsyncprofile/headroomadaptivegaincurve-swift.struct/colorvolumetransform-swift.struct/tonemapping.md)
  Headroom-adaptive tone mapping that adjusts HDR content to the display’s available headroom.
- [ColorSyncProfile.HeadroomAdaptiveGainCurve.ColorVolumeTransform.ToneMapping.Method](colorsyncprofile/headroomadaptivegaincurve-swift.struct/colorvolumetransform-swift.struct/tonemapping/method-swift.enum.md)
  The tone-mapping method: reference-white-based, or a headroom-adaptive gain curve.
- [ColorSyncProfile.HeadroomAdaptiveGainCurve.Error](colorsyncprofile/headroomadaptivegaincurve-swift.struct/error.md)
  An error thrown while constructing Headroom Adaptive Gain Curve metadata.


---

*[View on Apple Developer](https://developer.apple.com/documentation/colorsync/colorsyncprofile/headroomadaptivegaincurve-swift.struct/colorvolumetransform-swift.struct)*