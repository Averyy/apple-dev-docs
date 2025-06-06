# Worley Noise 3D

**Framework**: ShaderGraph  
**Kind**: subscript

A 3D Worley noise generator.

#### Parameter Types

#### Parameter Descriptions

#### Discussion

The Worley Noise 3D node procedurally generates nonuniform cellular regions. The node creates a finite number of center points, and each region is a polygon that surrounds the points closest to each center point. Because this node generates noise in 3D, the texture doesn’t repeat in the Z direction but rather continues as depth changes. Below is an example of a simple node graph that uses the Worley Noise 3D node to generate a black and white pattern procedurally.

![None](https://docs-assets.developer.apple.com/published/93e069365411ee3b9980bbaac0872c99/WorleyNoise3dGraph.png)

Multiply the incoming texture coordinates with a constant float, which changes the frequency of the generated noise. A higher value corresponds to the pattern repeating more often. Then run the output through a convert node to change it to a black and white color value.
Below, the resulting texture applies to a cube.

![None](https://docs-assets.developer.apple.com/published/bdf0fcb2dbd86638217094fcc5ebedc6/WorleyNoise3dMaterial.png)

## See Also

- [Noise 3D](3d-procedural/noise-3d.md)
  A 3D Perlin noise generator.
- [Fractal Noise 3D](3d-procedural/fractal-noise-3d.md)
  Zero-centered 3D fractal noise created by summing several octaves of 3D Perlin noise.
- [Cellular Noise 3D](3d-procedural/cellular-noise-3d.md)
  A 3D cellular noise generator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/shadergraph/3d-procedural/worley-noise-3d)*