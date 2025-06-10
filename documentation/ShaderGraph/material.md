# Material

**Framework**: ShaderGraph  
**Kind**: dictionary

Encapsulate a set of shader graph nodes into a single module.

#### Overview

`Material` nodes help you divide your graph into subsets of nodes, each with distinct inputs and outputs. A [`Node Graph`](material/node-graph.md) appears as a single node within your main graph. Editing that node hides the main graph and gives you an empty space that you fill with additional nodes. Use that space to build a specific portion of your main graph, and use the [`Node Graph`](material/node-graph.md) to define the inputs and outputs to that separate space.

## Topics

### Nodes
- [Node Graph](material/node-graph.md)
  A node that can contain shading nodes and other node graphs.

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
- [Geometric](geometric.md)
  Access scene geometry while your graph runs.
- [Logic](logic.md)
  Perform Boolean operations and other logical comparisons on data values.
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

*[View on Apple Developer](https://developer.apple.com/documentation/shadergraph/material)*