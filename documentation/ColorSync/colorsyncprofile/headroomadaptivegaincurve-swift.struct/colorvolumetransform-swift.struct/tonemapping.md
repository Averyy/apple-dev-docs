# ColorSyncProfile.HeadroomAdaptiveGainCurve.ColorVolumeTransform.ToneMapping

**Framework**: ColorSync  
**Kind**: struct  
**Role**: Structure

Headroom-adaptive tone mapping that adjusts HDR content to the display’s available headroom.

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
struct ToneMapping
```

#### Overview

A tone mapping pairs a baseline headroom with a [`ColorSyncProfile.HeadroomAdaptiveGainCurve.ColorVolumeTransform.ToneMapping.Method`](./tonemapping/method-swift.enum.md) that describes how to map content above reference white.

## Topics

### Initializers
- [init(baselineHeadroomStops: Float, method: ColorSyncProfile.HeadroomAdaptiveGainCurve.ColorVolumeTransform.ToneMapping.Method) throws](./tonemapping/init%28baselineheadroomstops,method%29.md)
  Creates a headroom-adaptive tone mapping.
### Instance Properties
- [var baselineHeadroomStops: Float](./tonemapping/baselineheadroomstops.md)
  Baseline headroom in stops above reference white.
- [var method: ColorSyncProfile.HeadroomAdaptiveGainCurve.ColorVolumeTransform.ToneMapping.Method](./tonemapping/method-swift.property.md)
  The method used to tone map content above reference white.
### Enumerations
- [ColorSyncProfile.HeadroomAdaptiveGainCurve.ColorVolumeTransform.ToneMapping.Method](./tonemapping/method-swift.enum.md)
  The tone-mapping method: reference-white-based, or a headroom-adaptive gain curve.

## See Also

### Describing a curve in Swift
- [ColorSyncProfile.HeadroomAdaptiveGainCurve](../../headroomadaptivegaincurve-swift.struct.md)
  Headroom Adaptive Gain Curve metadata that describes how to tone map a profile’s HDR content to the dynamic range available on the display.
- [ColorSyncProfile.HeadroomAdaptiveGainCurve.ColorVolumeTransform](../colorvolumetransform-swift.struct.md)
  A color volume transform that maps HDR content into a display’s dynamic range.
- [ColorSyncProfile.HeadroomAdaptiveGainCurve.ColorVolumeTransform.ToneMapping.Method](./tonemapping/method-swift.enum.md)
  The tone-mapping method: reference-white-based, or a headroom-adaptive gain curve.
- [ColorSyncProfile.HeadroomAdaptiveGainCurve.Error](../error.md)
  An error thrown while constructing Headroom Adaptive Gain Curve metadata.


---

*[View on Apple Developer](https://developer.apple.com/documentation/colorsync/colorsyncprofile/headroomadaptivegaincurve-swift.struct/colorvolumetransform-swift.struct/tonemapping)*