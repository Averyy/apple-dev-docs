# Step (RealityKit)

**Framework**: ShaderGraph  
**Kind**: subscript

Outputs a 1 or a 0 depending on whether the input is greater than or less than the edge value.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 26.0+ (Beta)
- visionOS 1.0+

#### Overview

0 if X < Edge, otherwise it returns 1.0

#### Parameter Types

#### Parameter Descriptions

#### Discussion

The Step node takes the `In` value and compares it to the `Edge` parameter. If the value is less than `Edge`, the node returns `0`. Otherwise, it returns `1`.

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
- [Saturate](adjustment/saturate.md)
  Adjusts the saturation of a color.


---

*[View on Apple Developer](https://developer.apple.com/documentation/shadergraph/adjustment/step-(realitykit))*