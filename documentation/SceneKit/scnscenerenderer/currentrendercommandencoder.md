# currentRenderCommandEncoder

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

The Metal render command encoder in use for the current SceneKit rendering pass.

**Availability**:
- iOS 8.0+ - Deprecated in 26.0
- iPadOS 8.0+ - Deprecated in 26.0
- Mac Catalyst 13.1+ - Deprecated in 26.0
- macOS 10.8+ - Deprecated in 26.0
- tvOS 9.0+ - Deprecated in 26.0
- visionOS 1.0+ - Deprecated in 26.0
- watchOS 3.0+ - Deprecated in 26.0

## Declaration

```swift
var currentRenderCommandEncoder: (any MTLRenderCommandEncoder)? { get }
```

```objc
@property (nonatomic, readonly, nullable) id<MTLRenderCommandEncoder> currentRenderCommandEncoder;
```

#### Discussion

Use this render command encoder to encode additional rendering commands before or after SceneKit draws its own content.

This property is valid only during the SceneKit rendering loop—that is, within one of the methods defined in the [`SCNSceneRendererDelegate`](../scnscenerendererdelegate.md) protocol. Accessing this property at any other time returns `nil`.

## See Also

### Customizing Scene Rendering with Metal
- [var device: (any MTLDevice)?](./device.md)
  The Metal device this renderer uses for rendering.
- [var commandQueue: (any MTLCommandQueue)?](./commandqueue.md)
  The Metal command queue this renderer uses for rendering.
- [var colorPixelFormat: MTLPixelFormat](./colorpixelformat.md)
  The Metal pixel format for the renderer’s color output.
- [var depthPixelFormat: MTLPixelFormat](./depthpixelformat.md)
  The Metal pixel format for the renderer’s depth buffer.
- [var stencilPixelFormat: MTLPixelFormat](./stencilpixelformat.md)
  The Metal pixel format for the renderer’s stencil buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnscenerenderer/currentrendercommandencoder)*