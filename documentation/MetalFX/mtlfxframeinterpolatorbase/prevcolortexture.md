# prevColorTexture

**Framework**: MetalFX  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

The previous color texture for this frame interpolator during the last call to encode work into a command buffer.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 27.1+

## Declaration

```swift
var prevColorTexture: (any MTLTexture)? { get set }
```

```objc
@property (nonatomic, retain, nullable) id<MTLTexture> prevColorTexture;
```

## Discussion

The frame interpolator typically uses the previous color texture as part of its operation. When you call [`encode(commandBuffer:)`](../mtlfxframeinterpolator/encode%28commandbuffer%29.md) and its [`shouldResetHistory`](./shouldresethistory.md) property is [`false`](../../Swift/false.md), then you are responsible for assigning to this property the data that in [`colorTexture`](./colortexture.md) from the previous call to [`encode(commandBuffer:)`](../mtlfxframeinterpolator/encode%28commandbuffer%29.md).

Additionally, you are responsible for ensuring the usage and pixel format of the texture you assign to this property matches the texture usage [`colorTextureUsage`](./colortextureusage.md) requests and the pixel format that [`colorTextureFormat`](./colortextureformat.md) requests.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalfx/mtlfxframeinterpolatorbase/prevcolortexture)*