# SCNRenderer

**Framework**: SceneKit  
**Kind**: class

A renderer for displaying a SceneKit scene in an existing Metal workflow or OpenGL context.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
class SCNRenderer
```

#### Overview

Use this class when you want to add content rendered by SceneKit to an app that already renders other content by using Metal, OpenGL, or OpenGL ES directly. To provide content for a SceneKit renderer, assign a [`SCNScene`](scnscene.md) object to its [`scene`](scnrenderer/scene.md) property.

For additional important methods and properties for working with SceneKit renderers, see [`SCNSceneRenderer`](scnscenerenderer.md).

## Topics

### Creating a Renderer
- [convenience init(device: (any MTLDevice)?, options: [AnyHashable : Any]?)](scnrenderer/init(device:options:).md)
  Creates a renderer with the specified Metal device.
- [convenience init(context: EAGLContext?, options: [AnyHashable : Any]?)](scnrenderer/init(context:options:).md)
  Creates a renderer with the specified OpenGL context.
### Specifying a Scene
- [var scene: SCNScene?](scnrenderer/scene.md)
  The scene to be rendered.
### Managing Animation Timing
- [var nextFrameTime: CFTimeInterval](scnrenderer/nextframetime.md)
  The timestamp for the next frame to be rendered.
### Rendering a Scene Using Metal
- [func render(atTime: CFTimeInterval, viewport: CGRect, commandBuffer: any MTLCommandBuffer, passDescriptor: MTLRenderPassDescriptor)](scnrenderer/render(attime:viewport:commandbuffer:passdescriptor:).md)
  Renders the scene’s contents at the specified system time in the specified Metal command buffer.
### Rendering a Scene Using OpenGL
- [func render()](scnrenderer/render.md)
  Renders the scene’s contents in the renderer’s OpenGL context.
- [func render(atTime: CFTimeInterval)](scnrenderer/render(attime:).md)
  Renders the scene’s contents at the specified system time in the renderer’s OpenGL context.
### Capturing a Snapshot
- [func snapshot(atTime: CFTimeInterval, with: CGSize, antialiasingMode: SCNAntialiasingMode) -> UIImage](scnrenderer/snapshot(attime:with:antialiasingmode:).md)
  Creates an image by drawing the renderer’s content at the specified system time.
### Instance Methods
- [func render(withViewport: CGRect, commandBuffer: any MTLCommandBuffer, passDescriptor: MTLRenderPassDescriptor)](scnrenderer/render(withviewport:commandbuffer:passdescriptor:).md)
- [func update(atTime: CFTimeInterval)](scnrenderer/update(attime:).md)
- [func updateProbes([SCNNode], atTime: CFTimeInterval)](scnrenderer/updateprobes(_:attime:).md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [SCNSceneRenderer](scnscenerenderer.md)
- [SCNTechniqueSupport](scntechniquesupport.md)

## See Also

- [protocol SCNSceneRenderer](scnscenerenderer.md)
  Methods and properties common to the [`SCNView`](scnview.md), [`SCNLayer`](scnlayer.md), and [`SCNRenderer`](scnrenderer.md) classes.
- [protocol SCNSceneRendererDelegate](scnscenerendererdelegate.md)
  Methods your app can implement to participate in SceneKit’s animation loop or perform additional rendering.
- [class SCNLayer](scnlayer.md)
  A Core Animation layer that renders a SceneKit scene as its content.
- [class SCNHitTestResult](scnhittestresult.md)
  Information about the result of a scene-space or view-space search for scene elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnrenderer)*