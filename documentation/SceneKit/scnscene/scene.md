# scene

**Framework**: SceneKit  
**Kind**: method  
**Role**: Type Method

Creates and returns an empty scene.

**Availability**:
- iOS 8.0+ - Deprecated in 26.0
- iPadOS 8.0+ - Deprecated in 26.0
- Mac Catalyst 13.1+ - Deprecated in 26.0
- macOS 10.8+ - Deprecated in 26.0
- tvOS 9.0+ - Deprecated in 26.0
- visionOS 1.0+ - Deprecated in 26.0
- watchOS 3.0+ - Deprecated in 26.0

## Declaration

```objc
+ (instancetype) scene;
```

#### Return Value

A new, empty scene object.

#### Discussion

An empty scene contains only a root [`SCNNode`](../scnnode.md) object with no contents. To populate the scene, add children to the root node.

## See Also

### Related Documentation
- [var rootNode: SCNNode](./rootnode.md)
  The root node of the scene graph.
### Creating a Scene from a File
- [convenience init?(named: String)](./init%28named%29.md)
  Loads a scene from a file with the specified name in the app’s main bundle.
- [convenience init?(named: String, inDirectory: String?, options: [SCNSceneSource.LoadingOption : Any]?)](./init%28named,indirectory,options%29.md)
  Loads a scene from a file with the specified name in a specific subdirectory of the app’s main bundle.
- [convenience init(url: URL, options: [SCNSceneSource.LoadingOption : Any]?) throws](./init%28url,options%29-7ugvv.md)
  Loads a scene from the specified URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnscene/scene)*