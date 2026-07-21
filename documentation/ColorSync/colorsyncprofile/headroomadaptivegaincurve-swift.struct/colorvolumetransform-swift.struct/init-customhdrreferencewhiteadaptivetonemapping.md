# init(customHDRReferenceWhite:adaptiveToneMapping:)

**Framework**: ColorSync  
**Kind**: init

Creates a color volume transform.

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
init(customHDRReferenceWhite: Float? = nil, adaptiveToneMapping: ColorSyncProfile.HeadroomAdaptiveGainCurve.ColorVolumeTransform.ToneMapping? = nil) throws
```

#### Discussion

> **Note**: [`ColorSyncProfile.HeadroomAdaptiveGainCurve.Error.invalidHDRReferenceWhite(_:)`](colorsyncprofile/headroomadaptivegaincurve-swift.struct/error/invalidhdrreferencewhite(_:).md) if `customHDRReferenceWhite` is less than or equal to `0`.

## Parameters

- `customHDRReferenceWhite`: A custom HDR reference white luminance in nits, or `nil` to use the standard 203-nit reference white. Must be greater than `0` when specified.
- `adaptiveToneMapping`: The headroom-adaptive tone mapping to apply, or `nil` for none.


---

*[View on Apple Developer](https://developer.apple.com/documentation/colorsync/colorsyncprofile/headroomadaptivegaincurve-swift.struct/colorvolumetransform-swift.struct/init(customhdrreferencewhite:adaptivetonemapping:))*