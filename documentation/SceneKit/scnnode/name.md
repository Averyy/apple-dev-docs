# name

**Framework**: SceneKit  
**Kind**: property

A name associated with the node.

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
var name: String? { get set }
```

#### Discussion

You can provide a descriptive name for a node to make managing your scene graph easier. Nodes loaded from a scene file may have names assigned by an artist using a 3D authoring tool. Use the [`childNode(withName:recursively:)`](scnnode/childnode(withname:recursively:).md) or [`childNodes(passingTest:)`](scnnode/childnodes(passingtest:).md) method to retrieve a node from a scene graph by its name, or the [`SCNSceneSource`](scnscenesource.md) class to examine nodes in a scene file without loading its scene graph.

The names of nodes and their attached objects are saved when you export a scene to a file using its [`write(to:options:delegate:progressHandler:)`](scnscene/write(to:options:delegate:progresshandler:).md) method, and appear in the Xcode scene editor. The SceneKit statistics view (see [`showsStatistics`](scnscenerenderer/showsstatistics.md)) also shows the names of nodes with attached cameras.

## See Also

- [func childNodes(passingTest: (SCNNode, UnsafeMutablePointer<ObjCBool>) -> Bool) -> [SCNNode]](scnnode/childnodes(passingtest:).md)
  Returns all nodes in the node’s child node subtree that satisfy the test applied by a block.
- [func childNode(withName: String, recursively: Bool) -> SCNNode?](scnnode/childnode(withname:recursively:).md)
  Returns the first node in the node’s child node subtree with the specified name.
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
- [var categoryBitMask: Int](scnnode/categorybitmask.md)
  A mask that defines which categories the node belongs to.
- [protocol SCNBoundingVolume](scnboundingvolume.md)
  Methods common to the [`SCNNode`](scnnode.md) and [`SCNGeometry`](scngeometry.md) classes for measuring location and size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnnode/name)*