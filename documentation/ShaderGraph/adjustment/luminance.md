# Luminance

**Framework**: ShaderGraph  
**Kind**: subscript

Outputs a grayscale value containing the luminance of the incoming RGB color in all color channels.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 26.0+
- visionOS 1.0+

#### Parameter Types

#### Parameter Descriptions

- **`In`**: The input to convert to grayscale.
- **`Luma Coefficients`**: The luma coefficients of the color space. The possible values for this node are the luma coeffiecients for the color spaces `acescg`, `rec202/rec2100`, or `rec709`. The default value is the luma coeffiecients for `acescg`, which are `(0.2722287, 0.6740818, 0.0536895)`.

#### Discussion

The Luminance node takes in a color input and outputs that input as a grayscale image. The node computes the grayscale of an image by taking the dot product of the luma coefficients and the color vector. Below is an example of a simple node graph that uses the luminance node to convert an image to grayscale:

![None](/images/ShaderGraph-Docs/LuminanceGraph.png)

Below, the resulting texture applies to a cube:

![None](/images/ShaderGraph-Docs/LuminanceMaterial.png)

## See Also

- [Remap](adjustment/remap.md)
  Linearly remaps incoming values from one range to another.
- [Smooth Step](adjustment/smooth-step.md)
  Outputs a smooth remapping from low-high to 0-1.
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

*[View on Apple Developer](https://developer.apple.com/documentation/shadergraph/adjustment/luminance)*