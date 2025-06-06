# Data

**Framework**: ShaderGraph  
**Kind**: dictionary

Convert data values to different formats, or manipulate individual elements within a data structure.

#### Overview

Use data nodes to take one type of data and manipulate it to get a different type of value. Data manipulations can take several forms:

- Convert one data type to a different format.
- Combine individual elements to create a single data type.
- Separate a single data type into its component elements.
- Extract or manipulate individual values from a data structure and use them as input to other nodes.

## Topics

### Nodes
- [Convert](data/convert.md)
  Converts a stream from one data type to another.
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

## See Also

- [2D-Procedural](2d-procedural.md)
  Generate 2D gradients, noise, and other patterns programmatically for your material.
- [2D-Texture](2d-texture.md)
  Load and configure 2D texture files.
- [3D-Procedural](3d-procedural.md)
  Generate 3D noise patterns programmatically for your material.
- [3D-Texture](3d-texture.md)
  Project multiple 2D images onto a surface to create a 3D texture.
- [Adjustment](adjustment.md)
  Modify or convert values, or ranges of values, from one form to another.
- [Application](application.md)
  Get system values such as the current time or the direction of the up vector.
- [Compositing](compositing.md)
  Generate a single output from the combination of multiple data values.
- [Geometric](geometric.md)
  Access scene geometry while your graph runs.
- [Logic](logic.md)
  Perform Boolean operations and other logical comparisons on data values.
- [Material](material.md)
  Encapsulate a set of shader graph nodes into a single module.
- [Math](math.md)
  Perform a wide variety of mathematical and transformative operations on data values.
- [Organization](organization.md)
  Modify the visual flow of data within your graph without changing any values.
- [Procedural](procedural.md)
  Add a constant number, vector, matrix, color, string, or other value to your graph.
- [RealityKit](realitykit.md)
  Add RealityKit surfaces or textures to your material and access and manipulate scene geometry.
- [Surface](surface.md)
  Generate a MaterialX preview surface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/shadergraph/data)*