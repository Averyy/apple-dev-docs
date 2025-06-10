# scene

**Framework**: SceneKit  
**Kind**: property  
**Required**: Yes

The scene to be displayed.

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
var scene: SCNScene? { get set }
```

#### Discussion

Setting a new scene immediately replaces whatever scene the renderer was previously displaying. To display a transition between scenes, use the [`present(_:with:incomingPointOfView:completionHandler:)`](scnscenerenderer/present(_:with:incomingpointofview:completionhandler:).md) method.

## See Also

- [func present(SCNScene, with: SKTransition, incomingPointOfView: SCNNode?, completionHandler: (() -> Void)?)](scnscenerenderer/present(_:with:incomingpointofview:completionhandler:).md)
  Displays the specified scene with an animated transition.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnscenerenderer/scene)*