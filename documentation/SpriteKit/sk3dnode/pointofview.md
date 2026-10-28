# pointOfView

**Framework**: SpriteKit  
**Kind**: property  
**Role**: Instance Property

The Scene Kit node from which the scene’s contents are viewed when rendered.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var pointOfView: SCNNode? { get set }
```

```objc
@property (nonatomic, retain, nullable) SCNNode * pointOfView;
```

## Discussion

Use a [`SCNNode`](../../SceneKit/scnnode.md) object with an [`SCNCamera`](../../SceneKit/scncamera.md) instance assigned to its [`camera`](../../SceneKit/scnnode/camera.md) property to view a scene. This SceneKit node provides the position and direction of a virtual camera, and the camera object provides rendering parameters such as field of view and focus. The direction of view is along the negative z-axis of the SceneKit node’s local coordinate space.

## See Also

### Configuring a 3D Node
- [var viewportSize: CGSize](./viewportsize.md)
  The size of the image rendered by the node.
- [var scnScene: SCNScene?](./scnscene.md)
  The SceneKit scene to render.
- [var autoenablesDefaultLighting: Bool](./autoenablesdefaultlighting.md)
  A Boolean value that determines whether Scene Kit automatically adds lights to a scene.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/sk3dnode/pointofview)*