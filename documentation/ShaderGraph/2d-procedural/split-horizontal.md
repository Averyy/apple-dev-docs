# Split Horizontal

**Framework**: ShaderGraph  
**Kind**: subscript

A left-to-right split matte, split at a specified U value.

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

This node creates two distinct regions along the horizontal axis. The value of the `Center` input determines these regions. A value of `0` establishes the center at the left-most position, causing the output to always be equal to the `Right` input. A value of `1` establishes the center at the right-most position. Below is a an example of a simple node graph that uses `Split Horizontal` to create a split color:

![None](https://docs-assets.developer.apple.com/published/459511dd7149b3269154ec05b39ee336/SplitHorizontalGraph.png)

By editing the center value, you change the texture to show a larger left or right region. The image below shows the resulting textures:

![None](https://docs-assets.developer.apple.com/published/5920a6f7e93c7bce9bd9992da86620cb/SplitHorizontalMaterial1.png)

## See Also

- [Ramp Horizontal](2d-procedural/ramp-horizontal.md)
  A left-to-right linear value ramp (gradient) generator.
- [Ramp Vertical](2d-procedural/ramp-vertical.md)
  A top-to-bottom linear value ramp (gradient) generator.
- [Ramp 4 Corners](2d-procedural/ramp-4-corners.md)
  A four-point linear value ramp (gradient) generator.
- [Split Vertical](2d-procedural/split-vertical.md)
  A top-to-bottom split matte, split at a specified V value.
- [Noise 2D](2d-procedural/noise-2d.md)
  A 2D Perlin noise generator.
- [Cellular Noise 2D](2d-procedural/cellular-noise-2d.md)
  A 2D cellular noise generator.
- [Worley Noise 2D](2d-procedural/worley-noise-2d.md)
  A 2D Worley noise generator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/shadergraph/2d-procedural/split-horizontal)*