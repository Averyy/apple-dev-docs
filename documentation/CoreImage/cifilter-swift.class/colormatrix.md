# colorMatrix()

**Framework**: Core Image  
**Kind**: method

Alters the colors in an image based on vectors provided.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class func colorMatrix() -> any CIFilter & CIColorMatrix
```

## Mentions

- [Simulating Scratchy Analog Film](simulating-scratchy-analog-film.md)

#### Return Value

The modified image.

#### Discussion

This method applies the color matrix filter to an image. The effect calculates the color matrix by multiplying the vector properties with the color values from the input image.

The color matrix filter uses the following properties:

The following code creates a filter that adds a green hue to the input image:

```swift
func colorMatrix(inputImage: CIImage) -> CIImage {
    let colorMatrixFilter = CIFilter.colorMatrix()
    colorMatrixFilter.inputImage = inputImage
    colorMatrixFilter.rVector = CIVector (x: 1, y: 0, z: 0.2, w: 0)
    colorMatrixFilter.gVector = CIVector (x: 0, y: 1, z: 0, w: 0.9)
    colorMatrixFilter.bVector = CIVector (x: 0, y: 0, z: 1, w: 0)
    colorMatrixFilter.aVector = CIVector (x: 0, y: 0, z: 0, w: 1)
    colorMatrixFilter.biasVector = CIVector (x: 0, y: 0, z: 0, w: 0)
    return colorMatrixFilter.outputImage!
}
```

![Two versions of a photograph side by side. The photo on the left shows a small bunch of flowers photographed close up, in focus, with good light and no effects. In the photo on the right, a color matrix filter is applied, transforming the colors in the image to have a green hue.](https://docs-assets.developer.apple.com/published/ac7fc9aa7c63ddf5ba37706d1006f2bf/media-3544998%402x.png)

## See Also

- [class func colorAbsoluteDifference() -> any CIFilter & CIColorAbsoluteDifference](cifilter-swift.class/colorabsolutedifference.md)
  Calculates the absolute difference between each color component in the input images.
- [class func colorClamp() -> any CIFilter & CIColorClamp](cifilter-swift.class/colorclamp.md)
  Alters the colors in an image based on color components.
- [class func colorControls() -> any CIFilter & CIColorControls](cifilter-swift.class/colorcontrols.md)
  Alters the brightness, contrast, and saturation of an image’s colors.
- [class func colorPolynomial() -> any CIFilter & CIColorPolynomial](cifilter-swift.class/colorpolynomial.md)
  Alters an image’s colors.
- [class func colorThreshold() -> any CIFilter & CIColorThreshold](cifilter-swift.class/colorthreshold.md)
  Compares the red, green, and blue components of the input image to a threshold and sets them to 1 or 0.
- [class func colorThresholdOtsu() -> any CIFilter & CIColorThresholdOtsu](cifilter-swift.class/colorthresholdotsu.md)
  Compares the red, green, and blue components of the input image against a threshold calculated using Otsu’s algorithm.
- [class func depthToDisparity() -> any CIFilter & CIDepthToDisparity](cifilter-swift.class/depthtodisparity.md)
  Converts from an image containing depth data to an image containing disparity data.
- [class func disparityToDepth() -> any CIFilter & CIDisparityToDepth](cifilter-swift.class/disparitytodepth.md)
  Creates depth data from an image containing disparity data.
- [class func exposureAdjust() -> any CIFilter & CIExposureAdjust](cifilter-swift.class/exposureadjust.md)
  Adjusts an image’s exposure.
- [class func gammaAdjust() -> any CIFilter & CIGammaAdjust](cifilter-swift.class/gammaadjust.md)
  Alters an image’s transition between black and white.
- [class func hueAdjust() -> any CIFilter & CIHueAdjust](cifilter-swift.class/hueadjust.md)
  Modifies an image’s hue.
- [class func linearToSRGBToneCurve() -> any CIFilter & CILinearToSRGBToneCurve](cifilter-swift.class/lineartosrgbtonecurve.md)
  Alters an image’s color intensity.
- [class func sRGBToneCurveToLinear() -> any CIFilter & CISRGBToneCurveToLinear](cifilter-swift.class/srgbtonecurvetolinear.md)
  Converts the colors in an image from sRGB to linear.
- [class func temperatureAndTint() -> any CIFilter & CITemperatureAndTint](cifilter-swift.class/temperatureandtint.md)
  Alters an image’s temperature and tint.
- [class func toneCurve() -> any CIFilter & CIToneCurve](cifilter-swift.class/tonecurve.md)
  Alters an image’s tone curve according to a series of data points.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifilter-swift.class/colormatrix())*