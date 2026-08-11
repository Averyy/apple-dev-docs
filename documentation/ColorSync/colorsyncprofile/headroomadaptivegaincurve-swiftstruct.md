# ColorSyncProfile.HeadroomAdaptiveGainCurve

**Framework**: ColorSync  
**Kind**: struct

Headroom Adaptive Gain Curve metadata that describes how to tone map a profile’s HDR content to the dynamic range available on the display.

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
struct HeadroomAdaptiveGainCurve
```

#### Overview

A profile stores this metadata in its HAGC tag; it applies only to profiles whose transfer function is PQ, HLG, or linear. Use [`colorVolumeTransform`](colorsyncprofile/headroomadaptivegaincurve-swift.struct/colorvolumetransform-swift.property.md) to describe the tone mapping to perform, then embed the curve in a profile with `ColorSyncProfileCreateCopyWithHeadroomAdaptiveGainCurveInfoDictionary`.

## Topics

### Structures
- [ColorSyncProfile.HeadroomAdaptiveGainCurve.ColorVolumeTransform](colorsyncprofile/headroomadaptivegaincurve-swift.struct/colorvolumetransform-swift.struct.md)
  A color volume transform that maps HDR content into a display’s dynamic range.
### Initializers
- [init(applicationVersion: UInt8, colorVolumeTransform: ColorSyncProfile.HeadroomAdaptiveGainCurve.ColorVolumeTransform?) throws](colorsyncprofile/headroomadaptivegaincurve-swift.struct/init(applicationversion:colorvolumetransform:).md)
  Creates Headroom Adaptive Gain Curve metadata.
### Instance Properties
- [var applicationVersion: UInt8](colorsyncprofile/headroomadaptivegaincurve-swift.struct/applicationversion.md)
  The application version of the metadata, as defined by ST 2094-50.
- [var colorVolumeTransform: ColorSyncProfile.HeadroomAdaptiveGainCurve.ColorVolumeTransform?](colorsyncprofile/headroomadaptivegaincurve-swift.struct/colorvolumetransform-swift.property.md)
  The color volume transform to apply, if any.
### Enumerations
- [ColorSyncProfile.HeadroomAdaptiveGainCurve.Error](colorsyncprofile/headroomadaptivegaincurve-swift.struct/error.md)
  An error thrown while constructing Headroom Adaptive Gain Curve metadata.

## See Also

- [ColorSyncProfile.HeadroomAdaptiveGainCurve.ColorVolumeTransform](colorsyncprofile/headroomadaptivegaincurve-swift.struct/colorvolumetransform-swift.struct.md)
  A color volume transform that maps HDR content into a display’s dynamic range.
- [ColorSyncProfile.HeadroomAdaptiveGainCurve.ColorVolumeTransform.ToneMapping](colorsyncprofile/headroomadaptivegaincurve-swift.struct/colorvolumetransform-swift.struct/tonemapping.md)
  Headroom-adaptive tone mapping that adjusts HDR content to the display’s available headroom.
- [ColorSyncProfile.HeadroomAdaptiveGainCurve.ColorVolumeTransform.ToneMapping.Method](colorsyncprofile/headroomadaptivegaincurve-swift.struct/colorvolumetransform-swift.struct/tonemapping/method-swift.enum.md)
  The tone-mapping method: reference-white-based, or a headroom-adaptive gain curve.
- [ColorSyncProfile.HeadroomAdaptiveGainCurve.Error](colorsyncprofile/headroomadaptivegaincurve-swift.struct/error.md)
  An error thrown while constructing Headroom Adaptive Gain Curve metadata.


---

*[View on Apple Developer](https://developer.apple.com/documentation/colorsync/colorsyncprofile/headroomadaptivegaincurve-swift.struct)*