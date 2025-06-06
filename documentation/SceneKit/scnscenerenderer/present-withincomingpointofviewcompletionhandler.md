# present(_:with:incomingPointOfView:completionHandler:)

**Framework**: SceneKit  
**Kind**: method  
**Required**: Yes

Displays the specified scene with an animated transition.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func present(_ scene: SCNScene, with transition: SKTransition, incomingPointOfView pointOfView: SCNNode?) async
```

#### Discussion

> **Note**:  In Swift, you can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration: ```swift
func present(_ scene: SCNScene, with transition: SKTransition, incomingPointOfView pointOfView: SCNNode?) async
``` For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

 In Swift, you can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration:

```swift
func present(_ scene: SCNScene, with transition: SKTransition, incomingPointOfView pointOfView: SCNNode?) async
```

For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

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