# renderCallbacks

**Framework**: RealityKit  
**Kind**: property

A container that holds the view’s render callbacks.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+ (Beta)

## Declaration

```swift
@MainActor
@preconcurrency var renderCallbacks: ARView.RenderCallbacks { get set }
```

## Mentions

- [Applying core image filters as a postprocess effect](applying-core-image-filters-as-a-postprocess-effect.md)
- [Implementing postprocess effects using Metal compute functions](implementing-postprocess-effects-using-metal-compute-functions.md)

#### Discussion

Render callbacks are closures RealityKit calls at predefined times. You can use render callbacks to modify the results of RealityKit’s rendering. If you assign a function or closure to any of the contained callback properties, RealityKit calls that function or closure at a predefined time. Setting the `ARView/RenderCallbacks-swift.postProcess` property, for example, causes RealityKit to call the assigned function or closure every frame, after RealityKit renders the scene, but before it displays it.

## See Also

- [var session: ARSession](arview/session.md)
  The AR session that supports the view’s rendering.
- [var automaticallyConfigureSession: Bool](arview/automaticallyconfiguresession.md)
  An indication of whether to use an automatically configured AR session.
- [var renderOptions: ARView.RenderOptions](arview/renderoptions-swift.property.md)
  The render options that configure the view’s AR session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/arview/rendercallbacks-swift.property)*