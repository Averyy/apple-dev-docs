# Ramp Vertical

**Framework**: ShaderGraph  
**Kind**: subscript

A top-to-bottom linear value ramp (gradient) generator.

#### Parameter Types

#### Parameter Descriptions

#### Discussion

This node uses interpolation to create a vertical ramp or gradient from two values. Any point within the output ramp is a mix of the two values. A given point is more similar to the value that its vertical position is closer to. Below is a an example of a simple node graph that uses Ramp Vertical to create a color gradient.

![None](https://docs-assets.developer.apple.com/published/fe4213c8fa2452496e89ae10982502ab/RampVerticalGraph.png)

The image below shows the resulting texture, along with the color values on either side.

![None](https://docs-assets.developer.apple.com/published/03252167c26d5947d2711bff9736ac34/RampVerticalMaterial.png)

## See Also

- [Ramp Horizontal](2d-procedural/ramp-horizontal.md)
  A left-to-right linear value ramp (gradient) generator.
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

*[View on Apple Developer](https://developer.apple.com/documentation/shadergraph/2d-procedural/ramp-vertical)*