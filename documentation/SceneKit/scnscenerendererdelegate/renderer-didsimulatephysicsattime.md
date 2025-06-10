# renderer(_:didSimulatePhysicsAtTime:)

**Framework**: SceneKit  
**Kind**: method

Tells the delegate to perform any updates that need to occur after physics simulations are performed.

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
optional func renderer(_ renderer: any SCNSceneRenderer, didSimulatePhysicsAtTime time: TimeInterval)
```

#### Discussion

SceneKit calls this method exactly once per frame, so long as the [`SCNView`](scnview.md) object (or other [`SCNSceneRenderer`](scnscenerenderer.md) object) displaying the scene is not paused.

Implement this method to add game logic to the rendering loop. Any changes you make to the scene graph during this method are immediately reflected in the displayed scene. That is, SceneKit immediately updates the hierarchy of presentation nodes it uses to render the scene (instead of using the [`SCNTransaction`](scntransaction.md) class to “batch” your changes).

This method is the last opportunity SceneKit provides for you to change the scene graph before rendering.

## Parameters

- `renderer`: The SceneKit object responsible for rendering the scene.
- `time`: The current system time, in seconds. Use this parameter for any time-based elements of your game logic.

## See Also

- [func renderer(any SCNSceneRenderer, updateAtTime: TimeInterval)](scnscenerendererdelegate/renderer(_:updateattime:).md)
  Tells the delegate to perform any updates that need to occur before actions, animations, and physics are evaluated.
- [func renderer(any SCNSceneRenderer, didApplyAnimationsAtTime: TimeInterval)](scnscenerendererdelegate/renderer(_:didapplyanimationsattime:).md)
  Tells the delegate to perform any updates that need to occur after actions and animations are evaluated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnscenerendererdelegate/renderer(_:didsimulatephysicsattime:))*