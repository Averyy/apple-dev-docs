# name

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

A name associated with the node.

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
var name: String? { get set }
```

```objc
@property (nonatomic, copy, nullable) NSString * name;
```

## Discussion

You can provide a descriptive name for a node to make managing your scene graph easier. Nodes loaded from a scene file may have names assigned by an artist using a 3D authoring tool. Use the [`childNode(withName:recursively:)`](./childnode%28withname,recursively%29.md) or [`childNodes(passingTest:)`](./childnodes%28passingtest%29.md) method to retrieve a node from a scene graph by its name, or the [`SCNSceneSource`](../scnscenesource.md) class to examine nodes in a scene file without loading its scene graph.

The names of nodes and their attached objects are saved when you export a scene to a file using its [`write(to:options:delegate:progressHandler:)`](../scnscene/write%28to,options,delegate,progresshandler%29.md) method, and appear in the Xcode scene editor. The SceneKit statistics view (see [`showsStatistics`](../scnscenerenderer/showsstatistics.md)) also shows the names of nodes with attached cameras.

## See Also

### Related Documentation
- [func childNodes(passingTest: (SCNNode, UnsafeMutablePointer<ObjCBool>) -> Bool) -> [SCNNode]](./childnodes%28passingtest%29.md)
  Returns all nodes in the node’s child node subtree that satisfy the test applied by a block.
- [func childNode(withName: String, recursively: Bool) -> SCNNode?](./childnode%28withname,recursively%29.md)
  Returns the first node in the node’s child node subtree with the specified name.
### Managing Node Content
- [var light: SCNLight?](./light.md)
  The light attached to the node.
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

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnnode/name)*