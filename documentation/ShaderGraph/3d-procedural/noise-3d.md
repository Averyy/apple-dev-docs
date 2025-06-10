# Noise 3D

**Framework**: ShaderGraph  
**Kind**: subscript

A 3D Perlin noise generator.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 26.0+ (Beta)
- visionOS 1.0+

#### Parameter Types

#### Parameter Descriptions

#### Discussion

The Noise 3D shader node procedurally generates Perlin noise patterns you can use to add texture and variation to materials. All noise values that are procedurally generated are numbers between `0` and `1` before the amplitude and pivot are applied. Because this node generates noise in 3D, the texture doesn’t repeat in the Z direction, but rather continues as depth changes. Below is an example of a simple node graph that uses the Noise 3D node to generate a black and white pattern procedurally:

![None](https://docs-assets.developer.apple.com/published/b8c62b146b40ba2082029f77b5a5af71/Noise3dGraph.png)

Multiply the incoming position with a constant float. The float changes the frequency of the generated noise to a higher number that corresponds with the pattern repeating more often. Below, the resulting texture applies to a cube:

![None](https://docs-assets.developer.apple.com/published/b6f5f45d5a71fedd0f03b2c4ee7f1a0d/Noise3dMaterial.png)

## See Also

- [Fractal Noise 3D](3d-procedural/fractal-noise-3d.md)
  Zero-centered 3D fractal noise created by summing several octaves of 3D Perlin noise.
- [Cellular Noise 3D](3d-procedural/cellular-noise-3d.md)
  A 3D cellular noise generator.
- [Worley Noise 3D](3d-procedural/worley-noise-3d.md)
  A 3D Worley noise generator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/shadergraph/3d-procedural/noise-3d)*