# init(baselineHeadroomStops:method:)

**Framework**: ColorSync  
**Kind**: init

Creates a headroom-adaptive tone mapping.

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
init(baselineHeadroomStops: Float, method: ColorSyncProfile.HeadroomAdaptiveGainCurve.ColorVolumeTransform.ToneMapping.Method = .referenceWhiteBased) throws
```

#### Discussion

> **Note**: [`ColorSyncProfile.HeadroomAdaptiveGainCurve.Error.negativeBaselineHeadroom(_:)`](colorsyncprofile/headroomadaptivegaincurve-swift.struct/error/negativebaselineheadroom(_:).md) if `baselineHeadroomStops` is negative.

## Parameters

- `baselineHeadroomStops`: The headroom of the source content in stops above reference white. Must be greater than or equal to `0`.
- `method`: The tone-mapping method to apply. Defaults to [`ColorSyncProfile.HeadroomAdaptiveGainCurve.ColorVolumeTransform.ToneMapping.Method.referenceWhiteBased`](colorsyncprofile/headroomadaptivegaincurve-swift.struct/colorvolumetransform-swift.struct/tonemapping/method-swift.enum/referencewhitebased.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/colorsync/colorsyncprofile/headroomadaptivegaincurve-swift.struct/colorvolumetransform-swift.struct/tonemapping/init(baselineheadroomstops:method:))*