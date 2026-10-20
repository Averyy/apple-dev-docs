# Dot

**Framework**: ShaderGraph  
**Kind**: subscript  
**Role**: ShaderGraph Node

A pass-through node used for visually routing edges in the graph.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 26.0+
- visionOS 1.0+

#### Parameter Types

**Dot (float)**:

| Input | Type |
| --- | --- |
| `In` | Float |
| `Note` | String |

| Output | Type |
| --- | --- |
| `Out` | Float |

**Dot (matrix3x3f)**:

| Input | Type |
| --- | --- |
| `In` | Matrix3x3f |
| `Note` | String |

| Output | Type |
| --- | --- |
| `Out` | Matrix3x3f |

**Dot (Surface Shader)**:

| Input | Type |
| --- | --- |
| `In` | Token |
| `Note` | String |

| Output | Type |
| --- | --- |
| `Out` | Token |

**Dot (vector3f)**:

| Input | Type |
| --- | --- |
| `In` | Vector3f |
| `Note` | String |

| Output | Type |
| --- | --- |
| `Out` | Vector3f |

**Dot (matrix4x4f)**:

| Input | Type |
| --- | --- |
| `In` | Matrix4x4f |
| `Note` | String |

| Output | Type |
| --- | --- |
| `Out` | Matrix4x4f |

**Dot (color3f)**:

| Input | Type |
| --- | --- |
| `In` | Color3 |
| `Note` | String |

| Output | Type |
| --- | --- |
| `Out` | Color3 |

**Dot (vector4f)**:

| Input | Type |
| --- | --- |
| `In` | Vector4f |
| `Note` | String |

| Output | Type |
| --- | --- |
| `Out` | Vector4f |

**Dot (color4f)**:

| Input | Type |
| --- | --- |
| `In` | Color4 |
| `Note` | String |

| Output | Type |
| --- | --- |
| `Out` | Color4 |

**Dot (imageFile)**:

| Input | Type |
| --- | --- |
| `In` | AssetPath |
| `Note` | String |

| Output | Type |
| --- | --- |
| `Out` | AssetPath |

**Dot (vector2f)**:

| Input | Type |
| --- | --- |
| `In` | Vector2f |
| `Note` | String |

| Output | Type |
| --- | --- |
| `Out` | Vector2f |

**Dot (Geometry Modifier)**:

| Input | Type |
| --- | --- |
| `In` | Token |
| `Note` | String |

| Output | Type |
| --- | --- |
| `Out` | Token |

**Dot (string)**:

| Input | Type |
| --- | --- |
| `In` | String |
| `Note` | String |

| Output | Type |
| --- | --- |
| `Out` | String |

**Dot (integer)**:

| Input | Type |
| --- | --- |
| `In` | Int32 |
| `Note` | String |

| Output | Type |
| --- | --- |
| `Out` | Int32 |

**Dot (bool)**:

| Input | Type |
| --- | --- |
| `In` | Bool |
| `Note` | String |

| Output | Type |
| --- | --- |
| `Out` | Bool |

**Dot (half)**:

| Input | Type |
| --- | --- |
| `In` | Half |
| `Note` | String |

| Output | Type |
| --- | --- |
| `Out` | Half |

#### Dicussion

The Dot node is only visual; it has no effect on its input or output. Use the Dot node to make a graph more readable and visually appealing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/shadergraph/organization/dot)*