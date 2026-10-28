# Cellular Noise 2D

**Framework**: ShaderGraph  
**Kind**: subscript  
**Role**: ShaderGraph Node

A 2D cellular noise generator.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 26.0+
- visionOS 1.0+

## Parameter Types

| Input | Type |
| --- | --- |
| `Texture Coordinates` | Vector2f |

| Output | Type |
| --- | --- |
| `Out` | Float |

## Parameter descriptions

- **`Texture Coordinates`**: The 2D coordinate at which the data is read to map the texture onto a surface. The default is to use the current UV coordinates, in which U is the horizontal axis and V is the vertical axis.

## Discussion

The `Cellular Noise 2D` shader node procedurally generates noise patterns that you can use to add texture and variation to materials. Below is an example of a node graph that uses the `Cellular Noise 2D` node to generate a black and white pattern procedurally:

![](https://developer.apple.com/tutorials/images/ShaderGraph-Docs/CellNoise2dGraph.png)

Multiply the incoming texture coordinates with a constant float. The float changes the frequency of the generated noise to a higher number that corresponds with the pattern repeating more often. The output of the node runs through a `Convert` node to change the float output to a black and white color output: Below, the resulting texture applies to a cube:

![](https://developer.apple.com/tutorials/images/ShaderGraph-Docs/CellNoise2dMaterial.png)

## See Also

### Nodes
- [Ramp Horizontal](./ramp-horizontal.md)
  A left-to-right linear value ramp (gradient) generator.
- [Ramp Vertical](./ramp-vertical.md)
  A top-to-bottom linear value ramp (gradient) generator.
- [Ramp 4 Corners](./ramp-4-corners.md)
  A four-point linear value ramp (gradient) generator.
- [Split Horizontal](./split-horizontal.md)
  A left-to-right split matte, split at a specified U value.
- [Split Vertical](./split-vertical.md)
  A top-to-bottom split matte, split at a specified V value.
- [Noise 2D](./noise-2d.md)
  A 2D Perlin noise generator.
- [Worley Noise 2D](./worley-noise-2d.md)
  A 2D Worley noise generator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/shadergraph/2d-procedural/cellular-noise-2d)*