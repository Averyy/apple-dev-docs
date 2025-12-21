# Ramp 4 Corners

**Framework**: ShaderGraph  
**Kind**: subscript

A four-point linear value ramp (gradient) generator.

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

This node uses bilinear interpolation to create a ramp from four corner values. Any point within the output ramp is a mix of one of the four corner values. A given point is more similar to a corner value the closer its position is to that corner. Below is a an example of a simple node graph that uses `Ramp 4 Corners` to create a gradient with four different colors:

![None](https://docs-assets.developer.apple.com/published/1778842288c4d7928f63c92b5eb32703/Ramp4Graph.png)

The image below shows the resulting texture along with the color values on each corner:

![None](https://docs-assets.developer.apple.com/published/1d6fc6df1e54b2e218c0941bff4530e0/Ramp4Material.png)

## See Also

- [Ramp Horizontal](2d-procedural/ramp-horizontal.md)
  A left-to-right linear value ramp (gradient) generator.
- [Ramp Vertical](2d-procedural/ramp-vertical.md)
  A top-to-bottom linear value ramp (gradient) generator.
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

*[View on Apple Developer](https://developer.apple.com/documentation/shadergraph/2d-procedural/ramp-4-corners)*