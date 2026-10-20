# temperatureAndTint()

**Framework**: Core Image  
**Kind**: method  
**Role**: Type Method

Alters an image’s temperature and tint.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class func temperatureAndTint() -> any CIFilter & CITemperatureAndTint
```

```objc
+ (CIFilter<CITemperatureAndTint> *) temperatureAndTintFilter;
```

#### Return Value

The modified image.

#### Discussion

This method applies the image temperature and tint filter to an image. The effect adjusts the white balance of the input image to match the `targetNeutral` property, resulting in a cooler or warmer tone image.

The temperature and tint filter uses the following properties:

- **`neutral`**: A `vector` containing the source white point as a [`CIVector`](../civector.md).
- **`targetNeutral`**: A vector containing the desired white point as a [`CIVector`](../civector.md).
- **`inputImage`**: An image with the type [`CIImage`](../ciimage.md).

The following code creates a filter that adds an orange hue to the input image:

```swift
func tempatureAndTint(inputImage: CIImage) -> CIImage {
    let tempatureAndTintFilter = CIFilter.temperatureAndTint()
    tempatureAndTintFilter.inputImage = inputImage
    tempatureAndTintFilter.neutral = CIVector(x: 11500, y: 10)
    tempatureAndTintFilter.targetNeutral = CIVector(x: 4000, y: 0)
    return tempatureAndTintFilter.outputImage!
}
```

![Two versions of a photograph side by side. The photo on the left shows a small bunch of flowers photographed close up, in focus, with good light and no effects. In the photo on the right, a temperature and tint filter is applied, resulting in a orange hue applied to the image.](https://developer.apple.com/tutorials/images/com.apple.coreimage/media-3545008@2x.png)

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
- [class func toneCurve() -> any CIFilter & CIToneCurve](./tonecurve%28%29.md)
  Alters an image’s tone curve according to a series of data points.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifilter-swift.class/temperatureandtint())*