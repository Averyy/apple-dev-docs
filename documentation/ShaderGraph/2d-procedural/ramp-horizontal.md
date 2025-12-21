# Ramp Horizontal

**Framework**: ShaderGraph  
**Kind**: subscript

A left-to-right linear value ramp (gradient) generator.

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

This node uses interpolation to create a horizontal ramp or gradient from two values. Any point within the output ramp is a mix of the two values. A given point is more similar to the value that its horizontal position is closer to. Below is a an example of a simple node graph that uses `Ramp Horizontal` to create a color gradient:

![None](https://docs-assets.developer.apple.com/published/262f1f12dc34a4ffc9d1065f449f1c8c/RampHorizontalGraph.png)

The image below shows the resulting texture, along with the color values on either side:

![None](https://docs-assets.developer.apple.com/published/be3386c09c6ce3c9d3076223b98fea13/RampHorizontalMaterial.png)

## See Also

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
- [Cellular Noise 2D](2d-procedural/cellular-noise-2d.md)
  A 2D cellular noise generator.
- [Worley Noise 2D](2d-procedural/worley-noise-2d.md)
  A 2D Worley noise generator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/shadergraph/2d-procedural/ramp-horizontal)*