# light

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

The light attached to the node.

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
var light: SCNLight? { get set }
```

```objc
@property (nonatomic, retain, nullable) SCNLight * light;
```

#### Discussion

A node can have only one light attached to it. To combine lights so they can be controlled or animated together, create a node with no light and add other nodes to it.

## See Also

### Managing Node Content
- [var name: String?](./name.md)
  A name associated with the node.
- [var camera: SCNCamera?](./camera.md)
  The camera attached to the node.
- [var geometry: SCNGeometry?](./geometry.md)
  The geometry attached to the node.
- [var morpher: SCNMorpher?](./morpher.md)
  The morpher object responsible for blending the node’s geometry.
- [var skinner: SCNSkinner?](./skinner.md)
  The skinner object responsible for skeletal animations of node’s contents.
- [var categoryBitMask: Int](./categorybitmask.md)
  A mask that defines which categories the node belongs to.
- [protocol SCNBoundingVolume](../scnboundingvolume.md)
  Methods common to the [`SCNNode`](../scnnode.md) and [`SCNGeometry`](../scngeometry.md) classes for measuring location and size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnnode/light)*