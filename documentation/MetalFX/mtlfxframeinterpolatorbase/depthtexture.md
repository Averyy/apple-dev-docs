# depthTexture

**Framework**: MetalFX  
**Kind**: property  
**Required**: Yes

The depth texture this frame interpolator evaluates.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- macOS 10.11+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
var depthTexture: (any MTLTexture)? { get set }
```

#### Discussion

You are responsible for ensuring the usage and pixel format of the texture you assign to this property matches the texture usage [`depthTextureUsage`](mtlfxframeinterpolatorbase/depthtextureusage.md) requests and the pixel format that [`depthTextureFormat`](mtlfxframeinterpolatorbase/depthtextureformat.md) requests.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalfx/mtlfxframeinterpolatorbase/depthtexture)*