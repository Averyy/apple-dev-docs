# present(_:with:incomingPointOfView:completionHandler:)

**Framework**: SceneKit  
**Kind**: method  
**Required**: Yes

Displays the specified scene with an animated transition.

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
func present(_ scene: SCNScene, with transition: SKTransition, incomingPointOfView pointOfView: SCNNode?) async
```

#### Discussion

Use this method to change the scene displayed in a SceneKit view (or other renderer) with an animated transition. For details on transition styles, see [`SKTransition`](https://developer.apple.com/documentation/SpriteKit/SKTransition).

## Parameters

- `scene`: The new scene to be displayed.
- `transition`: An object that specifies the duration and style of the animated transition.
- `pointOfView`: The node to use as the   property when displaying the new scene.
- `completionHandler`: This block takes no parameters and has no return value.

## See Also

- [var scene: SCNScene?](scnscenerenderer/scene.md)
  The scene to be displayed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnscenerenderer/present(_:with:incomingpointofview:completionhandler:))*