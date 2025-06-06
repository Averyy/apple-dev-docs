# Saturate

**Framework**: Shadergraph  
**Kind**: subscript

Adjusts the saturation of a color.

#### Parameter Types

#### Parameter Descriptions

#### Discussion

The Saturate node performs a linear interpolation between the incoming color value and the luminance of the incoming color value. Setting the value of the `Amount` parameter to `0` adjusts the output to a grayscale of the input equal to the value that the [`Luminance`](adjustment/luminance.md) would output.

> **Note**: The effect of this node isn’t equivalent to adjusting saturation with the [`HSV Adjust`](adjustment/hsv-adjust.md) node. The Saturate node takes into account a colorspace when processing its modifications.

Below is an example of a simple node graph that uses the Saturate node to modify the saturation of an image.

![None](https://docs-assets.developer.apple.com/published/53fe35cf80e429ddc0ea359e9d067a7c/SaturateGraph.png)

Below, the resulting texture applies to a cube.

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
- [HSV Adjust](adjustment/hsv-adjust.md)
  Adjusts the hue, saturation and value of an RGB color by a vector .
- [Step (RealityKit)](adjustment/step-(realitykit).md)
  Outputs a 1 or a 0 depending on whether the input is greater than or less than the edge value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/shadergraph/adjustment/saturate)*