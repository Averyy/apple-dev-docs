# camera

**Framework**: SpriteKit  
**Kind**: property

The camera node in the scene that determines what part of the scene’s coordinate space is visible in the view.

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
@MainActor
weak var camera: SKCameraNode? { get set }
```

## Mentions

- [Positioning a Scene’s Origin Within its View](positioning-a-scene-s-origin-within-its-view.md)
- [Getting Started with a Camera](getting-started-with-a-camera.md)

#### Discussion

The default value of this property is `nil`, which means that the scene’s [`anchorPoint`](skscene/anchorpoint.md) and [`size`](skscene/size.md) properties determine what portion of the scene is visible. If set to point to a camera node contained in the scene, the [`anchorPoint`](skscene/anchorpoint.md) property is ignored and the scene is rendered using the camera node’s properties instead.

A camera must be added as a child of the scene for it to render that scene.

Listing 1 shows, in Swift, how to add a camera to an [`SKScene`](skscene.md) named `scene`. The camera is positioned in the center of the scene which gives the same result as rendering a camera-less scene with an [`anchorPoint`](skscene/anchorpoint.md) of [`zero`](https://developer.apple.com/documentation/CoreFoundation/CGPoint/zero).

Listing 1. Adding a camera to a scene

```swift
let cameraNode = SKCameraNode()
    
cameraNode.position = CGPoint(x: scene.size.width / 2,
                              y: scene.size.height / 2)
    
scene.addChild(cameraNode)
scene.camera = cameraNode
```

For more information, see [`SKCameraNode`](skcameranode.md).

## See Also

- [Positioning a Scene’s Origin Within its View](positioning-a-scene-s-origin-within-its-view.md)
  Try the different ways to configure the scene’s origin inside its view.
- [var anchorPoint: CGPoint](skscene/anchorpoint.md)
  The point in the view’s frame that corresponds to the scene’s origin.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skscene/camera)*