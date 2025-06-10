# prevColorTexture

**Framework**: MetalFX  
**Kind**: property  
**Required**: Yes

The previous color texture for this frame interpolator during the last call to encode work into a command buffer.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- macOS 10.11+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
var prevColorTexture: (any MTLTexture)? { get set }
```

#### Discussion

The frame interpolator typically uses the previous color texture as part of its operation. When you call [`encode(to:)`](mtlfxframeinterpolator/encode(to:).md) and its [`shouldResetHistory`](mtlfxframeinterpolatorbase/shouldresethistory.md) property is [`false`](https://developer.apple.com/documentation/swift/false), then you are responsible for assigning to this property the data that in [`colorTexture`](mtlfxframeinterpolatorbase/colortexture.md) from the previous call to [`encode(to:)`](mtlfxframeinterpolator/encode(to:).md).

Additionally, you are responsible for ensuring the usage and pixel format of the texture you assign to this property matches the texture usage [`colorTextureUsage`](mtlfxframeinterpolatorbase/colortextureusage.md) requests and the pixel format that [`colorTextureFormat`](mtlfxframeinterpolatorbase/colortextureformat.md) requests.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalfx/mtlfxframeinterpolatorbase/prevcolortexture)*