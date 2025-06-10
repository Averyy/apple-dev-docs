# morpher

**Framework**: SceneKit  
**Kind**: property

The morpher object responsible for blending the node’s geometry.

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
var morpher: SCNMorpher? { get set }
```

#### Discussion

You use a morpher object to interpolate between multiple geometries. For details, see [`SCNMorpher`](scnmorpher.md).

## See Also

- [var name: String?](scnnode/name.md)
  A name associated with the node.
- [var light: SCNLight?](scnnode/light.md)
  The light attached to the node.
- [var camera: SCNCamera?](scnnode/camera.md)
  The camera attached to the node.
- [var geometry: SCNGeometry?](scnnode/geometry.md)
  The geometry attached to the node.
- [var skinner: SCNSkinner?](scnnode/skinner.md)
  The skinner object responsible for skeletal animations of node’s contents.
- [var categoryBitMask: Int](scnnode/categorybitmask.md)
  A mask that defines which categories the node belongs to.
- [protocol SCNBoundingVolume](scnboundingvolume.md)
  Methods common to the [`SCNNode`](scnnode.md) and [`SCNGeometry`](scngeometry.md) classes for measuring location and size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnnode/morpher)*