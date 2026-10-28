# ColorSyncProfile.HeadroomAdaptiveGainCurve

**Framework**: ColorSync  
**Kind**: struct  
**Role**: Structure

Headroom Adaptive Gain Curve metadata that describes how to tone map a profile’s HDR content to the dynamic range available on the display.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
struct HeadroomAdaptiveGainCurve
```

## Overview

A profile stores this metadata in its HAGC tag; it applies only to profiles whose transfer function is PQ, HLG, or linear. Use [`colorVolumeTransform`](./headroomadaptivegaincurve-swift.struct/colorvolumetransform-swift.property.md) to describe the tone mapping to perform, then embed the curve in a profile with `ColorSyncProfileCreateCopyWithHeadroomAdaptiveGainCurveInfoDictionary`.

## Topics

### Structures
- [ColorSyncProfile.HeadroomAdaptiveGainCurve.ColorVolumeTransform](./headroomadaptivegaincurve-swift.struct/colorvolumetransform-swift.struct.md)
  A color volume transform that maps HDR content into a display’s dynamic range.
### Initializers
- [init(applicationVersion: UInt8, colorVolumeTransform: ColorSyncProfile.HeadroomAdaptiveGainCurve.ColorVolumeTransform?) throws](./headroomadaptivegaincurve-swift.struct/init%28applicationversion,colorvolumetransform%29.md)
  Creates Headroom Adaptive Gain Curve metadata.
### Instance Properties
- [var applicationVersion: UInt8](./headroomadaptivegaincurve-swift.struct/applicationversion.md)
  The application version of the metadata, as defined by ST 2094-50.
- [var colorVolumeTransform: ColorSyncProfile.HeadroomAdaptiveGainCurve.ColorVolumeTransform?](./headroomadaptivegaincurve-swift.struct/colorvolumetransform-swift.property.md)
  The color volume transform to apply, if any.
### Enumerations
- [ColorSyncProfile.HeadroomAdaptiveGainCurve.Error](./headroomadaptivegaincurve-swift.struct/error.md)
  An error thrown while constructing Headroom Adaptive Gain Curve metadata.

## See Also

### Describing a curve in Swift
- [ColorSyncProfile.HeadroomAdaptiveGainCurve.ColorVolumeTransform](./headroomadaptivegaincurve-swift.struct/colorvolumetransform-swift.struct.md)
  A color volume transform that maps HDR content into a display’s dynamic range.
- [ColorSyncProfile.HeadroomAdaptiveGainCurve.ColorVolumeTransform.ToneMapping](./headroomadaptivegaincurve-swift.struct/colorvolumetransform-swift.struct/tonemapping.md)
  Headroom-adaptive tone mapping that adjusts HDR content to the display’s available headroom.
- [ColorSyncProfile.HeadroomAdaptiveGainCurve.ColorVolumeTransform.ToneMapping.Method](./headroomadaptivegaincurve-swift.struct/colorvolumetransform-swift.struct/tonemapping/method-swift.enum.md)
  The tone-mapping method: reference-white-based, or a headroom-adaptive gain curve.
- [ColorSyncProfile.HeadroomAdaptiveGainCurve.Error](./headroomadaptivegaincurve-swift.struct/error.md)
  An error thrown while constructing Headroom Adaptive Gain Curve metadata.


---

*[View on Apple Developer](https://developer.apple.com/documentation/colorsync/colorsyncprofile/headroomadaptivegaincurve-swift.struct)*