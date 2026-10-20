# skinner

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

The skinner object responsible for skeletal animations of node’s contents.

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
var skinner: SCNSkinner? { get set }
```

```objc
@property (nonatomic, retain, nullable) SCNSkinner * skinner;
```

#### Discussion

A skinner object maintains an hierarchy of control nodes that can deform the node’s geometry using skeletal animations created in an external 3D authoring tool. For details, see [`SCNSkinner`](../scnskinner.md).

## See Also

### Managing Node Content
- [var name: String?](./name.md)
  A name associated with the node.
- [var light: SCNLight?](./light.md)
  The light attached to the node.
- [var camera: SCNCamera?](./camera.md)
  The camera attached to the node.
- [var geometry: SCNGeometry?](./geometry.md)
  The geometry attached to the node.
- [var morpher: SCNMorpher?](./morpher.md)
  The morpher object responsible for blending the node’s geometry.
- [var categoryBitMask: Int](./categorybitmask.md)
  A mask that defines which categories the node belongs to.
- [protocol SCNBoundingVolume](../scnboundingvolume.md)
  Methods common to the [`SCNNode`](../scnnode.md) and [`SCNGeometry`](../scngeometry.md) classes for measuring location and size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnnode/skinner)*