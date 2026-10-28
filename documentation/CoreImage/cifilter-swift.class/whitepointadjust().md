# whitePointAdjust()

**Framework**: Core Image  
**Kind**: method  
**Role**: Type Method

Adjusts the image’s white-point.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class func whitePointAdjust() -> any CIFilter & CIWhitePointAdjust
```

```objc
+ (CIFilter<CIWhitePointAdjust> *) whitePointAdjustFilter;
```

## Return Value

The modified image.

## Discussion

This method applies the white-point adjust filter to an image. The effect adjusts the white-point of the input image by mapping all shades of gray to shades of the color property.

The white-point adjust filter uses the following properties:

- **`color`**: The new white point color with the type of [`CIColor`](../cicolor.md).
- **`inputImage`**: An image with the type [`CIImage`](../ciimage.md).

The following code creates a filter that adds a red hue to the input image:

```swift
func whitePoint(inputImage: CIImage) -> CIImage {
    let whitePointFilter = CIFilter.whitePointAdjust()
    whitePointFilter.inputImage = inputImage
    whitePointFilter.color = CIColor(red: 1, green: 0.6, blue: 0.6, alpha: 1)
    return whitePointFilter.outputImage!
}
```

![Two versions of a photograph side by side. The photo on the left shows a small bunch of flowers photographed close up, in focus, with good light and no effects. In the photo on the right, a white point adjust filter is applied, resulting in a pink hue added to the entire image.](https://developer.apple.com/tutorials/images/com.apple.coreimage/media-3545004@2x.png)

## See Also

### Filters
- [class func colorAbsoluteDifference() -> any CIFilter & CIColorAbsoluteDifference](./colorabsolutedifference%28%29.md)
  Calculates the absolute difference between each color component in the input images.
- [class func colorClamp() -> any CIFilter & CIColorClamp](./colorclamp%28%29.md)
  Alters the colors in an image based on color components.
- [class func colorControls() -> any CIFilter & CIColorControls](./colorcontrols%28%29.md)
  Alters the brightness, contrast, and saturation of an image’s colors.
- [class func colorMatrix() -> any CIFilter & CIColorMatrix](./colormatrix%28%29.md)
  Alters the colors in an image based on vectors provided.
- [class func colorPolynomial() -> any CIFilter & CIColorPolynomial](./colorpolynomial%28%29.md)
  Alters an image’s colors.
- [class func colorThreshold() -> any CIFilter & CIColorThreshold](./colorthreshold%28%29.md)
  Compares the red, green, and blue components of the input image to a threshold and sets them to 1 or 0.
- [class func colorThresholdOtsu() -> any CIFilter & CIColorThresholdOtsu](./colorthresholdotsu%28%29.md)
  Compares the red, green, and blue components of the input image against a threshold calculated using Otsu’s algorithm.
- [class func depthToDisparity() -> any CIFilter & CIDepthToDisparity](./depthtodisparity%28%29.md)
  Converts from an image containing depth data to an image containing disparity data.
- [class func disparityToDepth() -> any CIFilter & CIDisparityToDepth](./disparitytodepth%28%29.md)
  Creates depth data from an image containing disparity data.
- [class func exposureAdjust() -> any CIFilter & CIExposureAdjust](./exposureadjust%28%29.md)
  Adjusts an image’s exposure.
- [class func gammaAdjust() -> any CIFilter & CIGammaAdjust](./gammaadjust%28%29.md)
  Alters an image’s transition between black and white.
- [class func hueAdjust() -> any CIFilter & CIHueAdjust](./hueadjust%28%29.md)
  Modifies an image’s hue.
- [class func linearToSRGBToneCurve() -> any CIFilter & CILinearToSRGBToneCurve](./lineartosrgbtonecurve%28%29.md)
  Alters an image’s color intensity.
- [class func sRGBToneCurveToLinear() -> any CIFilter & CISRGBToneCurveToLinear](./srgbtonecurvetolinear%28%29.md)
  Converts the colors in an image from sRGB to linear.
- [class func temperatureAndTint() -> any CIFilter & CITemperatureAndTint](./temperatureandtint%28%29.md)
  Alters an image’s temperature and tint.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifilter-swift.class/whitepointadjust())*