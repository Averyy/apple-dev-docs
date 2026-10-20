# present(_:with:incomingPointOfView:completionHandler:)

**Framework**: SceneKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Displays the specified scene with an animated transition.

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
func present(_ scene: SCNScene, with transition: SKTransition, incomingPointOfView pointOfView: SCNNode?, completionHandler: (@Sendable () -> Void)? = nil)
```

```swift
func present(_ scene: SCNScene, with transition: SKTransition, incomingPointOfView pointOfView: SCNNode?) async
```

```objc
- (void) presentScene:(SCNScene *) scene withTransition:(SKTransition *) transition incomingPointOfView:(SCNNode *) pointOfView completionHandler:(void (^)()) completionHandler;
```

#### Discussion

Use this method to change the scene displayed in a SceneKit view (or other renderer) with an animated transition. For details on transition styles, see [`SKTransition`](../../SpriteKit/sktransition.md).

## Parameters

- `scene`: The new scene to be displayed.
- `transition`: An object that specifies the duration and style of the animated transition.
- `pointOfView`: The node to use as the [`pointOfView`](./pointofview.md) property when displaying the new scene.
- `completionHandler`: A block that SceneKit calls after the transition animation has completed.

  This block takes no parameters and has no return value.

## See Also

### Presenting a Scene
- [var scene: SCNScene?](./scene.md)
  The scene to be displayed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnscenerenderer/present(_:with:incomingpointofview:completionhandler:))*