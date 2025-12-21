# pointOfView

**Framework**: SpriteKit  
**Kind**: property

The Scene Kit node from which the scene’s contents are viewed when rendered.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var pointOfView: SCNNode? { get set }
```

#### Discussion

Use a [`SCNNode`](https://developer.apple.com/documentation/SceneKit/SCNNode) object with an [`SCNCamera`](https://developer.apple.com/documentation/SceneKit/SCNCamera) instance assigned to its [`camera`](https://developer.apple.com/documentation/SceneKit/SCNNode/camera) property to view a scene. This SceneKit node provides the position and direction of a virtual camera, and the camera object provides rendering parameters such as field of view and focus. The direction of view is along the negative z-axis of the SceneKit node’s local coordinate space.

## See Also

- [var viewportSize: CGSize](sk3dnode/viewportsize.md)
  The size of the image rendered by the node.
- [var scnScene: SCNScene?](sk3dnode/scnscene.md)
  The SceneKit scene to render.
- [var autoenablesDefaultLighting: Bool](sk3dnode/autoenablesdefaultlighting.md)
  A Boolean value that determines whether Scene Kit automatically adds lights to a scene.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/sk3dnode/pointofview)*