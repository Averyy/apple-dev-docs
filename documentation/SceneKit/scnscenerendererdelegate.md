# SCNSceneRendererDelegate

**Framework**: SceneKit  
**Kind**: protocol

Methods your app can implement to participate in SceneKit’s animation loop or perform additional rendering.

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
protocol SCNSceneRendererDelegate : NSObjectProtocol
```

#### Overview

To build an app or game with SceneKit, you use an [`SCNView`](scnview.md) object (or other object conforming the [`SCNSceneRenderer`](scnscenerenderer.md) protocol) to display your scene. Then, to add per-frame game logic, or to perform custom Metal or OpenGL rendering before or after SceneKit renders the scene, specify your own custom object that implements the [`SCNSceneRendererDelegate`](scnscenerendererdelegate.md) protocol for the view’s [`delegate`](scnscenerenderer/delegate.md) property.

When rendering your scene, an [`SCNView`](scnview.md) object (or other SceneKit renderer) runs a rendering loop that processes and then draws the scene. [`SCNSceneRendererDelegate`](scnscenerendererdelegate.md) shows the steps in this loop.

![None](https://docs-assets.developer.apple.com/published/3f3d7914795ccd9d65d70c7d530f2083/media-2929793%402x.png)

Each time through the rendering loop, a SceneKit view (or renderer) executes the following actions in order:

1. The view calls its delegate’s [`renderer(_:updateAtTime:)`](scnscenerendererdelegate/renderer(_:updateattime:).md) method.
2. SceneKit executes actions and performs animations attached to the scene graph. (See the [`SCNAction`](scnaction.md) class and [`SCNAnimatable`](scnanimatable.md) protocol.)
3. The view calls its delegate’s [`renderer(_:didApplyAnimationsAtTime:)`](scnscenerendererdelegate/renderer(_:didapplyanimationsattime:).md) method.
4. SceneKit applies its physics simulation to any physics bodies in the scene. (See [`SCNPhysicsWorld`](scnphysicsworld.md), [`SCNPhysicsBody`](scnphysicsbody.md), and related classes.)
5. The view calls its delegate’s [`renderer(_:didSimulatePhysicsAtTime:)`](scnscenerendererdelegate/renderer(_:didsimulatephysicsattime:).md) method.
6. The view calls its delegate’s [`renderer(_:willRenderScene:atTime:)`](scnscenerendererdelegate/renderer(_:willrenderscene:attime:).md) method.
7. SceneKit renders the scene graph in the view.
8. The view calls its delegate’s [`renderer(_:didRenderScene:atTime:)`](scnscenerendererdelegate/renderer(_:didrenderscene:attime:).md) method.

##### Working with the Rendering Loop

When building a game, you typically need to run logic relating to gameplay before each frame of animation. Game logic may include input handling, artificial intelligence, game scripting, or other tasks. Often, the results of this logic involve making changes to nodes or running actions on nodes.

The methods listed in [`SCNSceneRendererDelegate`](scnscenerendererdelegate.md) provide places to implement your game logic. Which of these methods you implement for which tasks depends on your game design. For example, if your game uses physics, you might implement the [`renderer(_:didSimulatePhysicsAtTime:)`](scnscenerendererdelegate/renderer(_:didsimulatephysicsattime:).md) method to decide whether the player has won the game based on the state of physics bodies in the scene. If your gameplay isn’t based on the physics simulation, you might make such decisions in the [`renderer(_:updateAtTime:)`](scnscenerendererdelegate/renderer(_:updateattime:).md) method instead.

##### Custom Rendering

If you want to perform custom rendering before or after SceneKit renders the contents of the scene, implement one or both methods listed in [`SCNSceneRendererDelegate`](scnscenerendererdelegate.md). These methods are appropriate for custom Metal or OpenGL drawing that does not depend on the structure or content of the scene graph. If you instead want to render a special effect that is attached to a specific location in the scene, see [`SCNNodeRendererDelegate`](scnnoderendererdelegate.md). Or if you want to use GPU shader programs to customize SceneKit’s rendering of scene content, see [`SCNShadable`](scnshadable.md).

## Topics

### Adding Custom Logic to the Rendering Loop
- [func renderer(any SCNSceneRenderer, updateAtTime: TimeInterval)](scnscenerendererdelegate/renderer(_:updateattime:).md)
  Tells the delegate to perform any updates that need to occur before actions, animations, and physics are evaluated.
- [func renderer(any SCNSceneRenderer, didApplyAnimationsAtTime: TimeInterval)](scnscenerendererdelegate/renderer(_:didapplyanimationsattime:).md)
  Tells the delegate to perform any updates that need to occur after actions and animations are evaluated.
- [func renderer(any SCNSceneRenderer, didSimulatePhysicsAtTime: TimeInterval)](scnscenerendererdelegate/renderer(_:didsimulatephysicsattime:).md)
  Tells the delegate to perform any updates that need to occur after physics simulations are performed.
### Rendering Custom Scene Content
- [func renderer(any SCNSceneRenderer, willRenderScene: SCNScene, atTime: TimeInterval)](scnscenerendererdelegate/renderer(_:willrenderscene:attime:).md)
  Tells the delegate that the renderer has cleared the viewport and is about to render the scene.
- [func renderer(any SCNSceneRenderer, didRenderScene: SCNScene, atTime: TimeInterval)](scnscenerendererdelegate/renderer(_:didrenderscene:attime:).md)
  Tells the delegate that the renderer has rendered the scene.
### Instance Methods
- [func renderer(any SCNSceneRenderer, didApplyConstraintsAtTime: TimeInterval)](scnscenerendererdelegate/renderer(_:didapplyconstraintsattime:).md)

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [protocol SCNSceneRenderer](scnscenerenderer.md)
  Methods and properties common to the [`SCNView`](scnview.md), [`SCNLayer`](scnlayer.md), and [`SCNRenderer`](scnrenderer.md) classes.
- [class SCNLayer](scnlayer.md)
  A Core Animation layer that renders a SceneKit scene as its content.
- [class SCNRenderer](scnrenderer.md)
  A renderer for displaying a SceneKit scene in an existing Metal workflow or OpenGL context.
- [class SCNHitTestResult](scnhittestresult.md)
  Information about the result of a scene-space or view-space search for scene elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnscenerendererdelegate)*