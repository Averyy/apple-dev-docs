# Contrast

**Framework**: ShaderGraph  
**Kind**: subscript

Increases or decreases contrast of values using a linear slope multiplier.

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

Below is an example of a node graph that uses the `Contrast` node to make a black and white arrow texture more gray and closer in color.

![None](https://docs-assets.developer.apple.com/published/b875b7e718e1101dcab31f42da00ba66/ContrastGraph.png)

Below, the resulting texture applies to a cube:

![None](https://docs-assets.developer.apple.com/published/b5031fa1f42bfc35c8ab51be05d66b6d/ContrastMaterial.png)

In the image above, the value of `Pivot` is `0.2`, which represents a dark gray. Because the value of `Amount` is also `0.2`, the contrast of the input decreases while the color value of the texture moves closer to the `Pivot` input. As a result, the output texture of the node becomes a gray version of the original black and white arrow texture.

## See Also

- [Remap](adjustment/remap.md)
  Linearly remaps incoming values from one range to another.
- [Smooth Step](adjustment/smooth-step.md)
  Outputs a smooth remapping from low-high to 0-1.
- [Luminance](adjustment/luminance.md)
  Outputs a grayscale value containing the luminance of the incoming RGB color in all color channels.
- [RGB to HSV](adjustment/rgb-to-hsv.md)
  Converts a color from RGB to HSV space.
- [HSV to RGB](adjustment/hsv-to-rgb.md)
  Converts a color from HSV to RGB space.
- [Range](adjustment/range.md)
  Remaps incoming values from one range to another.
- [HSV Adjust](adjustment/hsv-adjust.md)
  Adjusts the hue, saturation and value of an RGB color by a vector .
- [Saturate](adjustment/saturate.md)
  Adjusts the saturation of a color.
- [Step (RealityKit)](adjustment/step-(realitykit).md)
  Outputs a 1 or a 0 depending on whether the input is greater than or less than the edge value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/shadergraph/adjustment/contrast)*