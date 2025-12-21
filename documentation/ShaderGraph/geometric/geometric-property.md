# Geometric Property

**Framework**: ShaderGraph  
**Kind**: subscript

The value of the specified geometric property (defined using ) of the currently-bound geometry.

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

The Geometric Property node attempts to return the value of the geometric property with the name defined by the `Geomprop` parameter. If that property doesn’t exist or there’s an error retrieving the property’s value, the node outputs the value of the `Default` parameter.

> **Note**: The type of this node must be the same as the type of the geometric property you’re attempting to reference.

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
- [Reflect (RealityKit)](geometric/reflect-(realitykit).md)
  Reflects a vector about another vector.
- [Refract (RealityKit)](geometric/refract-(realitykit).md)
  Refracts a vector using a given normal and index of refraction (eta).


---

*[View on Apple Developer](https://developer.apple.com/documentation/shadergraph/geometric/geometric-property)*