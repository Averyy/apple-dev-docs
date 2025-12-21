# textureCoordinateTransform

**Framework**: RealityKit  
**Kind**: property

A two-dimensional transformation to apply to the entity’s primary texture coordinates.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+
- visionOS ?+

## Declaration

```swift
var textureCoordinateTransform: PhysicallyBasedMaterial.TextureCoordinateTransform { get set }
```

#### Discussion

An entity’s UV texture coordinates control how RealityKit materials map image textures onto an entity. This property allows you to transform the texture coordinates to change the way this material maps its textures. You might, for example, change the scale of a property to apply a tiled, repeating pattern, or continuously rotate or translate the texture coordinates to animate materials to create special effects, such as fire or flowing liquids.

The following example shows how to set a material’s UV transformation:

```swift
let rotationRadians = Float(45.0) * .pi / 180 // 45 degrees converted to radians.
material.textureCoordinateTransform = .init(offset: SIMD2<Float>(x:0.5, y: 0.5),
                                            scale: SIMD2<Float>(x:0.5, y: 0.5),
                                            rotation: rotationRadians)
```

Some entities imported from USDZ files have more than one set of UV coordinates. This property affects the primary UV set (sometimes called “UV1”). To transform the secondary UV coordinates (”UV2”), use [`secondaryTextureCoordinateTransform`](physicallybasedmaterial/secondarytexturecoordinatetransform.md).

## See Also

- [var secondaryTextureCoordinateTransform: PhysicallyBasedMaterial.TextureCoordinateTransform](physicallybasedmaterial/secondarytexturecoordinatetransform.md)
  A two-dimensional transformation to apply to the entity’s secondary texture coordinates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/physicallybasedmaterial/texturecoordinatetransform-swift.property)*