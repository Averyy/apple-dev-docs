# Geometric

**Framework**: ShaderGraph  
**Kind**: dictionary

Access scene geometry while your graph runs.

#### Overview

When the GPU applies your graph to a scene, geometric nodes reflect the data value the system is currently processing. Use these nodes to get details about that data value, such as its coordinates, normal, or tangent information. Alternatively, use the Reflect and Refract nodes to modify vectors relative to the current data value.

## Topics

### Nodes
- [Position](geometric/position.md)
  The coordinates of the currently-processed data in a given coordinate space.
- [Normal](geometric/normal.md)
  The geometric normal of the currently-processed data in a given coordinate space.
- [Tangent](geometric/tangent.md)
  The geometric tangent of the currently-processed data in a given coordinate space.
- [Bitangent](geometric/bitangent.md)
  The geometric bitangent vector of the currently-processed data in a given coordinate space.
- [Texture Coordinates](geometric/texture-coordinates.md)
  The 2D or 3D texture coordinates of the currently-processed data.
- [Geometry Color](geometric/geometry-color.md)
  The color associated with the geometry at the currently-processed geometric position, typically defined by vertex color.
- [Geometric Property](geometric/geometric-property.md)
  The value of the specified geometric property (defined using ) of the currently-bound geometry.
- [Reflect (RealityKit)](geometric/reflect-(realitykit).md)
  Reflects a vector about another vector.
- [Refract (RealityKit)](geometric/refract-(realitykit).md)
  Refracts a vector using a given normal and index of refraction (eta).

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
- [Data](data.md)
  Convert data values to different formats, or manipulate individual elements within a data structure.
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

*[View on Apple Developer](https://developer.apple.com/documentation/shadergraph/geometric)*