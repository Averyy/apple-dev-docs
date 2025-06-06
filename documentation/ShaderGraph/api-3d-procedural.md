# 3D-Procedural

**Framework**: ShaderGraph  
**Kind**: dictionary

Generate 3D noise patterns programmatically for your material.

#### Overview

3D Procedural nodes generate noise patterns that don’t repeat along the z-axis of your model. Use the nodes to add random variations to parts of your material, such as its surface roughness. Each node produces a different type of noise pattern based on a specific algorithm.

## Topics

### Nodes
- [Noise 3D](3d-procedural/noise-3d.md)
  A 3D Perlin noise generator.
- [Fractal Noise 3D](3d-procedural/fractal-noise-3d.md)
  Zero-centered 3D fractal noise created by summing several octaves of 3D Perlin noise.
- [Cellular Noise 3D](3d-procedural/cellular-noise-3d.md)
  A 3D cellular noise generator.
- [Worley Noise 3D](3d-procedural/worley-noise-3d.md)
  A 3D Worley noise generator.

## See Also

- [2D-Procedural](2d-procedural.md)
  Generate 2D gradients, noise, and other patterns programmatically for your material.
- [2D-Texture](2d-texture.md)
  Load and configure 2D texture files.
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

*[View on Apple Developer](https://developer.apple.com/documentation/shadergraph/3d-procedural)*