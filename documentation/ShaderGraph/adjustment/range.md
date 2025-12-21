# Range

**Framework**: ShaderGraph  
**Kind**: subscript

Remaps incoming values from one range to another.

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

The `Range` node takes a range of incoming values and converts them to another range. The node also provides the option to apply a gamma correction, which occurs in the middle of the transformation process. The gamma value is the inverse exponent the node applies to the  incoming values. For example, a value of `2` raises the incoming values to the power of `1/2`, effectively calculating the square root. The node also provides the option to clamp the output, which means any values below the `Out Low` parameter are set to the value of `Out Low`, and any values above the `Out High` parameter are set to value of `Out High`.

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
- [HSV Adjust](adjustment/hsv-adjust.md)
  Adjusts the hue, saturation and value of an RGB color by a vector .
- [Saturate](adjustment/saturate.md)
  Adjusts the saturation of a color.
- [Step (RealityKit)](adjustment/step-(realitykit).md)
  Outputs a 1 or a 0 depending on whether the input is greater than or less than the edge value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/shadergraph/adjustment/range)*