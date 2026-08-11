# init(chromaticities:alternateCurves:)

**Framework**: ColorSync  
**Kind**: init

Creates an adaptive gain curve.

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
init(chromaticities: ColorSyncProfile.HeadroomAdaptiveGainCurve.ColorVolumeTransform.ToneMapping.Method.Chromaticities = .bt709, alternateCurves: [ColorSyncProfile.HeadroomAdaptiveGainCurve.ColorVolumeTransform.ToneMapping.Method.AlternateCurve]) throws
```

#### Discussion

> **Note**: [`ColorSyncProfile.HeadroomAdaptiveGainCurve.Error.tooManyAlternateCurves(count:limit:)`](colorsyncprofile/headroomadaptivegaincurve-swift.struct/error/toomanyalternatecurves(count:limit:).md) if more than four curves are supplied, or [`ColorSyncProfile.HeadroomAdaptiveGainCurve.Error.invalidCustomChromaticities`](colorsyncprofile/headroomadaptivegaincurve-swift.struct/error/invalidcustomchromaticities.md) if custom chromaticities fall outside the valid range.

## Parameters

- `chromaticities`: The chromaticities used to derive the driving signal. Defaults to [`ColorSyncProfile.HeadroomAdaptiveGainCurve.ColorVolumeTransform.ToneMapping.Method.Chromaticities.bt709`](colorsyncprofile/headroomadaptivegaincurve-swift.struct/colorvolumetransform-swift.struct/tonemapping/method-swift.enum/chromaticities/bt709.md).
- `alternateCurves`: The alternate curves. At most four.


---

*[View on Apple Developer](https://developer.apple.com/documentation/colorsync/colorsyncprofile/headroomadaptivegaincurve-swift.struct/colorvolumetransform-swift.struct/tonemapping/method-swift.enum/adaptivegaincurve/init(chromaticities:alternatecurves:))*