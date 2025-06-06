# Cellular Noise 2D

**Framework**: ShaderGraph  
**Kind**: subscript

A 2D cellular noise generator.

#### Parameter Types

#### Parameter Descriptions

#### Discussion

The Cellular Noise 2D shader node procedurally generates noise patterns that can be used to add texture and variation to materials. Below is an example of a simple node graph that uses the Cellular Noise 2D Node to generate a black and white pattern procedurally.

![None](https://docs-assets.developer.apple.com/published/e7cba5b397d0b79f7db7a9a072b3e93d/CellNoise2dGraph.png)

Multiply the incoming texture coordinates with a constant float. The float changes the frequency of the generated noise to a higher number that corresponds with the pattern repeating more often. The output of the node runs through a convert node in order to change the float output to a black and white color output. Below, the resulting texture applies to a cube.

![None](https://docs-assets.developer.apple.com/published/c346f62f96cb87deeccd42e14b529293/CellNoise2dMaterial.png)

## See Also

- [Ramp Horizontal](2d-procedural/ramp-horizontal.md)
  A left-to-right linear value ramp (gradient) generator.
- [Ramp Vertical](2d-procedural/ramp-vertical.md)
  A top-to-bottom linear value ramp (gradient) generator.
- [Ramp 4 Corners](2d-procedural/ramp-4-corners.md)
  A four-point linear value ramp (gradient) generator.
- [Split Horizontal](2d-procedural/split-horizontal.md)
  A left-to-right split matte, split at a specified U value.
- [Split Vertical](2d-procedural/split-vertical.md)
  A top-to-bottom split matte, split at a specified V value.
- [Noise 2D](2d-procedural/noise-2d.md)
  A 2D Perlin noise generator.
- [Worley Noise 2D](2d-procedural/worley-noise-2d.md)
  A 2D Worley noise generator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/shadergraph/2d-procedural/cellular-noise-2d)*