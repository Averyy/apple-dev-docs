# Convert

**Framework**: ShaderGraph  
**Kind**: subscript

Converts a stream from one data type to another.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 26.0+
- visionOS 1.0+

#### Parameter Types

#### Discussion

The `Convert` node takes data of one type and outputs it in another form. The supported type conversions are shown above with the various convert node types. The `Convert` node handles data types in the following ways:

- When converting a `float` to a `color` or `vector`, the `Convert` node copies the `float` to all channels of the `color` or `vector`.
- When converting a `color3` to a `color4`, the `Convert` node sets the output alpha to `1.0`
- When converting a `color4` to a `color3`, the `Convert` node drops the alpha channel.
- When converting a `boolean` or `integer` to a `float`, the output is either `1.0` or `0.0`.
- When converting a `vector2` to `vector3` or a `vector3` to a `vector4`, the `Convert` nodes populates the additional channel with a value of `1.0`
- When converting a `vector4` to a `vector3`, or a `vector3` to a `vector2`, drop the last channel.

## See Also

- [Swizzle](data/swizzle.md)
  Performs an arbitrary permutation of the channels of the input stream, returning a new stream of the specified type.
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

*[View on Apple Developer](https://developer.apple.com/documentation/shadergraph/data/convert)*