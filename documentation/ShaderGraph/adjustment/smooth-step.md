# Smooth Step

**Framework**: ShaderGraph  
**Kind**: subscript

Outputs a smooth remapping from low-high to 0-1.

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

The `Smooth Step` node outputs a smooth remapping using Hermite interpolation. Any input with a value lower than the `Low` parameter results in an output of `0`. Any input with a value higher than the `High` parameter results in an output of `1`.

## See Also

- [Remap](adjustment/remap.md)
  Linearly remaps incoming values from one range to another.
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
- [Saturate](adjustment/saturate.md)
  Adjusts the saturation of a color.
- [Step (RealityKit)](adjustment/step-(realitykit).md)
  Outputs a 1 or a 0 depending on whether the input is greater than or less than the edge value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/shadergraph/adjustment/smooth-step)*