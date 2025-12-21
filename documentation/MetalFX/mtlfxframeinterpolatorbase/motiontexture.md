# motionTexture

**Framework**: MetalFX  
**Kind**: property  
**Required**: Yes

The motion texture this frame interpolator evaluates.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+

## Declaration

```swift
var motionTexture: (any MTLTexture)? { get set }
```

#### Discussion

You are responsible for ensuring the usage and pixel format of the texture you assign to this property matches the texture usage [`motionTextureUsage`](mtlfxframeinterpolatorbase/motiontextureusage.md) requests and the pixel format that [`motionTextureFormat`](mtlfxframeinterpolatorbase/motiontextureformat.md) requests.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalfx/mtlfxframeinterpolatorbase/motiontexture)*