# isAutoExposureEnabled

**Framework**: MetalFX  
**Kind**: property

A Boolean value that indicates whether MetalFX calculates the exposure for each frame.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 26.0+ (Beta)
- tvOS 18.0+

## Declaration

```swift
var isAutoExposureEnabled: Bool { get set }
```

#### Discussion

Set this property to [`true`](https://developer.apple.com/documentation/swift/true) to create a scaler that automatically calculates the exposure level for each image it scales.

> **Note**: Denoiser scaler instances that use auto exposure ignore their [`exposureTexture`](mtlfxtemporalscalerbase/exposuretexture.md) property.

This property’s default value is [`false`](https://developer.apple.com/documentation/swift/false).


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalfx/mtlfxtemporaldenoisedscalerdescriptor/isautoexposureenabled)*