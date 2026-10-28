# labDeltaE()

**Framework**: Core Image  
**Kind**: method  
**Role**: Type Method

Compares an image’s color values.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class func labDeltaE() -> any CIFilter & CILabDeltaE
```

```objc
+ (CIFilter<CILabDeltaE> *) LabDeltaE;
```

## Return Value

The modified image.

## Discussion

This method applies the Lab ΔE filter to an image. The effect creates an image based on the visual color differences between the two input images. The resulting image contains ΔE 1994 values between 0.0 and 100.0.

The Lab ΔE filter uses the following properties:

- **`inputImage`**: An image with the type [`CIImage`](../ciimage.md).
- **`image2`**: An image with the type [`CIImage`](../ciimage.md) the system uses for comparison.

The following code creates a filter that removes the background from the input image:

```swift
func labDeltaE(inputImage: CIImage, inputImage2: CIImage) -> CIImage {
    let labDeltaEFilter = CIFilter.labDeltaE()
    labDeltaEFilter.inputImage = inputImage
    labDeltaEFilter.image2 = inputImage2
    return labDeltaEFilter.outputImage!
}
```

![Two photographs of a star, pentagon, nonagon, and a rounded corner square arranged in the center of the image on a black background. In the photo on the right, a Lab ΔE filter is applied, so the image no longer has a black background, and all of the white shapes are now on a transparent layer.](https://developer.apple.com/tutorials/images/com.apple.coreimage/media-3546476@2x.png)

## See Also

### Color Effect Filters
- [class func colorCrossPolynomial() -> any CIFilter & CIColorCrossPolynomial](./colorcrosspolynomial%28%29.md)
  Adjusts an image’s color by applying polynomial cross-products.
- [class func colorCube() -> any CIFilter & CIColorCube](./colorcube%28%29.md)
  Adjusts an image’s pixels using a three-dimensional color table.
- [class func colorCubeWithColorSpace() -> any CIFilter & CIColorCubeWithColorSpace](./colorcubewithcolorspace%28%29.md)
  Adjusts an image’s pixels using a three-dimensional color table in specified color space.
- [class func colorCubesMixedWithMask() -> any CIFilter & CIColorCubesMixedWithMask](./colorcubesmixedwithmask%28%29.md)
  Alters an image’s pixels using a three-dimensional color tables and a mask image.
- [class func colorCurves() -> any CIFilter & CIColorCurves](./colorcurves%28%29.md)
  Adjusts an image’s color curves.
- [class func colorInvert() -> any CIFilter & CIColorInvert](./colorinvert%28%29.md)
  Inverts an image’s colors.
- [class func colorMap() -> any CIFilter & CIColorMap](./colormap%28%29.md)
  Performs a transformation of the input image colors to colors from a gradient image.
- [class func colorMonochrome() -> any CIFilter & CIColorMonochrome](./colormonochrome%28%29.md)
  Adjusts an image’s colors to shades of a single color.
- [class func colorPosterize() -> any CIFilter & CIColorPosterize](./colorposterize%28%29.md)
  Flattens an image’s colors.
- [class func convertLabToRGB() -> any CIFilter & CIConvertLab](./convertlabtorgb%28%29.md)
  Converts an image from CIELAB to RGB color space.
- [class func convertRGBtoLab() -> any CIFilter & CIConvertLab](./convertrgbtolab%28%29.md)
  Converts an image from RGB to CIELAB color space.
- [class func dither() -> any CIFilter & CIDither](./dither%28%29.md)
  Applies randomized noise to produce a processed look.
- [class func documentEnhancer() -> any CIFilter & CIDocumentEnhancer](./documentenhancer%28%29.md)
  Adjusts an image’s shadows and contrast.
- [class func falseColor() -> any CIFilter & CIFalseColor](./falsecolor%28%29.md)
  Replaces an image’s colors with specified colors.
- [class func maskToAlpha() -> any CIFilter & CIMaskToAlpha](./masktoalpha%28%29.md)
  Converts an image to a white image with an alpha component.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifilter-swift.class/labdeltae())*