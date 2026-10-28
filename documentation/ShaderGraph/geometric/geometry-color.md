# Geometry Color

**Framework**: ShaderGraph  
**Kind**: subscript  
**Role**: ShaderGraph Node

The color associated with the geometry at the currently-processed geometric position, typically defined by vertex color.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 26.0+
- visionOS 1.0+

## Parameter Types

**Geometry Color (float)**:

| Input | Type |
| --- | --- |
| `Index` | Int32 |

| Output | Type |
| --- | --- |
| `Out` | Float |

**Geometry Color (color3f)**:

| Input | Type |
| --- | --- |
| `Index` | Int32 |

| Output | Type |
| --- | --- |
| `Out` | Color3 |

**Geometry Color (color4f)**:

| Input | Type |
| --- | --- |
| `Index` | Int32 |

| Output | Type |
| --- | --- |
| `Out` | Color4 |

## Parameter description

- **`Index`**: The index of the color the node references. The default value is `0`.

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
- [Texture Coordinates](./texture-coordinates.md)
  The 2D or 3D texture coordinates of the currently-processed data.
- [Geometric Property](./geometric-property.md)
  The value of the specified geometric property (defined using ) of the currently-bound geometry.
- [Reflect (RealityKit)](./reflect-%28realitykit%29.md)
  Reflects a vector about another vector.
- [Refract (RealityKit)](./refract-%28realitykit%29.md)
  Refracts a vector using a given normal and index of refraction (eta).


---

*[View on Apple Developer](https://developer.apple.com/documentation/shadergraph/geometric/geometry-color)*