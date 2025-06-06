# rootNode

**Framework**: SceneKit  
**Kind**: property

The root node of the scene graph.

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
var rootNode: SCNNode { get }
```

#### Discussion

All scene content—nodes, geometries and their materials, lights, cameras, and related objects—is organized in a node hierarchy with a single common root node.

Some scene files created using external tools may describe node hierarchies containing multiple root nodes. When SceneKit imports such files, their separate root nodes will be made children of a new, unique root node.

Each child node’s coordinate system is defined relative to the transformation of its parent node. You should not modify the [`transform`](scnnode/transform.md) property of the root node.

## See Also

- [var background: SCNMaterialProperty](scnscene/background.md)
  A background to be rendered before the rest of the scene.
- [var lightingEnvironment: SCNMaterialProperty](scnscene/lightingenvironment.md)
  A cube map texture that depicts the environment surrounding the scene’s contents, used for advanced lighting effects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnscene/rootnode)*