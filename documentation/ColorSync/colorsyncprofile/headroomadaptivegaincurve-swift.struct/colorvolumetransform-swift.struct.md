# ColorSyncProfile.HeadroomAdaptiveGainCurve.ColorVolumeTransform

**Framework**: ColorSync  
**Kind**: struct  
**Role**: Structure

A color volume transform that maps HDR content into a display’s dynamic range.

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
struct ColorVolumeTransform
```

## Overview

A color volume transform can override the standard HDR reference white and, optionally, supply headroom-adaptive tone mapping.

## Topics

### Structures
- [ColorSyncProfile.HeadroomAdaptiveGainCurve.ColorVolumeTransform.ToneMapping](./colorvolumetransform-swift.struct/tonemapping.md)
  Headroom-adaptive tone mapping that adjusts HDR content to the display’s available headroom.
### Initializers
- [init(customHDRReferenceWhite: Float?, adaptiveToneMapping: ColorSyncProfile.HeadroomAdaptiveGainCurve.ColorVolumeTransform.ToneMapping?) throws](./colorvolumetransform-swift.struct/init%28customhdrreferencewhite,adaptivetonemapping%29.md)
  Creates a color volume transform.
### Instance Properties
- [var adaptiveToneMapping: ColorSyncProfile.HeadroomAdaptiveGainCurve.ColorVolumeTransform.ToneMapping?](./colorvolumetransform-swift.struct/adaptivetonemapping.md)
  The adaptive tone mapping to apply, if any.
- [var customHDRReferenceWhite: Float?](./colorvolumetransform-swift.struct/customhdrreferencewhite.md)
  A custom HDR reference white value, if specified.

## See Also

### Describing a curve in Swift
- [ColorSyncProfile.HeadroomAdaptiveGainCurve](../headroomadaptivegaincurve-swift.struct.md)
  Headroom Adaptive Gain Curve metadata that describes how to tone map a profile’s HDR content to the dynamic range available on the display.
- [ColorSyncProfile.HeadroomAdaptiveGainCurve.ColorVolumeTransform.ToneMapping](./colorvolumetransform-swift.struct/tonemapping.md)
  Headroom-adaptive tone mapping that adjusts HDR content to the display’s available headroom.
- [ColorSyncProfile.HeadroomAdaptiveGainCurve.ColorVolumeTransform.ToneMapping.Method](./colorvolumetransform-swift.struct/tonemapping/method-swift.enum.md)
  The tone-mapping method: reference-white-based, or a headroom-adaptive gain curve.
- [ColorSyncProfile.HeadroomAdaptiveGainCurve.Error](./error.md)
  An error thrown while constructing Headroom Adaptive Gain Curve metadata.


---

*[View on Apple Developer](https://developer.apple.com/documentation/colorsync/colorsyncprofile/headroomadaptivegaincurve-swift.struct/colorvolumetransform-swift.struct)*