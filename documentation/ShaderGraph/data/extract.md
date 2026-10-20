# Extract

**Framework**: ShaderGraph  
**Kind**: subscript  
**Role**: ShaderGraph Node

Generates a float stream from one channel of a color​N o​r vector​N ​stream.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 26.0+
- visionOS 1.0+

#### Parameter Types

**Extract (color3f)**:

| Input | Type |
| --- | --- |
| `In` | Color3 |
| `Index` | Int32 |

| Output | Type |
| --- | --- |
| `Out` | Float |

**Extract (vector3h)**:

| Input | Type |
| --- | --- |
| `In` | Vector3h |
| `Index` | Int32 |

| Output | Type |
| --- | --- |
| `Out` | Half |

**Extract (vector4f)**:

| Input | Type |
| --- | --- |
| `In` | Vector4f |
| `Index` | Int32 |

| Output | Type |
| --- | --- |
| `Out` | Float |

**Extract (vector2h)**:

| Input | Type |
| --- | --- |
| `In` | Vector2h |
| `Index` | Int32 |

| Output | Type |
| --- | --- |
| `Out` | Half |

**Extract (vector2f)**:

| Input | Type |
| --- | --- |
| `In` | Vector2f |
| `Index` | Int32 |

| Output | Type |
| --- | --- |
| `Out` | Float |

**Extract (color4f)**:

| Input | Type |
| --- | --- |
| `In` | Color4 |
| `Index` | Int32 |

| Output | Type |
| --- | --- |
| `Out` | Float |

**Extract (vector3f)**:

| Input | Type |
| --- | --- |
| `In` | Vector3f |
| `Index` | Int32 |

| Output | Type |
| --- | --- |
| `Out` | Float |

**Extract (vector4h)**:

| Input | Type |
| --- | --- |
| `In` | Vector4h |
| `Index` | Int32 |

| Output | Type |
| --- | --- |
| `Out` | Half |

#### Parameter descriptions

- **`In`**: The input from which to extract a value.
- **`Index`**: The index of the input from which to extract a value. Default value is `0`.

#### Discussion

The Extract node takes its `In` input and always outputs a singular `Float`. The value of the node’s output is the value of number in the `Index` position of `In`. For example, if `In` is equal to a `Vector3` of (10,15,20) and `Index` is `1`, the output is `15`.

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
- [Combine 4](./combine-4.md)
  Combines the channels from four streams into four channels of a single output stream of a compatible type.
- [Separate 2](./separate-2.md)
  Outputs each of the channels of a vector2 or integer2 as individual float or integer outputs.
- [Separate 3](./separate-3.md)
  Outputs each of the channels of a color3, vector3, or integer3 as individual float or integer outputs.
- [Separate 4](./separate-4.md)
  Outputs each of the channels of a color4, vector4, or integer4 as individual float or integer outputs.
- [Primvar Reader](./primvar-reader.md)
  A node that provides the ability for shading networks to consume data defined on geometry.


---

*[View on Apple Developer](https://developer.apple.com/documentation/shadergraph/data/extract)*