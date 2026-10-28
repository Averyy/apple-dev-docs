# Cellular Noise 3D

**Framework**: ShaderGraph  
**Kind**: subscript  
**Role**: ShaderGraph Node

A 3D cellular noise generator.

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
| `Position` | Vector3f |

| Output | Type |
| --- | --- |
| `Out` | Float |

## Parameter descriptions

- **`Position`**: The 3D coordinates at which the data is read in order to map the texture onto a surface. The default is to use the current 3D object-space coordinates.

## Discussion

The `Cellular Noise 3D` shader node procedurally generates noise patterns that you can use to add texture and variation to materials. Because this node generates noise in 3D, the texture doesn’t repeat in the Z direction, but rather continue as depth changes. Below is an example of a node graph that uses the `Cellular Noise 3D` node to generate a black and white pattern procedurally:

![](https://developer.apple.com/tutorials/images/ShaderGraph-Docs/CellNoise3dGraph.png)

Multiply the incoming position with a constant float. The float changes the frequency of the generated noise to a higher number that corresponds with the pattern repeating more often. The output of the node runs through a `Convert` node to change the float output to a black and white color output. Below, the resulting texture applies to a cube:

![](https://developer.apple.com/tutorials/images/ShaderGraph-Docs/CellNoise3dMaterial.png)

## See Also

### Nodes
- [Noise 3D](./noise-3d.md)
  A 3D Perlin noise generator.
- [Fractal Noise 3D](./fractal-noise-3d.md)
  Zero-centered 3D fractal noise created by summing several octaves of 3D Perlin noise.
- [Worley Noise 3D](./worley-noise-3d.md)
  A 3D Worley noise generator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/shadergraph/3d-procedural/cellular-noise-3d)*