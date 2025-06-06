# 2D-Texture

**Framework**: ShaderGraph  
**Kind**: dictionary

Load and configure 2D texture files.

#### Overview

Use these nodes to incorporate file-based textures into your material. In addition to loading textures from disk, you can use each node to customize the rendering behavior of the texture.

For example, a Tiled Image node repeats the original image to fill the surface with content. In addition to loading textures, you can use the Transform 2D node to apply an affine transform to a 2D vector.

## Topics

### Nodes
- [Image](2d-texture/image.md)
  A texture referencing a 2D image file.
- [Tiled Image](2d-texture/tiled-image.md)
  Samples data from an image with provisions for offsetting and tiling in UV space.
- [UV Texture](2d-texture/uv-texture.md)
  A MaterialX version of USD UV Texture reader.
- [Transform 2D](2d-texture/transform-2d.md)
  A node that applies an affine transformation to a 2d input.

## See Also

- [2D-Procedural](2d-procedural.md)
  Generate 2D gradients, noise, and other patterns programmatically for your material.
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

*[View on Apple Developer](https://developer.apple.com/documentation/shadergraph/2d-texture)*