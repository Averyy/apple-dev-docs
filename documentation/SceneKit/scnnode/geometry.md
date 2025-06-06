# geometry

**Framework**: SceneKit  
**Kind**: property

The geometry attached to the node.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
var geometry: SCNGeometry? { get set }
```

#### Discussion

A node can have only one geometry attached to it. To combine geometries so they can be controlled or animated together, create a node with no geometry and add other nodes to it.

Animating the node’s geometric properties can move, rotate, stretch and scale its geometry. For more advanced animations of a node’s geometry, use its [`morpher`](scnnode/morpher.md) and [`skinner`](scnnode/skinner.md) objects.

## See Also

- [var name: String?](scnnode/name.md)
  A name associated with the node.
- [var light: SCNLight?](scnnode/light.md)
  The light attached to the node.
- [var camera: SCNCamera?](scnnode/camera.md)
  The camera attached to the node.
- [var morpher: SCNMorpher?](scnnode/morpher.md)
  The morpher object responsible for blending the node’s geometry.
- [var skinner: SCNSkinner?](scnnode/skinner.md)
  The skinner object responsible for skeletal animations of node’s contents.
- [var categoryBitMask: Int](scnnode/categorybitmask.md)
  A mask that defines which categories the node belongs to.
- [protocol SCNBoundingVolume](scnboundingvolume.md)
  Methods common to the [`SCNNode`](scnnode.md) and [`SCNGeometry`](scngeometry.md) classes for measuring location and size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnnode/geometry)*