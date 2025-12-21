# Reflect (RealityKit)

**Framework**: ShaderGraph  
**Kind**: subscript

Reflects a vector about another vector.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 26.0+
- visionOS 1.0+

#### Parameter Types

#### Parameter Descriptions

#### Discussion

The `Reflect` node reflects the `In` vector by taking into account the surface orientation determined by the `Normal` vector. The `Reflect` node normalizes the `Normal` vector, then calculates the reflection direction using the formula, `In - 2 * dot(Normal, In) * Normal`. In this equation, `dot()` represents the dot product of the two vectors.

## See Also

- [Position](geometric/position.md)
  The coordinates of the currently-processed data in a given coordinate space.
- [Normal](geometric/normal.md)
  The geometric normal of the currently-processed data in a given coordinate space.
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
- [Refract (RealityKit)](geometric/refract-(realitykit).md)
  Refracts a vector using a given normal and index of refraction (eta).


---

*[View on Apple Developer](https://developer.apple.com/documentation/shadergraph/geometric/reflect-(realitykit))*