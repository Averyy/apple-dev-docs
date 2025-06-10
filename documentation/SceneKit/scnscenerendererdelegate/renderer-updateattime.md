# renderer(_:updateAtTime:)

**Framework**: SceneKit  
**Kind**: method

Tells the delegate to perform any updates that need to occur before actions, animations, and physics are evaluated.

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
optional func renderer(_ renderer: any SCNSceneRenderer, updateAtTime time: TimeInterval)
```

#### Discussion

SceneKit calls this method exactly once per frame, so long as the [`SCNView`](scnview.md) object (or other [`SCNSceneRenderer`](scnscenerenderer.md) object) displaying the scene is not paused.

Implement this method to add game logic to the rendering loop. Any changes you make to the scene graph during this method are immediately reflected in the displayed scene. That is, SceneKit immediately updates the hierarchy of presentation nodes it uses to render the scene (instead of using the [`SCNTransaction`](scntransaction.md) class to “batch” your changes).

## Parameters

- `renderer`: The SceneKit object responsible for rendering the scene.
- `time`: The current system time, in seconds. Use this parameter for any time-based elements of your game logic.

## See Also

- [func renderer(any SCNSceneRenderer, didApplyAnimationsAtTime: TimeInterval)](scnscenerendererdelegate/renderer(_:didapplyanimationsattime:).md)
  Tells the delegate to perform any updates that need to occur after actions and animations are evaluated.
- [func renderer(any SCNSceneRenderer, didSimulatePhysicsAtTime: TimeInterval)](scnscenerendererdelegate/renderer(_:didsimulatephysicsattime:).md)
  Tells the delegate to perform any updates that need to occur after physics simulations are performed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnscenerendererdelegate/renderer(_:updateattime:))*