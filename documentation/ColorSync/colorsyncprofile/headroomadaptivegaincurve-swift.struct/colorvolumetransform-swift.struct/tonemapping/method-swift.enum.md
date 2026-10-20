# ColorSyncProfile.HeadroomAdaptiveGainCurve.ColorVolumeTransform.ToneMapping.Method

**Framework**: ColorSync  
**Kind**: enum  
**Role**: Enumeration

The tone-mapping method: reference-white-based, or a headroom-adaptive gain curve.

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
enum Method
```

## Topics

### Structures
- [ColorSyncProfile.HeadroomAdaptiveGainCurve.ColorVolumeTransform.ToneMapping.Method.AdaptiveGainCurve](./method-swift.enum/adaptivegaincurve.md)
  A set of headroom-adaptive gain curves and the chromaticities used to drive them.
- [ColorSyncProfile.HeadroomAdaptiveGainCurve.ColorVolumeTransform.ToneMapping.Method.AlternateCurve](./method-swift.enum/alternatecurve.md)
  An alternate gain curve that targets a specific display headroom level.
### Enumeration Cases
- [case adaptiveGainCurveMapping(ColorSyncProfile.HeadroomAdaptiveGainCurve.ColorVolumeTransform.ToneMapping.Method.AdaptiveGainCurve)](./method-swift.enum/adaptivegaincurvemapping%28_%29.md)
  Maps content above reference white using a headroom-adaptive gain curve.
- [ColorSyncProfile.HeadroomAdaptiveGainCurve.ColorVolumeTransform.ToneMapping.Method.referenceWhiteBased](./method-swift.enum/referencewhitebased.md)
  Maps content above reference white using the Reference-White-Based Tone Mapping method.
### Enumerations
- [ColorSyncProfile.HeadroomAdaptiveGainCurve.ColorVolumeTransform.ToneMapping.Method.Chromaticities](./method-swift.enum/chromaticities.md)
  The color space chromaticities used to derive a gain curve’s driving signal.

## See Also

### Describing a curve in Swift
- [ColorSyncProfile.HeadroomAdaptiveGainCurve](../../../headroomadaptivegaincurve-swift.struct.md)
  Headroom Adaptive Gain Curve metadata that describes how to tone map a profile’s HDR content to the dynamic range available on the display.
- [ColorSyncProfile.HeadroomAdaptiveGainCurve.ColorVolumeTransform](../../colorvolumetransform-swift.struct.md)
  A color volume transform that maps HDR content into a display’s dynamic range.
- [ColorSyncProfile.HeadroomAdaptiveGainCurve.ColorVolumeTransform.ToneMapping](../tonemapping.md)
  Headroom-adaptive tone mapping that adjusts HDR content to the display’s available headroom.
- [ColorSyncProfile.HeadroomAdaptiveGainCurve.Error](../../error.md)
  An error thrown while constructing Headroom Adaptive Gain Curve metadata.


---

*[View on Apple Developer](https://developer.apple.com/documentation/colorsync/colorsyncprofile/headroomadaptivegaincurve-swift.struct/colorvolumetransform-swift.struct/tonemapping/method-swift.enum)*