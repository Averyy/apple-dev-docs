# colorThresholdOtsu()

**Framework**: Core Image  
**Kind**: method  
**Role**: Type Method

Compares the red, green, and blue components of the input image against a threshold calculated using Otsu’s algorithm.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
class func colorThresholdOtsu() -> any CIFilter & CIColorThresholdOtsu
```

```objc
+ (CIFilter<CIColorThresholdOtsu> *) colorThresholdOtsuFilter;
```

## Return Value

An image containing pixels with color components that are either 1 or 0.

## Discussion

The filter applies Otsu’s algorithm to the reg, green, and blue color components. The filter uses these thresholds to set the color to components to 1 or 0. The alpha component remains unchanged.

The color threshold Otsu filter uses the following property:

- **`inputImage`**: An image with the type [`CIImage`](../ciimage.md).

The following code creates a filter that results in an image where each color component is either 1 or 0:

```swift
func colorThresholdOTSU(inputImage: CIImage) -> CIImage {
    let filter = CIFilter.colorThresholdOtsu()
    filter.inputImage = inputImage
    return filter.outputImage!
}
```

![Two images arranged horizontally. The left image contains a photograph of a modern building with light colored concrete set against a clear sky. The image on the right shows the result of applying the color threshold Otsu filter. The light colored concrete is now set to bright white and the sky is set to fully saturated blue. ](https://developer.apple.com/tutorials/images/com.apple.coreimage/media-4407336@2x.png)

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

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifilter-swift.class/colorthresholdotsu())*