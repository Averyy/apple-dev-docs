# Swizzle

**Framework**: ShaderGraph  
**Kind**: subscript  
**Role**: ShaderGraph Node

Performs an arbitrary permutation of the channels of the input stream, returning a new stream of the specified type.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 26.0+
- visionOS 1.0+

#### Parameter Types

**Swizzle (float color3f)**:

| Input | Type |
| --- | --- |
| `In` | Float |
| `Channels` | String |

| Output | Type |
| --- | --- |
| `Out` | Color3 |

**Swizzle (half color3f)**:

| Input | Type |
| --- | --- |
| `In` | Half |
| `Channels` | String |

| Output | Type |
| --- | --- |
| `Out` | Color3 |

**Swizzle (color3f vector4f)**:

| Input | Type |
| --- | --- |
| `In` | Color3 |
| `Channels` | String |

| Output | Type |
| --- | --- |
| `Out` | Vector4f |

**Swizzle (color4f float)**:

| Input | Type |
| --- | --- |
| `In` | Color4 |
| `Channels` | String |

| Output | Type |
| --- | --- |
| `Out` | Float |

**Swizzle (vector2h vector4h)**:

| Input | Type |
| --- | --- |
| `In` | Vector2h |
| `Channels` | String |

| Output | Type |
| --- | --- |
| `Out` | Vector4h |

**Swizzle (vector4h vector4h)**:

| Input | Type |
| --- | --- |
| `In` | Vector4h |
| `Channels` | String |

| Output | Type |
| --- | --- |
| `Out` | Vector4h |

**Swizzle (color3f color4f)**:

| Input | Type |
| --- | --- |
| `In` | Color3 |
| `Channels` | String |

| Output | Type |
| --- | --- |
| `Out` | Color4 |

**Swizzle (vector2f color4f)**:

| Input | Type |
| --- | --- |
| `In` | Vector2f |
| `Channels` | String |

| Output | Type |
| --- | --- |
| `Out` | Color4 |

**Swizzle (vector4f float)**:

| Input | Type |
| --- | --- |
| `In` | Vector4f |
| `Channels` | String |

| Output | Type |
| --- | --- |
| `Out` | Float |

**Swizzle (color3f float)**:

| Input | Type |
| --- | --- |
| `In` | Color3 |
| `Channels` | String |

| Output | Type |
| --- | --- |
| `Out` | Float |

**Swizzle (color4f vector3f)**:

| Input | Type |
| --- | --- |
| `In` | Color4 |
| `Channels` | String |

| Output | Type |
| --- | --- |
| `Out` | Vector3f |

**Swizzle (half vector3h)**:

| Input | Type |
| --- | --- |
| `In` | Half |
| `Channels` | String |

| Output | Type |
| --- | --- |
| `Out` | Vector3h |

**Swizzle (vector4f vector2f)**:

| Input | Type |
| --- | --- |
| `In` | Vector4f |
| `Channels` | String |

| Output | Type |
| --- | --- |
| `Out` | Vector2f |

**Swizzle (vector4h half)**:

| Input | Type |
| --- | --- |
| `In` | Vector4h |
| `Channels` | String |

| Output | Type |
| --- | --- |
| `Out` | Half |

**Swizzle (vector4h vector3h)**:

| Input | Type |
| --- | --- |
| `In` | Vector4h |
| `Channels` | String |

| Output | Type |
| --- | --- |
| `Out` | Vector3h |

**Swizzle (float vector4f)**:

| Input | Type |
| --- | --- |
| `In` | Float |
| `Channels` | String |

| Output | Type |
| --- | --- |
| `Out` | Vector4f |

**Swizzle (vector3f float)**:

| Input | Type |
| --- | --- |
| `In` | Vector3f |
| `Channels` | String |

| Output | Type |
| --- | --- |
| `Out` | Float |

**Swizzle (vector2f color3f)**:

| Input | Type |
| --- | --- |
| `In` | Vector2f |
| `Channels` | String |

| Output | Type |
| --- | --- |
| `Out` | Color3 |

**Swizzle (vector2f float)**:

| Input | Type |
| --- | --- |
| `In` | Vector2f |
| `Channels` | String |

| Output | Type |
| --- | --- |
| `Out` | Float |

**Swizzle (half vector4h)**:

| Input | Type |
| --- | --- |
| `In` | Half |
| `Channels` | String |

| Output | Type |
| --- | --- |
| `Out` | Vector4h |

**Swizzle (color4f color3f)**:

| Input | Type |
| --- | --- |
| `In` | Color4 |
| `Channels` | String |

| Output | Type |
| --- | --- |
| `Out` | Color3 |

**Swizzle (vector2h vector2h)**:

| Input | Type |
| --- | --- |
| `In` | Vector2h |
| `Channels` | String |

| Output | Type |
| --- | --- |
| `Out` | Vector2h |

**Swizzle (vector4f half)**:

| Input | Type |
| --- | --- |
| `In` | Vector4f |
| `Channels` | String |

| Output | Type |
| --- | --- |
| `Out` | Half |

**Swizzle (vector2f vector2f)**:

| Input | Type |
| --- | --- |
| `In` | Vector2f |
| `Channels` | String |

| Output | Type |
| --- | --- |
| `Out` | Vector2f |

**Swizzle (vector3h vector3h)**:

| Input | Type |
| --- | --- |
| `In` | Vector3h |
| `Channels` | String |

| Output | Type |
| --- | --- |
| `Out` | Vector3h |

**Swizzle (float vector2f)**:

| Input | Type |
| --- | --- |
| `In` | Float |
| `Channels` | String |

| Output | Type |
| --- | --- |
| `Out` | Vector2f |

**Swizzle (vector3h half)**:

| Input | Type |
| --- | --- |
| `In` | Vector3h |
| `Channels` | String |

| Output | Type |
| --- | --- |
| `Out` | Half |

**Swizzle (color3f vector3f)**:

| Input | Type |
| --- | --- |
| `In` | Color3 |
| `Channels` | String |

| Output | Type |
| --- | --- |
| `Out` | Vector3f |

**Swizzle (vector3f vector2f)**:

| Input | Type |
| --- | --- |
| `In` | Vector3f |
| `Channels` | String |

| Output | Type |
| --- | --- |
| `Out` | Vector2f |

**Swizzle (vector4f color4f)**:

| Input | Type |
| --- | --- |
| `In` | Vector4f |
| `Channels` | String |

| Output | Type |
| --- | --- |
| `Out` | Color4 |

**Swizzle (vector3f color3f)**:

| Input | Type |
| --- | --- |
| `In` | Vector3f |
| `Channels` | String |

| Output | Type |
| --- | --- |
| `Out` | Color3 |

**Swizzle (vector2f vector3f)**:

| Input | Type |
| --- | --- |
| `In` | Vector2f |
| `Channels` | String |

| Output | Type |
| --- | --- |
| `Out` | Vector3f |

**Swizzle (vector2h vector3h)**:

| Input | Type |
| --- | --- |
| `In` | Vector2h |
| `Channels` | String |

| Output | Type |
| --- | --- |
| `Out` | Vector3h |

**Swizzle (float vector3f)**:

| Input | Type |
| --- | --- |
| `In` | Float |
| `Channels` | String |

| Output | Type |
| --- | --- |
| `Out` | Vector3f |

**Swizzle (color4f half)**:

| Input | Type |
| --- | --- |
| `In` | Color4 |
| `Channels` | String |

| Output | Type |
| --- | --- |
| `Out` | Half |

**Swizzle (vector3h vector4h)**:

| Input | Type |
| --- | --- |
| `In` | Vector3h |
| `Channels` | String |

| Output | Type |
| --- | --- |
| `Out` | Vector4h |

**Swizzle (half vector2h)**:

| Input | Type |
| --- | --- |
| `In` | Half |
| `Channels` | String |

| Output | Type |
| --- | --- |
| `Out` | Vector2h |

**Swizzle (vector4f vector4f)**:

| Input | Type |
| --- | --- |
| `In` | Vector4f |
| `Channels` | String |

| Output | Type |
| --- | --- |
| `Out` | Vector4f |

**Swizzle (vector3f vector4f)**:

| Input | Type |
| --- | --- |
| `In` | Vector3f |
| `Channels` | String |

| Output | Type |
| --- | --- |
| `Out` | Vector4f |

**Swizzle (color3f color3f)**:

| Input | Type |
| --- | --- |
| `In` | Color3 |
| `Channels` | String |

| Output | Type |
| --- | --- |
| `Out` | Color3 |

**Swizzle (vector4h vector2h)**:

| Input | Type |
| --- | --- |
| `In` | Vector4h |
| `Channels` | String |

| Output | Type |
| --- | --- |
| `Out` | Vector2h |

**Swizzle (color3f vector2f)**:

| Input | Type |
| --- | --- |
| `In` | Color3 |
| `Channels` | String |

| Output | Type |
| --- | --- |
| `Out` | Vector2f |

**Swizzle (color4f vector2f)**:

| Input | Type |
| --- | --- |
| `In` | Color4 |
| `Channels` | String |

| Output | Type |
| --- | --- |
| `Out` | Vector2f |

**Swizzle (vector3f half)**:

| Input | Type |
| --- | --- |
| `In` | Vector3f |
| `Channels` | String |

| Output | Type |
| --- | --- |
| `Out` | Half |

**Swizzle (color3f half)**:

| Input | Type |
| --- | --- |
| `In` | Color3 |
| `Channels` | String |

| Output | Type |
| --- | --- |
| `Out` | Half |

**Swizzle (vector4f color3f)**:

| Input | Type |
| --- | --- |
| `In` | Vector4f |
| `Channels` | String |

| Output | Type |
| --- | --- |
| `Out` | Color3 |

**Swizzle (vector3h vector2h)**:

| Input | Type |
| --- | --- |
| `In` | Vector3h |
| `Channels` | String |

| Output | Type |
| --- | --- |
| `Out` | Vector2h |

**Swizzle (color4f vector4f)**:

| Input | Type |
| --- | --- |
| `In` | Color4 |
| `Channels` | String |

| Output | Type |
| --- | --- |
| `Out` | Vector4f |

**Swizzle (vector2f half)**:

| Input | Type |
| --- | --- |
| `In` | Vector2f |
| `Channels` | String |

| Output | Type |
| --- | --- |
| `Out` | Half |

**Swizzle (half color4f)**:

| Input | Type |
| --- | --- |
| `In` | Half |
| `Channels` | String |

| Output | Type |
| --- | --- |
| `Out` | Color4 |

**Swizzle (vector4f vector3f)**:

| Input | Type |
| --- | --- |
| `In` | Vector4f |
| `Channels` | String |

| Output | Type |
| --- | --- |
| `Out` | Vector3f |

**Swizzle (vector3f color4f)**:

| Input | Type |
| --- | --- |
| `In` | Vector3f |
| `Channels` | String |

| Output | Type |
| --- | --- |
| `Out` | Color4 |

**Swizzle (vector2f vector4f)**:

| Input | Type |
| --- | --- |
| `In` | Vector2f |
| `Channels` | String |

| Output | Type |
| --- | --- |
| `Out` | Vector4f |

**Swizzle (vector3f vector3f)**:

| Input | Type |
| --- | --- |
| `In` | Vector3f |
| `Channels` | String |

| Output | Type |
| --- | --- |
| `Out` | Vector3f |

**Swizzle (color4f color4f)**:

| Input | Type |
| --- | --- |
| `In` | Color4 |
| `Channels` | String |

| Output | Type |
| --- | --- |
| `Out` | Color4 |

**Swizzle (float color4f)**:

| Input | Type |
| --- | --- |
| `In` | Float |
| `Channels` | String |

| Output | Type |
| --- | --- |
| `Out` | Color4 |

**Swizzle (vector2h half)**:

| Input | Type |
| --- | --- |
| `In` | Vector2h |
| `Channels` | String |

| Output | Type |
| --- | --- |
| `Out` | Half |

#### Parameter descriptions

- **`In`**: The input value.
- **`Channels`**: A string of `1-4` characters that determine the permutation to perform. These characters can be “r”, “g”, “b”, or “a” if the `In` parameter is a color input, or “x”, “y”, “z”, or “w” for vector inputs. Use “r” or “x” if the input is a float.

#### Discussion

The `Swizzle` node determines its output by first looking at the `Channels` parameter. Each character in the `Channel` string represents one of the channels of the `In` parameter. For example, if you pass in a vector3 of `(1, 5, 10)` as the `In` parameter, “x” refers to `1`, `y` to `5`, and `z` to `10`. The order of the characters determines how the channels of the input switch around to create the output. For the previous example, if the `Channels` parameter is “zzz”, the output is `(10, 10, 10)`.

> **Note**: The character length of `Channels` must be equal to the number of channels in the output.

The table below shows additional examples of the swizzle node process:

| In | Channels | Out |
| --- | --- | --- |
| Vector3: (1, 5, 10) | zzz | Vector3: (10, 10, 10) |
| Vector3: (1, 5, 10) | zyx | Vector3: (10, 5, 1) |
| Vector2: (5, 0) | xxy | Vector3: (5, 5, 0) |
| Vector3: (1, 5, 10) | zx | Vector2: (10, 1) |
| Color3: (0.5, 0.8, 0) | grb | Color3: (0.8, 0.5, 0) |

## See Also

### Nodes
- [Convert](./convert.md)
  Converts a stream from one data type to another.
- [Combine 2](./combine-2.md)
  Combines the channels from two streams into two channels of a single output stream of a compatible type.
- [Combine 3](./combine-3.md)
  Combines the channels from three streams into three channels of a single output stream of a compatible type.
- [Combine 4](./combine-4.md)
  Combines the channels from four streams into four channels of a single output stream of a compatible type.
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

*[View on Apple Developer](https://developer.apple.com/documentation/shadergraph/data/swizzle)*