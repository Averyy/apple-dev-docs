# Cellular Noise 2D

**Framework**: ShaderGraph  
**Kind**: subscript

A 2D cellular noise generator.

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

The `Cellular Noise 2D` shader node procedurally generates noise patterns that you can use to add texture and variation to materials. Below is an example of a node graph that uses the `Cellular Noise 2D` node to generate a black and white pattern procedurally:

![None](https://docs-assets.developer.apple.com/published/e7cba5b397d0b79f7db7a9a072b3e93d/CellNoise2dGraph.png)

Multiply the incoming texture coordinates with a constant float. The float changes the frequency of the generated noise to a higher number that corresponds with the pattern repeating more often. The output of the node runs through a `Convert` node to change the float output to a black and white color output: Below, the resulting texture applies to a cube:

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