# delegate

**Framework**: SceneKit  
**Kind**: property  
**Required**: Yes

A delegate object that receives messages about SceneKit’s rendering process.

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
weak var delegate: (any SCNSceneRendererDelegate)? { get set }
```

#### Discussion

A scene renderer delegate is a custom object that you provide. When SceneKit processes the scene for rendering each frame of animation, it notifies the delegate after significant steps in the update-and-render process. There are two primary uses for a scene renderer delegate:

- Implementing per-frame game logic. Use delegate methods to update the state of your game objects and modify the scene graph in response, either at the beginning of SceneKit’s rendering process for each frame, or after SceneKit has processed actions and animations or run the physics simulation for the scene.
- Performing custom rendering. Use a scene renderer delegate to draw your own content using Metal or OpenGL, either before SceneKit renders the scene’s contents (as a backdrop) or afterward (as an overlay).

This rendering is independent of the scene graph and its contents. If you instead want to perform custom rendering that is anchored at a location in the scene’s coordinate space, use the [`rendererDelegate`](scnnode/rendererdelegate.md) property of an [`SCNNode`](scnnode.md) object in the scene graph. Or if you want to customize the rendering of SceneKit’s geometries and materials, use the [`SCNShadable`](scnshadable.md) protocol to attach GPU shaders to SceneKit objects.

For details, see [`SCNSceneRendererDelegate`](scnscenerendererdelegate.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnscenerenderer/delegate)*