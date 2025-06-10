# init(_:_:_:_:_:_:_:)

**Framework**: RealityKit  
**Kind**: init

Creates a new context object.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+ (Beta)

## Declaration

```swift
init(_ device: any MTLDevice, _ commandBuffer: any MTLCommandBuffer, _ sourceColorTexture: any MTLTexture, _ sourceDepthTexture: any MTLTexture, _ targetColorTexture: any MTLTexture, _ projection: float4x4, _ time: TimeInterval)
```

#### Discussion

This initializer creates a new postprocess context object. RealityKit creates context objects and passes them to the postprocess render callback. Your code won’t usually need to create context objects directly.

## Parameters

- `device`: The Metal device the view renders to.
- `commandBuffer`: The Metal command buffer that encodes this view.
- `sourceColorTexture`: A texture containing the rendered frame.
- `sourceDepthTexture`: A texture containing the frame’s depth buffer.
- `targetColorTexture`: A texture the callback function writes to.
- `projection`: The projection matrix for this frame.
- `time`: The current elapsed time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/arview/postprocesscontext/init(_:_:_:_:_:_:_:))*