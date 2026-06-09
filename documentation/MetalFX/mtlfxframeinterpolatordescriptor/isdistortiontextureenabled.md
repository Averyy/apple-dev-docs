# isDistortionTextureEnabled

**Framework**: MetalFX  
**Kind**: property

A Boolean value that indicates whether the frame interpolator supports barrel distortion correction.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)

## Declaration

```swift
var isDistortionTextureEnabled: Bool { get set }
```

#### Discussion

Set this property to [`true`](https://developer.apple.com/documentation/Swift/true) to create a frame interpolator that can apply barrel distortion correction using a distortion field texture.

When you enable this property, you can assign a distortion texture to the interpolator’s [`distortionTexture`](mtlfxframeinterpolatorbase/distortiontexture.md) property to correct lens distortion artifacts during frame interpolation.

This property’s default value is [`false`](https://developer.apple.com/documentation/Swift/false).


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalfx/mtlfxframeinterpolatordescriptor/isdistortiontextureenabled)*