# Refract (RealityKit)

**Framework**: Shadergraph  
**Kind**: subscript

Refracts a vector using a given normal and index of refraction (eta).

#### Parameter Types

#### Parameter Descriptions

#### Discussion

The Refract node takes an incident vector `In` and calculates the direction of refraction off a surface.

> **Note**: The vectors passed as the `In` and `Normal` parameters must both already be normalized in order to get the desired output.

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
- [Reflect (RealityKit)](geometric/reflect-(realitykit).md)
  Reflects a vector about another vector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/shadergraph/geometric/refract-(realitykit))*