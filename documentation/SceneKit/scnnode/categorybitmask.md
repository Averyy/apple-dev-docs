# categoryBitMask

**Framework**: SceneKit  
**Kind**: property

A mask that defines which categories the node belongs to.

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
var categoryBitMask: Int { get set }
```

#### Discussion

You can assign each node in a scene to one or more categories, where each category corresponds to a bit in the bit mask. You define the mask values used in your app. When SceneKit renders a scene, it compares each node’s [`categoryBitMask`](scnnode/categorybitmask.md) property with the category bit masks of every other object that participates in the rendering process—lights, cameras, and techniques—using a bitwise AND operation. If the result is a nonzero value, SceneKit includes the node when rendering. The default category bit mask is `1`.

Use a node’s category bit mask together with:

- An [`SCNLight`](scnlight.md) object’s [`categoryBitMask`](scnlight/categorybitmask.md) property to exclude the node from that light’s illumination
- An [`SCNCamera`](scncamera.md) object’s [`categoryBitMask`](scncamera/categorybitmask.md) property to make the node invisible to that camera
- The category bit masks in an [`SCNTechnique`](scntechnique.md) object’s definition dictionary to include or exclude the node from phases of a multipass rendering technique

> **Note**:  This property doesn’t affect SceneKit’s physics simulation. To include or exclude a node from physics interactions, use the [`categoryBitMask`](scnphysicsbody/categorybitmask.md) property of the node’s [`physicsBody`](scnnode/physicsbody.md) and [`physicsField`](scnnode/physicsfield.md) objects.

## See Also

- [var name: String?](scnnode/name.md)
  A name associated with the node.
- [var light: SCNLight?](scnnode/light.md)
  The light attached to the node.
- [var camera: SCNCamera?](scnnode/camera.md)
  The camera attached to the node.
- [var geometry: SCNGeometry?](scnnode/geometry.md)
  The geometry attached to the node.
- [var morpher: SCNMorpher?](scnnode/morpher.md)
  The morpher object responsible for blending the node’s geometry.
- [var skinner: SCNSkinner?](scnnode/skinner.md)
  The skinner object responsible for skeletal animations of node’s contents.
- [protocol SCNBoundingVolume](scnboundingvolume.md)
  Methods common to the [`SCNNode`](scnnode.md) and [`SCNGeometry`](scngeometry.md) classes for measuring location and size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnnode/categorybitmask)*