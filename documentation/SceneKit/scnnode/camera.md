# camera

**Framework**: SceneKit  
**Kind**: property

The camera attached to the node.

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
var camera: SCNCamera? { get set }
```

#### Discussion

To use a camera for displaying a scene, set the the [`pointOfView`](scnscenerenderer/pointofview.md) property of the view (or layer or renderer) displaying the scene to the node containing the camera. A camera looks in the direction of the node’s negative z-axis, so you aim the camera by changing the position and orientation of the node containing it. You control geometric and optical parameters of the camera—projection, field of view, and depth of field—using the attached [`SCNCamera`](scncamera.md) object.

## See Also

- [var name: String?](scnnode/name.md)
  A name associated with the node.
- [var light: SCNLight?](scnnode/light.md)
  The light attached to the node.
- [var geometry: SCNGeometry?](scnnode/geometry.md)
  The geometry attached to the node.
- [var morpher: SCNMorpher?](scnnode/morpher.md)
  The morpher object responsible for blending the node’s geometry.
- [var skinner: SCNSkinner?](scnnode/skinner.md)
  The skinner object responsible for skeletal animations of node’s contents.
- [var categoryBitMask: Int](scnnode/categorybitmask.md)
  A mask that defines which categories the node belongs to.
- [protocol SCNBoundingVolume](scnboundingvolume.md)
  Methods common to the [`SCNNode`](scnnode.md) and [`SCNGeometry`](scngeometry.md) classes for measuring location and size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnnode/camera)*