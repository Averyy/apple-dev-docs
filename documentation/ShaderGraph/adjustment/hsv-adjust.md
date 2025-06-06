# HSV Adjust

**Framework**: ShaderGraph  
**Kind**: subscript

Adjusts the hue, saturation and value of an RGB color by a vector .

#### Parameter Types

#### Parameter Descriptions

#### Discussion

The HSV Adjust node adjusts the hue, saturation, and value of the color passed to the `In` parameter. The node performs this adjustment by adding the first value of the `Amount` vector to the hue, multiplying the saturation by the second value of the `Amount` vector, and multiplying that value by the third value of the `Amount` vector. When adjusting the hue, a positive value rotates the hue in the direction of red to green to blue. A value of 1 represents an entire rotation, and results in no change.

> **Note**: This node never changes the alpha of a `color4`.

This node never changes the alpha of a `color4`.

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
- [Contrast](adjustment/contrast.md)
  Increases or decreases contrast of values using a linear slope multiplier.
- [Range](adjustment/range.md)
  Remaps incoming values from one range to another.
- [Saturate](adjustment/saturate.md)
  Adjusts the saturation of a color.
- [Step (RealityKit)](adjustment/step-(realitykit).md)
  Outputs a 1 or a 0 depending on whether the input is greater than or less than the edge value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/shadergraph/adjustment/hsv-adjust)*