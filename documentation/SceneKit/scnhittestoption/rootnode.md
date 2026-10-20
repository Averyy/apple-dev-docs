# rootNode

**Framework**: SceneKit  
**Kind**: property  
**Role**: Type Property

The root of the node hierarchy to be searched.

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
static let rootNode: SCNHitTestOption
```

```c
extern SCNHitTestOption const SCNHitTestRootNodeKey;
```

#### Discussion

The value for this key is an [`SCNNode`](../scnnode.md) object. Hit-testing searches only the child node hierarchy under this node. When hit-testing takes place in the screen space of an [`SCNSceneRenderer`](../scnscenerenderer.md) object with the [`hitTest(_:options:)`](../scnscenerenderer/hittest%28_,options%29.md) method, the default value is the presented scene’s root node. When hit-testing is in a node using its [`hitTestWithSegment(from:to:options:)`](../scnnode/hittestwithsegment%28from,to,options%29.md), the default value is the node.

## See Also

### Options
- [static let backFaceCulling: SCNHitTestOption](./backfaceculling.md)
  An option to ignore faces not oriented toward the camera.
- [static let boundingBoxOnly: SCNHitTestOption](./boundingboxonly.md)
  An option to search for objects by bounding box only.
- [static let categoryBitMask: SCNHitTestOption](./categorybitmask.md)
  An option to search only for objects matching a specified bitmask.
- [static let clipToZRange: SCNHitTestOption](./cliptozrange.md)
  An option to search for objects only within the depth range of the current point of view.
- [static let ignoreChildNodes: SCNHitTestOption](./ignorechildnodes.md)
  An option to ignore child nodes when searching.
- [static let ignoreHiddenNodes: SCNHitTestOption](./ignorehiddennodes.md)
  An option to ignore hidden nodes when searching.
- [static let searchMode: SCNHitTestOption](./searchmode.md)
  An option for the number and order of hit test results to provide.
- [enum SCNHitTestSearchMode](../scnhittestsearchmode.md)
  Possible values for the [`searchMode`](./searchmode.md) option used with hit-testing methods.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnhittestoption/rootnode)*