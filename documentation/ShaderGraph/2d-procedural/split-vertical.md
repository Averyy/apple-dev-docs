# Split Vertical

**Framework**: ShaderGraph  
**Kind**: subscript

A top-to-bottom split matte, split at a specified V value.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 26.0+ (Beta)
- visionOS 1.0+

#### Parameter Types

#### Parameter Description

#### Discussion

This node creates two distinct regions along the vertical axis. The value of the `Center` input determines the regions. A value of `0` establishes the center at the top-most, position causing the output to always be equal to the `Top` input. A value of `1` establishes the center at the bottom-most position. Below is a an example of a simple node graph that uses `Split Vertical` to create a split color:

![None](https://docs-assets.developer.apple.com/published/4c238efca001e7e1d912c0d1b322cfd9/SplitVerticalGraph.png)

By editing the center value, you change the texture to show a larger top or bottom region. The image below shows the resulting textures:

![None](https://docs-assets.developer.apple.com/published/e93fc156dba3409fa1a0c50ceaeda4f9/SplitVerticalMaterial1.png)

## See Also

- [Ramp Horizontal](2d-procedural/ramp-horizontal.md)
  A left-to-right linear value ramp (gradient) generator.
- [Ramp Vertical](2d-procedural/ramp-vertical.md)
  A top-to-bottom linear value ramp (gradient) generator.
- [Ramp 4 Corners](2d-procedural/ramp-4-corners.md)
  A four-point linear value ramp (gradient) generator.
- [Split Horizontal](2d-procedural/split-horizontal.md)
  A left-to-right split matte, split at a specified U value.
- [Noise 2D](2d-procedural/noise-2d.md)
  A 2D Perlin noise generator.
- [Cellular Noise 2D](2d-procedural/cellular-noise-2d.md)
  A 2D cellular noise generator.
- [Worley Noise 2D](2d-procedural/worley-noise-2d.md)
  A 2D Worley noise generator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/shadergraph/2d-procedural/split-vertical)*