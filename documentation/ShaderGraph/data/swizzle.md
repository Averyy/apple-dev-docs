# Swizzle

**Framework**: ShaderGraph  
**Kind**: subscript

Performs an arbitrary permutation of the channels of the input stream, returning a new stream of the specified type.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 26.0+ (Beta)
- visionOS 1.0+

#### Parameter Types

#### Parameter Descriptions

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

- [Convert](data/convert.md)
  Converts a stream from one data type to another.
- [Combine 2](data/combine-2.md)
  Combines the channels from two streams into two channels of a single output stream of a compatible type.
- [Combine 3](data/combine-3.md)
  Combines the channels from three streams into three channels of a single output stream of a compatible type.
- [Combine 4](data/combine-4.md)
  Combines the channels from four streams into four channels of a single output stream of a compatible type.
- [Extract](data/extract.md)
  Generates a float stream from one channel of a color​N o​r vector​N ​stream.
- [Separate 2](data/separate-2.md)
  Outputs each of the channels of a vector2 or integer2 as individual float or integer outputs.
- [Separate 3](data/separate-3.md)
  Outputs each of the channels of a color3, vector3, or integer3 as individual float or integer outputs.
- [Separate 4](data/separate-4.md)
  Outputs each of the channels of a color4, vector4, or integer4 as individual float or integer outputs.
- [Primvar Reader](data/primvar-reader.md)
  A node that provides the ability for shading networks to consume data defined on geometry.


---

*[View on Apple Developer](https://developer.apple.com/documentation/shadergraph/data/swizzle)*