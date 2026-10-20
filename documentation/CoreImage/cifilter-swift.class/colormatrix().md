# colorMatrix()

**Framework**: Core Image  
**Kind**: method  
**Role**: Type Method

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

```objc
+ (CIFilter<CIColorMatrix> *) colorMatrixFilter;
```

## Mentions

- [Simulating Scratchy Analog Film](../simulating-scratchy-analog-film.md)

#### Return Value

The modified image.

#### Discussion

This method applies the color matrix filter to an image. The effect calculates the color matrix by multiplying the vector properties with the color values from the input image.

The color matrix filter uses the following properties:

- **`rVector`**: A [`CIVector`](../civector.md) representing the amount of red to multiply the source color values by.
- **`gVector`**: A [`CIVector`](../civector.md) representing the amount of green to multiply the source color values by.
- **`bVector`**: A [`CIVector`](../civector.md) representing the amount of blue to multiply the source color values by.
- **`aVector`**: A [`CIVector`](../civector.md) representing the amount of alpha to multiply the source color values by.
- **`biasVector`**: A [`CIVector`](../civector.md) representing the amount of each vector that’s added to each color component.
- **`inputImage`**: An image with the type [`CIImage`](../ciimage.md).

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

![Two versions of a photograph side by side. The photo on the left shows a small bunch of flowers photographed close up, in focus, with good light and no effects. In the photo on the right, a color matrix filter is applied, transforming the colors in the image to have a green hue.](https://developer.apple.com/tutorials/images/com.apple.coreimage/media-3544998@2x.png)

## See Also

### Filters
- [class func colorAbsoluteDifference() -> any CIFilter & CIColorAbsoluteDifference](./colorabsolutedifference%28%29.md)
  Calculates the absolute difference between each color component in the input images.
- [class func colorClamp() -> any CIFilter & CIColorClamp](./colorclamp%28%29.md)
  Alters the colors in an image based on color components.
- [class func colorControls() -> any CIFilter & CIColorControls](./colorcontrols%28%29.md)
  Alters the brightness, contrast, and saturation of an image’s colors.
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

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifilter-swift.class/colormatrix())*