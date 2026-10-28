# Texture Coordinates

**Framework**: ShaderGraph  
**Kind**: subscript  
**Role**: ShaderGraph Node

The 2D or 3D texture coordinates of the currently-processed data.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 26.0+
- visionOS 1.0+

## Parameter Types

**Texture Coordinates (vector2f)**:

| Input | Type |
| --- | --- |
| `Index` | Int32 |

| Output | Type |
| --- | --- |
| `Out` | Vector2f |

**Texture Coordinates (vector4f)**:

| Input | Type |
| --- | --- |
| `Index` | Int32 |

| Output | Type |
| --- | --- |
| `Out` | Vector4f |

## Parameter description

- **`Index`**: The index of the texture coordinates to reference; the default is `0`.

## See Also

### Nodes
- [Position](./position.md)
  The coordinates of the currently-processed data in a given coordinate space.
- [Normal](./normal.md)
  The geometric normal of the currently-processed data in a given coordinate space.
- [Tangent](./tangent.md)
  The geometric tangent of the currently-processed data in a given coordinate space.
- [Bitangent](./bitangent.md)
  The geometric bitangent vector of the currently-processed data in a given coordinate space.
- [Geometry Color](./geometry-color.md)
  The color associated with the geometry at the currently-processed geometric position, typically defined by vertex color.
- [Geometric Property](./geometric-property.md)
  The value of the specified geometric property (defined using ) of the currently-bound geometry.
- [Reflect (RealityKit)](./reflect-%28realitykit%29.md)
  Reflects a vector about another vector.
- [Refract (RealityKit)](./refract-%28realitykit%29.md)
  Refracts a vector using a given normal and index of refraction (eta).


---

*[View on Apple Developer](https://developer.apple.com/documentation/shadergraph/geometric/texture-coordinates)*