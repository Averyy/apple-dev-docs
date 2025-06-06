# textureCoordinateTransform

**Framework**: RealityKit  
**Kind**: property

A two-dimensional transformation RealityKit applies to the entity’s primary texture coordinates.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+

## Declaration

```swift
var textureCoordinateTransform: CustomMaterial.TextureCoordinateTransform { get set }
```

#### Discussion

An entity’s UV texture coordinates control how RealityKit materials map image textures onto an entity. Use this property to transform the texture coordinates and change the way this material maps its textures. For example, you might change the scale of the UV coordinates to apply a tiled, repeating pattern to the surface of your entity, or continuously rotate or translate the texture coordinates to animate materials and create special effects, such as fire or flowing liquids.

The following example shows how to set a material’s UV transformation:

```swift
let rotationRadians = Float(45.0) * .pi / 180 // 45 degrees converted to radians.
material.textureCoordinateTransform = .init(
    offset: [0.5, 0.5], scale: [0.5, 0.5],
    rotation: rotationRadians
)
```

The material’s shader function doesn’t have to do anything to apply the transformation. When the shader calls `params.geometry().uv1()`, RealityKit already transforms the returned coordinates.

## See Also

- [var secondaryTextureCoordinateTransform: CustomMaterial.TextureCoordinateTransform](custommaterial/secondarytexturecoordinatetransform.md)
  A two-dimensional transformation RealityKit applies to the entity’s secondary texture coordinates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/custommaterial/texturecoordinatetransform-swift.property)*