# postProcess

**Framework**: RealityKit  
**Kind**: property

A callback function for implementing postprocess effects.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+

## Declaration

```swift
var postProcess: ((ARView.PostProcessContext) -> Void)?
```

## Mentions

- [Implementing postprocess effects using Metal compute functions](implementing-postprocess-effects-using-metal-compute-functions.md)
- [Applying core image filters as a postprocess effect](applying-core-image-filters-as-a-postprocess-effect.md)
- [Using Metal performance shaders to create custom postprocess effects](using-metal-performance-shaders-to-create-custom-postprocess-effects.md)

#### Discussion

Assign a function or closure to this property to implement postprocessing effects for a RealityKit scene. If this value is non-`nil`, RealityKit calls the assigned function or closure once every frame before it displays the scene. If you register a postprocess render callback, the callback function needs to encode the modified frame buffer to the context’s [`targetColorTexture`](arview/postprocesscontext/targetcolortexture.md), or nothing renders.

A postprocess callback looks like this:

```swift
func myPostProcessCallback(context:ARView.PostProcessContext) {
   // Handle postprocessing here.
}
```

To register the function so RealityKit begins calling it, assign it to the [`postProcess`](arview/rendercallbacks-swift.struct/postprocess.md) property of the view’s [`renderCallbacks`](arview/rendercallbacks-swift.property.md) property.

```swift
arView.renderCallbacks.postProcess = myPostProcessCallback
```

To stop RealityKit from calling your function, assign `nil`:

```swift
arView.renderCallbacks.postProcess = nil
```

If your app turns postprocessing on and off frequently, another option for disabling postprocess effects is to keep your callback registered, but use an [`MTLBlitCommandEncoder`](https://developer.apple.com/documentation/Metal/MTLBlitCommandEncoder) to encode the unmodified frame directly to the output texture whenever postprocess effects aren’t active.

```swift
func myPostProcessCallback(context:ARView.PostProcessContext) {
    if (usePostProcessEffects) {
        handlePostProcessing(context: ARView.PostProcessContext)
        return
    }

    // If postprocess effects are disabled, copy sourceColorTexture
    // directly to targetColorTexture.
    let blitEncoder = context.commandBuffer.makeBlitCommandEncoder()
    blitEncoder?.copy(from: context.sourceColorTexture, to: context.targetColorTexture)
    blitEncoder?.endEncoding()
}
```

## See Also

- [var prepareWithDevice: ((any MTLDevice) -> Void)?](arview/rendercallbacks-swift.struct/preparewithdevice.md)
  A callback function for doing initial setup work.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/arview/rendercallbacks-swift.struct/postprocess)*