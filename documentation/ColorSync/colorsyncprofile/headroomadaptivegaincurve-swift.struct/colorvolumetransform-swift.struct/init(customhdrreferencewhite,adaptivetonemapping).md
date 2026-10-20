# init(customHDRReferenceWhite:adaptiveToneMapping:)

**Framework**: ColorSync  
**Kind**: init  
**Role**: Initializer

Creates a color volume transform.

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
init(customHDRReferenceWhite: Float? = nil, adaptiveToneMapping: ColorSyncProfile.HeadroomAdaptiveGainCurve.ColorVolumeTransform.ToneMapping? = nil) throws
```

#### Discussion

> **Throws**: [`ColorSyncProfile.HeadroomAdaptiveGainCurve.Error.invalidHDRReferenceWhite(_:)`](../error/invalidhdrreferencewhite%28_%29.md) if `customHDRReferenceWhite` is less than or equal to `0`.

## Parameters

- `customHDRReferenceWhite`: A custom HDR reference white luminance in nits, or `nil` to use the standard 203-nit reference white. Must be greater than `0` when specified.
- `adaptiveToneMapping`: The headroom-adaptive tone mapping to apply, or `nil` for none.


---

*[View on Apple Developer](https://developer.apple.com/documentation/colorsync/colorsyncprofile/headroomadaptivegaincurve-swift.struct/colorvolumetransform-swift.struct/init(customhdrreferencewhite:adaptivetonemapping:))*