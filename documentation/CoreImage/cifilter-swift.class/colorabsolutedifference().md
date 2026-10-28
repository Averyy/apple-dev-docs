# colorAbsoluteDifference()

**Framework**: Core Image  
**Kind**: method  
**Role**: Type Method

Calculates the absolute difference between each color component in the input images.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
class func colorAbsoluteDifference() -> any CIFilter & CIColorAbsoluteDifference
```

```objc
+ (CIFilter<CIColorAbsoluteDifference> *) colorAbsoluteDifferenceFilter;
```

## Return Value

An image containing the absolute color difference between the two input images.

## Discussion

This method applies the color absolute difference filter to an image. This filter calculates the absolute color difference of the red, green, and blue values between the two input images. The alpha channel is the product of the alpha channels from the two input images.

The absolute difference filter uses the following properties:

- **`inputImage`**: The first [`CIImage`](../ciimage.md) for differencing.
- **`inputImage2`**: The second [`CIImage`](../ciimage.md) for differencing.

The following code creates a filter that results in the color difference between two images:

```swift
func colorAbsolute(inputImage: CIImage, inputImage2: CIImage) -> CIImage {
    let filter = CIFilter.colorAbsoluteDifference()
    filter.inputImage = inputImage
    filter.inputImage2 = inputImage2
    return filter.outputImage!
}
```

![Three images arranged with two images on the left and an image on the right. The top left image is a solid green color, and the bottom left image is a single palm tree with a clear sky. The right image shows the result of applying the color absolute difference filter to the two images on the left. The palm tree is now highlighted against the background.](https://developer.apple.com/tutorials/images/com.apple.coreimage/media-4332166@2x.png)

## See Also

### Filters
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
- [class func toneCurve() -> any CIFilter & CIToneCurve](./tonecurve%28%29.md)
  Alters an image’s tone curve according to a series of data points.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifilter-swift.class/colorabsolutedifference())*