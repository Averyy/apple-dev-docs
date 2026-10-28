# background

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

A background to be rendered before the rest of the scene.

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
var background: SCNMaterialProperty { get }
```

```objc
@property (nonatomic, readonly) SCNMaterialProperty * background;
```

## Discussion

If the material property’s [`contents`](../scnmaterialproperty/contents.md) object is `nil`, SceneKit does not draw any background before drawing the rest of the scene. (If the scene is presented in an [`SCNView`](../scnview.md) instance, the view’s background color is visible behind the contents of the scene.)

If you specify a cube map texture for the material property (see the discussion of the [`contents`](../scnmaterialproperty/contents.md) property), SceneKit renders the background as a skybox.

## See Also

### Accessing Scene Contents
- [var rootNode: SCNNode](./rootnode.md)
  The root node of the scene graph.
- [var lightingEnvironment: SCNMaterialProperty](./lightingenvironment.md)
  A cube map texture that depicts the environment surrounding the scene’s contents, used for advanced lighting effects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnscene/background)*