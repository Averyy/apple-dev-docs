# Separate 2

**Framework**: ShaderGraph  
**Kind**: subscript  
**Role**: ShaderGraph Node

Outputs each of the channels of a vector2 or integer2 as individual float or integer outputs.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 26.0+
- visionOS 1.0+

## Parameter Types

**Separate 2 (vector2f)**:

| Input | Type |
| --- | --- |
| `In` | Vector2f |

| Output | Type |
| --- | --- |
| `x` | Float |
| `y` | Float |

**Separate 2**:

| Input | Type |
| --- | --- |
| `In` | Integer2 |

| Output | Type |
| --- | --- |
| `Outx` | Int32 |
| `Outy` | Int32 |

**Separate 2 (vector2h)**:

| Input | Type |
| --- | --- |
| `In` | Vector2h |

| Output | Type |
| --- | --- |
| `Outx` | Half |
| `Outy` | Half |

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
- [Extract](./extract.md)
  Generates a float stream from one channel of a color​N o​r vector​N ​stream.
- [Separate 3](./separate-3.md)
  Outputs each of the channels of a color3, vector3, or integer3 as individual float or integer outputs.
- [Separate 4](./separate-4.md)
  Outputs each of the channels of a color4, vector4, or integer4 as individual float or integer outputs.
- [Primvar Reader](./primvar-reader.md)
  A node that provides the ability for shading networks to consume data defined on geometry.


---

*[View on Apple Developer](https://developer.apple.com/documentation/shadergraph/data/separate-2)*