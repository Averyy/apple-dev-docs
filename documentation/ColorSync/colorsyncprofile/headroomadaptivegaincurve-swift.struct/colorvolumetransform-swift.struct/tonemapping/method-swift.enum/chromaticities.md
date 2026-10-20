# ColorSyncProfile.HeadroomAdaptiveGainCurve.ColorVolumeTransform.ToneMapping.Method.Chromaticities

**Framework**: ColorSync  
**Kind**: enum  
**Role**: Enumeration

The color space chromaticities used to derive a gain curve’s driving signal.

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
enum Chromaticities
```

## Topics

### Enumeration Cases
- [ColorSyncProfile.HeadroomAdaptiveGainCurve.ColorVolumeTransform.ToneMapping.Method.Chromaticities.bt2020](./chromaticities/bt2020.md)
  Recommendation ITU-R BT.2020-2 primaries.
- [ColorSyncProfile.HeadroomAdaptiveGainCurve.ColorVolumeTransform.ToneMapping.Method.Chromaticities.bt709](./chromaticities/bt709.md)
  Recommendation ITU-R BT.709-6 primaries.
- [ColorSyncProfile.HeadroomAdaptiveGainCurve.ColorVolumeTransform.ToneMapping.Method.Chromaticities.custom(red:green:blue:white:)](./chromaticities/custom%28red,green,blue,white%29.md)
  Custom primaries, given as xy chromaticity pairs for the red, green, and blue channels and the white point.
- [ColorSyncProfile.HeadroomAdaptiveGainCurve.ColorVolumeTransform.ToneMapping.Method.Chromaticities.displayP3](./chromaticities/displayp3.md)
  Display P3 primaries (SMPTE ST 2113:2018).


---

*[View on Apple Developer](https://developer.apple.com/documentation/colorsync/colorsyncprofile/headroomadaptivegaincurve-swift.struct/colorvolumetransform-swift.struct/tonemapping/method-swift.enum/chromaticities)*