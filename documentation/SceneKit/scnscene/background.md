# background

**Framework**: SceneKit  
**Kind**: property

A background to be rendered before the rest of the scene.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
var background: SCNMaterialProperty { get }
```

#### Discussion

If the material property’s [`contents`](scnmaterialproperty/contents.md) object is `nil`, SceneKit does not draw any background before drawing the rest of the scene. (If the scene is presented in an [`SCNView`](scnview.md) instance, the view’s background color is visible behind the contents of the scene.)

If you specify a cube map texture for the material property (see the discussion of the [`contents`](scnmaterialproperty/contents.md) property), SceneKit renders the background as a skybox.

## See Also

- [var rootNode: SCNNode](scnscene/rootnode.md)
  The root node of the scene graph.
- [var lightingEnvironment: SCNMaterialProperty](scnscene/lightingenvironment.md)
  A cube map texture that depicts the environment surrounding the scene’s contents, used for advanced lighting effects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnscene/background)*