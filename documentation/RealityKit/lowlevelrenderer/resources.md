# LowLevelRenderer.Resources

**Framework**: RealityKit  
**Kind**: struct

Prepared GPU resources for a renderer.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct Resources
```

## Topics

### Creating resources
- [init(configuration: LowLevelRenderer.Configuration, renderContext: any LowLevelRenderContext) async throws](lowlevelrenderer/resources/init(configuration:rendercontext:).md)
  Asynchronously compiles all shader and pipeline resources for the given configuration and render context.

## See Also

- [func render(using: any MTLCommandBuffer, (inout LowLevelRenderer.RenderState) -> ())](lowlevelrenderer/render(using:_:).md)
  Encodes draw calls for the frame into the given command buffer using a caller-controlled render callback.
- [LowLevelRenderer.RenderState](lowlevelrenderer/renderstate.md)
  The per-frame render state passed to the `render(using:_:)` callback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelrenderer/resources)*