# Noise 2D

**Framework**: ShaderGraph  
**Kind**: subscript

A 2D Perlin noise generator.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 26.0+
- visionOS 1.0+

#### Parameter Types

#### Parameter Descriptions

#### Discussion

The Noise 2D shader node procedurally generates Perlin noise patterns that you can use to add texture and variation to materials. All noise values that are procedurally generated are numbers between `0` and `1` before the amplitude and pivot are applied. Below is an example of a simple node graph that uses the Noise 2D Node to generate a black and white pattern procedurally:

Image(source: “Noise2dGraph”)

Multiply the incoming texture coordinates with a constant float. The float changes the frequency of the generated noise to a higher number that corresponds with the pattern repeating more often. Below, the resulting texture applies to a cube:

![None](https://docs-assets.developer.apple.com/published/0731a19532c2cf80f4640eb844465f64/Noise2dMaterial.png)

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
- [Cellular Noise 2D](2d-procedural/cellular-noise-2d.md)
  A 2D cellular noise generator.
- [Worley Noise 2D](2d-procedural/worley-noise-2d.md)
  A 2D Worley noise generator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/shadergraph/2d-procedural/noise-2d)*