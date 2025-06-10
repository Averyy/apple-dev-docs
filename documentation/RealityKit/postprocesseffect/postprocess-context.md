# postProcess(context:)

**Framework**: RealityKit  
**Kind**: method  
**Required**: Yes

A method where you can implement postprocess effects.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)

## Declaration

```swift
nonisolated
func postProcess(context: borrowing PostProcessEffectContext<any MTLCommandBuffer>)
```

#### Discussion

RealityKit calls this method after rendering the main scene, but before it is drawn on the screen, ideal for performing screen-space effects or drawing overlays.

When registering a post processing effect, the callback function needs to encode the modified frame buffer to the context’s [`targetColorTexture`](postprocesseffectcontext/targetcolortexture.md), or nothing renders.

An empty implementation might look like this, which copies the [`sourceColorTexture`](postprocesseffectcontext/sourcecolortexture.md) directly to the [`targetColorTexture`](postprocesseffectcontext/targetcolortexture.md):

```swift
func postProcess(context: borrowing PostProcessEffectContext<MTLCommandBuffer>) {
    // Post processing with no effect.
    let blitEncoder = context.commandBuffer.makeBlitCommandEncoder()
    blitEncoder?.copy(from: context.sourceColorTexture, to: context.targetColorTexture)
    blitEncoder?.endEncoding()
}
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/postprocesseffect/postprocess(context:))*