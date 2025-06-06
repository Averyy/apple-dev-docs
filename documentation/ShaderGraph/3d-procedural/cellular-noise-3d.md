# Cellular Noise 3D

**Framework**: ShaderGraph  
**Kind**: subscript

A 3D cellular noise generator.

#### Parameter Types

#### Parameter Descriptions

#### Discussion

The Cellular Noise 3D shader node procedurally generates noise patterns that can be used to add texture and variation to materials. Because this node generates noise in 3D, the texture will not repeat in the Z direction, but rather continue as depth changes. Below is an example of a simple node graph that uses the Cellular Noise 3D Node to generate a black and white pattern procedurally.

![None](https://docs-assets.developer.apple.com/published/4200e6f88d1d15770127a796b6cd87fc/CellNoise3dGraph.png)

Multiply the incoming position with a constant float. The float changes the frequency of the generated noise to a higher number that corresponds with the pattern repeating more often. The output of the node runs through a convert node in order to change the float output to a black and white color output. Below, the resulting texture applies to a cube.

![None](https://docs-assets.developer.apple.com/published/948eeb46004585adcd3e7ac2b89e1fc0/CellNoise3dMaterial.png)

## See Also

- [Noise 3D](3d-procedural/noise-3d.md)
  A 3D Perlin noise generator.
- [Fractal Noise 3D](3d-procedural/fractal-noise-3d.md)
  Zero-centered 3D fractal noise created by summing several octaves of 3D Perlin noise.
- [Worley Noise 3D](3d-procedural/worley-noise-3d.md)
  A 3D Worley noise generator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/shadergraph/3d-procedural/cellular-noise-3d)*