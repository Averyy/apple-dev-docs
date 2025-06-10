# ShaderGraph

**Framework**: ShaderGraph  
**Kind**: module

Create custom materials and effects for 3D content in Reality Composer Pro.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 15.0+
- tvOS 26.0+ (Beta)
- visionOS 1.0+

#### Overview

Create complex materials and effects with Shader Graph, a node-based material editor within Reality Composer Pro. The editor presents an interface in which you can build out node graphs to achieve various visual effects.

With the control Shader Graph provides over materials, you can create effects that might otherwise require writing Metal shaders. The nodes represent either a value or operation, and have inputs and outputs you can connect to build a material. They serve the same purpose as a variable, constant, or function in Metal. Multiple versions of a node tweak the inputs and outputs it can receive, similar to overloads of a function.

![None](https://docs-assets.developer.apple.com/published/9d613c8625c7195c13461b29b95ef35a/HomePageMaterial1.png)

Build your material using the nodes that achieve your desired visual and geometric effects, and apply these materials to entities within your Reality Composer Pro scene.

#### Interoperability

Shader Graph uses MaterialX 1.38 conventions to improve interoperability with content creation applications that can read and author MaterialX within USD files.

Shader Graph also includes several nodes that are unique to RealityKit. Some of these nodes are available as standard MaterialX definitions that you can use within your content creation workflow. To download these definitions, see [`MaterialX definitions`](https://developer.apple.comhttps://developer.apple.com/augmented-reality/realitykit/files/MaterialX-definitions.zip).

## Topics

### Node Categories
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

*[View on Apple Developer](https://developer.apple.com/documentation/ShaderGraph)*