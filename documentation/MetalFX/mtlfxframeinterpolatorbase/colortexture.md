# colorTexture

**Framework**: MetalFX  
**Kind**: property  
**Required**: Yes

The color texture that this frame interpolator evaluates.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- macOS 10.11+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
var colorTexture: (any MTLTexture)? { get set }
```

#### Discussion

You are responsible for ensuring the usage and pixel format of the texture you assign to this property matches the texture usage [`colorTextureUsage`](mtlfxframeinterpolatorbase/colortextureusage.md) requests and the pixel format that [`colorTextureFormat`](mtlfxframeinterpolatorbase/colortextureformat.md) requests.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalfx/mtlfxframeinterpolatorbase/colortexture)*