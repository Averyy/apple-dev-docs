# colorCrossPolynomial()

**Framework**: Core Image  
**Kind**: method

Adjusts an image’s color by applying polynomial cross-products.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class func colorCrossPolynomial() -> any CIFilter & CIColorCrossPolynomial
```

#### Return Value

The modified image.

#### Discussion

This method applies the color cross polynomial filter to an image. The effect targets each pixel individually and calculates the coefficients for the r`ed`, `green`, and `blue` channels according to the polynomial cross product.

The color cross-polynomial filter uses the following properties:

The following code creates a filter that adds a green hue to the input image:

```swift
    func colorCrossPolynomial(inputImage: CIImage) -> CIImage? {

        let colorCrossPolynomial = CIFilter.colorCrossPolynomial()
        let redfloatArr: [CGFloat] = [1, 1, 1, 1, 0, 0, 0, 0, 0, 0]
        let greenfloatArr: [CGFloat] = [0, 1, 1, 0, 0, 0, 0, 0, 0, 1]
        let bluefloatArr: [CGFloat] = [0, 0, 1, 0, 0, 0, 0, 1, 1, 0]

        colorCrossPolynomial.inputImage = inputImage
        colorCrossPolynomial.blueCoefficients = CIVector(values: bluefloatArr, count: bluefloatArr.count)
        colorCrossPolynomial.redCoefficients = CIVector(values: redfloatArr, count: redfloatArr.count)
        colorCrossPolynomial.greenCoefficients = CIVector(values: greenfloatArr, count: greenfloatArr.count)
        return colorCrossPolynomial.outputImage
    }
```

![Two pictures of a pink flower surrounded by foliage. The photo on the left shows a single flower photographed closeup, in focus, with good light and no effects. In the photo on the right, a color cross polynomial filter is applied, and the colors in the image have a green hue.](https://docs-assets.developer.apple.com/published/97c4618f009748914c3d6813cd800bf7/media-3545029%402x.png)

## See Also

- [class func colorCube() -> any CIFilter & CIColorCube](cifilter-swift.class/colorcube.md)
  Adjusts an image’s pixels using a three-dimensional color table.
- [class func colorCubeWithColorSpace() -> any CIFilter & CIColorCubeWithColorSpace](cifilter-swift.class/colorcubewithcolorspace.md)
  Adjusts an image’s pixels using a three-dimensional color table in specified color space.
- [class func colorCubesMixedWithMask() -> any CIFilter & CIColorCubesMixedWithMask](cifilter-swift.class/colorcubesmixedwithmask.md)
  Alters an image’s pixels using a three-dimensional color tables and a mask image.
- [class func colorCurves() -> any CIFilter & CIColorCurves](cifilter-swift.class/colorcurves.md)
  Adjusts an image’s color curves.
- [class func colorInvert() -> any CIFilter & CIColorInvert](cifilter-swift.class/colorinvert.md)
  Inverts an image’s colors.
- [class func colorMap() -> any CIFilter & CIColorMap](cifilter-swift.class/colormap.md)
  Performs a transformation of the input image colors to colors from a gradient image.
- [class func colorMonochrome() -> any CIFilter & CIColorMonochrome](cifilter-swift.class/colormonochrome.md)
  Adjusts an image’s colors to shades of a single color.
- [class func colorPosterize() -> any CIFilter & CIColorPosterize](cifilter-swift.class/colorposterize.md)
  Flattens an image’s colors.
- [class func convertLabToRGB() -> any CIFilter & CIConvertLab](cifilter-swift.class/convertlabtorgb.md)
  Converts an image from CIELAB to RGB color space.
- [class func convertRGBtoLab() -> any CIFilter & CIConvertLab](cifilter-swift.class/convertrgbtolab.md)
  Converts an image from RGB to CIELAB color space.
- [class func dither() -> any CIFilter & CIDither](cifilter-swift.class/dither.md)
  Applies randomized noise to produce a processed look.
- [class func documentEnhancer() -> any CIFilter & CIDocumentEnhancer](cifilter-swift.class/documentenhancer.md)
  Adjusts an image’s shadows and contrast.
- [class func falseColor() -> any CIFilter & CIFalseColor](cifilter-swift.class/falsecolor.md)
  Replaces an image’s colors with specified colors.
- [class func labDeltaE() -> any CIFilter & CILabDeltaE](cifilter-swift.class/labdeltae.md)
  Compares an image’s color values.
- [class func maskToAlpha() -> any CIFilter & CIMaskToAlpha](cifilter-swift.class/masktoalpha.md)
  Converts an image to a white image with an alpha component.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifilter-swift.class/colorcrosspolynomial())*