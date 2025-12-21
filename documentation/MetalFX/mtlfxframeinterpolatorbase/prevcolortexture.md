# prevColorTexture

**Framework**: MetalFX  
**Kind**: property  
**Required**: Yes

The previous color texture for this frame interpolator during the last call to encode work into a command buffer.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+

## Declaration

```swift
var prevColorTexture: (any MTLTexture)? { get set }
```

#### Discussion

The frame interpolator typically uses the previous color texture as part of its operation. When you call [`encode(commandBuffer:)`](mtlfxframeinterpolator/encode(commandbuffer:).md) and its [`shouldResetHistory`](mtlfxframeinterpolatorbase/shouldresethistory.md) property is [`false`](https://developer.apple.com/documentation/Swift/false), then you are responsible for assigning to this property the data that in [`colorTexture`](mtlfxframeinterpolatorbase/colortexture.md) from the previous call to [`encode(commandBuffer:)`](mtlfxframeinterpolator/encode(commandbuffer:).md).

Additionally, you are responsible for ensuring the usage and pixel format of the texture you assign to this property matches the texture usage [`colorTextureUsage`](mtlfxframeinterpolatorbase/colortextureusage.md) requests and the pixel format that [`colorTextureFormat`](mtlfxframeinterpolatorbase/colortextureformat.md) requests.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalfx/mtlfxframeinterpolatorbase/prevcolortexture)*