# init(applicationVersion:colorVolumeTransform:)

**Framework**: ColorSync  
**Kind**: init

Creates Headroom Adaptive Gain Curve metadata.

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
init(applicationVersion: UInt8 = 0, colorVolumeTransform: ColorSyncProfile.HeadroomAdaptiveGainCurve.ColorVolumeTransform? = nil) throws
```

#### Discussion

> **Note**: [`ColorSyncProfile.HeadroomAdaptiveGainCurve.Error.unsupportedApplicationVersion(_:)`](colorsyncprofile/headroomadaptivegaincurve-swift.struct/error/unsupportedapplicationversion(_:).md) if `applicationVersion` is not `0`.

## Parameters

- `applicationVersion`: The ST 2094-50 application version. Must be `0`.
- `colorVolumeTransform`: The color volume transform to apply, or `nil` for none.


---

*[View on Apple Developer](https://developer.apple.com/documentation/colorsync/colorsyncprofile/headroomadaptivegaincurve-swift.struct/init(applicationversion:colorvolumetransform:))*