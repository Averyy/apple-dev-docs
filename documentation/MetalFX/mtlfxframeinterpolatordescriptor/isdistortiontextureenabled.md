# isDistortionTextureEnabled

**Framework**: MetalFX  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the frame interpolator supports barrel distortion correction.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.1+

## Declaration

```swift
var isDistortionTextureEnabled: Bool { get set }
```

```objc
@property (nonatomic, readwrite, getter=isDistortionTextureEnabled) BOOL distortionTextureEnabled;
```

#### Discussion

Set this property to [`true`](../../Swift/true.md) to create a frame interpolator that can apply barrel distortion correction using a distortion field texture.

When you enable this property, you can assign a distortion texture to the interpolator’s [`distortionTexture`](../mtlfxframeinterpolatorbase/distortiontexture.md) property to correct lens distortion artifacts during frame interpolation.

This property’s default value is [`false`](../../Swift/false.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalfx/mtlfxframeinterpolatordescriptor/isdistortiontextureenabled)*