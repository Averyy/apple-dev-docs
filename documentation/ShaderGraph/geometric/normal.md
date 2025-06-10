# Normal

**Framework**: ShaderGraph  
**Kind**: subscript

The geometric normal of the currently-processed data in a given coordinate space.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 26.0+ (Beta)
- visionOS 1.0+

#### Parameter Types

#### Parameter Description

#### Discussion

Valid values for the `Space` parameter include the following:

- `model`: The local coordinate space before the shader applies any local deformations or global transforms to the geometry.
- `object`: The local coordinate space after the shader applies local deformations but before it applies global transforms to the geometry.
- `world`: The global coordinate space after the shader applies both local deformations and global transforms to the geometry.

## See Also

- [Position](geometric/position.md)
  The coordinates of the currently-processed data in a given coordinate space.
- [Tangent](geometric/tangent.md)
  The geometric tangent of the currently-processed data in a given coordinate space.
- [Bitangent](geometric/bitangent.md)
  The geometric bitangent vector of the currently-processed data in a given coordinate space.
- [Texture Coordinates](geometric/texture-coordinates.md)
  The 2D or 3D texture coordinates of the currently-processed data.
- [Geometry Color](geometric/geometry-color.md)
  The color associated with the geometry at the currently-processed geometric position, typically defined by vertex color.
- [Geometric Property](geometric/geometric-property.md)
  The value of the specified geometric property (defined using ) of the currently-bound geometry.
- [Reflect (RealityKit)](geometric/reflect-(realitykit).md)
  Reflects a vector about another vector.
- [Refract (RealityKit)](geometric/refract-(realitykit).md)
  Refracts a vector using a given normal and index of refraction (eta).


---

*[View on Apple Developer](https://developer.apple.com/documentation/shadergraph/geometric/normal)*