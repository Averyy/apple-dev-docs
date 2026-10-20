# init(chromaticities:alternateCurves:)

**Framework**: ColorSync  
**Kind**: init  
**Role**: Initializer

Creates an adaptive gain curve.

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
init(chromaticities: ColorSyncProfile.HeadroomAdaptiveGainCurve.ColorVolumeTransform.ToneMapping.Method.Chromaticities = .bt709, alternateCurves: [ColorSyncProfile.HeadroomAdaptiveGainCurve.ColorVolumeTransform.ToneMapping.Method.AlternateCurve]) throws
```

#### Discussion

> **Throws**: [`ColorSyncProfile.HeadroomAdaptiveGainCurve.Error.tooManyAlternateCurves(count:limit:)`](../../../../error/toomanyalternatecurves%28count,limit%29.md) if more than four curves are supplied, or [`ColorSyncProfile.HeadroomAdaptiveGainCurve.Error.invalidCustomChromaticities`](../../../../error/invalidcustomchromaticities.md) if custom chromaticities fall outside the valid range.

## Parameters

- `chromaticities`: The chromaticities used to derive the driving signal. Defaults to [`ColorSyncProfile.HeadroomAdaptiveGainCurve.ColorVolumeTransform.ToneMapping.Method.Chromaticities.bt709`](../chromaticities/bt709.md).
- `alternateCurves`: The alternate curves. At most four.


---

*[View on Apple Developer](https://developer.apple.com/documentation/colorsync/colorsyncprofile/headroomadaptivegaincurve-swift.struct/colorvolumetransform-swift.struct/tonemapping/method-swift.enum/adaptivegaincurve/init(chromaticities:alternatecurves:))*