# lightingEnvironment

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

A cube map texture that depicts the environment surrounding the scene’s contents, used for advanced lighting effects.

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
var lightingEnvironment: SCNMaterialProperty { get }
```

```objc
@property (nonatomic, readonly) SCNMaterialProperty * lightingEnvironment;
```

#### Discussion

When rendering materials with the [`physicallyBased`](../scnmaterial/lightingmodel-swift.struct/physicallybased.md) lighting model, SceneKit illuminates surfaces differently according to the environment that surrounds them. For example, with physically based shading, even a diffuse surface takes on some color from the sky above it and the ground below it.

> 💡 **Tip**:  For realistic results, reuse the same contents for both the lighting environment and the [`background`](./background.md) property.

For information about defining cube maps, see the discussion of the [`contents`](../scnmaterialproperty/contents.md) property.

## See Also

### Accessing Scene Contents
- [var rootNode: SCNNode](./rootnode.md)
  The root node of the scene graph.
- [var background: SCNMaterialProperty](./background.md)
  A background to be rendered before the rest of the scene.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnscene/lightingenvironment)*