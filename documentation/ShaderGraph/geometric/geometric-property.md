# Geometric Property

**Framework**: ShaderGraph  
**Kind**: subscript  
**Role**: ShaderGraph Node

The value of the specified geometric property (defined using ) of the currently-bound geometry.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 26.0+
- visionOS 1.0+

#### Parameter Types

**Geometric Property (float)**:

| Input | Type |
| --- | --- |
| `Geomprop` | String |
| `Default` | Float |

| Output | Type |
| --- | --- |
| `Out` | Float |

**Geometric Property (color4f)**:

| Input | Type |
| --- | --- |
| `Geomprop` | String |
| `Default` | Color4 |

| Output | Type |
| --- | --- |
| `Out` | Color4 |

**Geometric Property (vector2f)**:

| Input | Type |
| --- | --- |
| `Geomprop` | String |
| `Default` | Vector2f |

| Output | Type |
| --- | --- |
| `Out` | Vector2f |

**Geometric Property (color3f)**:

| Input | Type |
| --- | --- |
| `Geomprop` | String |
| `Default` | Color3 |

| Output | Type |
| --- | --- |
| `Out` | Color3 |

**Geometric Property (vector3f)**:

| Input | Type |
| --- | --- |
| `Geomprop` | String |
| `Default` | Vector3f |

| Output | Type |
| --- | --- |
| `Out` | Vector3f |

#### Parameter descriptions

- **`Geomprop`**: The name of the geometric property to be read.
- **`Default`**: The value the node returns if it’s unable to read the geometric property.

#### Discussion

The Geometric Property node attempts to return the value of the geometric property with the name defined by the `Geomprop` parameter. If that property doesn’t exist or there’s an error retrieving the property’s value, the node outputs the value of the `Default` parameter.

> **Note**: The type of this node must be the same as the type of the geometric property you’re attempting to reference.

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
- [Geometry Color](./geometry-color.md)
  The color associated with the geometry at the currently-processed geometric position, typically defined by vertex color.
- [Reflect (RealityKit)](./reflect-%28realitykit%29.md)
  Reflects a vector about another vector.
- [Refract (RealityKit)](./refract-%28realitykit%29.md)
  Refracts a vector using a given normal and index of refraction (eta).


---

*[View on Apple Developer](https://developer.apple.com/documentation/shadergraph/geometric/geometric-property)*