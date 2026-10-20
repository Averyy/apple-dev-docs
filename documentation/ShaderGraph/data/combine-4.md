# Combine 4

**Framework**: ShaderGraph  
**Kind**: subscript  
**Role**: ShaderGraph Node

Combines the channels from four streams into four channels of a single output stream of a compatible type.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 26.0+
- visionOS 1.0+

#### Parameter Types

**Combine 4 (color4f)**:

| Input | Type |
| --- | --- |
| `In 1` | Float |
| `In 2` | Float |
| `In 3` | Float |
| `In 4` | Float |

| Output | Type |
| --- | --- |
| `Out` | Color4 |

**Combine 4 (vector4h)**:

| Input | Type |
| --- | --- |
| `In 1` | Half |
| `In 2` | Half |
| `In 3` | Half |
| `In 4` | Half |

| Output | Type |
| --- | --- |
| `Out` | Vector4h |

**Combine 4 (color4h)**:

| Input | Type |
| --- | --- |
| `In 1` | Half |
| `In 2` | Half |
| `In 3` | Half |
| `In 4` | Half |

| Output | Type |
| --- | --- |
| `Out` | Color4 |

**Combine 4 (integer4)**:

| Input | Type |
| --- | --- |
| `In 1` | Int32 |
| `In 2` | Int32 |
| `In 3` | Int32 |
| `In 4` | Int32 |

| Output | Type |
| --- | --- |
| `Out` | Integer4 |

**Combine 4 (vector4f)**:

| Input | Type |
| --- | --- |
| `In 1` | Float |
| `In 2` | Float |
| `In 3` | Float |
| `In 4` | Float |

| Output | Type |
| --- | --- |
| `Out` | Vector4f |

**Combine 4 (matrix4x4f)**:

| Input | Type |
| --- | --- |
| `In 1` | Vector4f |
| `In 2` | Vector4f |
| `In 3` | Vector4f |
| `In 4` | Vector4f |

| Output | Type |
| --- | --- |
| `Out` | Matrix4x4f |

## See Also

### Nodes
- [Convert](./convert.md)
  Converts a stream from one data type to another.
- [Swizzle](./swizzle.md)
  Performs an arbitrary permutation of the channels of the input stream, returning a new stream of the specified type.
- [Combine 2](./combine-2.md)
  Combines the channels from two streams into two channels of a single output stream of a compatible type.
- [Combine 3](./combine-3.md)
  Combines the channels from three streams into three channels of a single output stream of a compatible type.
- [Extract](./extract.md)
  Generates a float stream from one channel of a color​N o​r vector​N ​stream.
- [Separate 2](./separate-2.md)
  Outputs each of the channels of a vector2 or integer2 as individual float or integer outputs.
- [Separate 3](./separate-3.md)
  Outputs each of the channels of a color3, vector3, or integer3 as individual float or integer outputs.
- [Separate 4](./separate-4.md)
  Outputs each of the channels of a color4, vector4, or integer4 as individual float or integer outputs.
- [Primvar Reader](./primvar-reader.md)
  A node that provides the ability for shading networks to consume data defined on geometry.


---

*[View on Apple Developer](https://developer.apple.com/documentation/shadergraph/data/combine-4)*