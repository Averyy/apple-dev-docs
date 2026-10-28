# colorMap()

**Framework**: Core Image  
**Kind**: method  
**Role**: Type Method

Performs a transformation of the input image colors to colors from a gradient image.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class func colorMap() -> any CIFilter & CIColorMap
```

```objc
+ (CIFilter<CIColorMap> *) colorMapFilter;
```

## Return Value

The modified image.

## Discussion

This method applies a color map filter to an image. The effect transforms source color values by converting the unpremultiplied RGB values to luma using the weighting `(0.2125, 0.7154, 0.0721)`. The luma value is then used to look up the new color from the gradient image.

The color map filter uses the following properties:

- **`inputImage`**: An image with the type [`CIImage`](../ciimage.md).
- **`gradientImage`**: An image representing the gradient of colors to be mapped to the input image colors with the type [`CIImage`](../ciimage.md).

The following code creates a filter that adds the gradient image colors to the input image:

```swift
func colorMap(inputImage: CIImage, gradientImage: CIImage) -> CIImage {
    let colorMap = CIFilter.colorMap()
    colorMap.inputImage = inputImage
    colorMap.gradientImage = gradientImage
    return colorMap.outputImage!
}
```

![One photograph on the left above a gradient image, and a second photograph on the right. The photograph on the top left shows a single flower photographed closeup, in focus, with good light and no effects. The image below is a gradient image displaying a gradual color shift from lime green to orange. The photo on the right shows the same pink flower picture with a color map filter applied. The photograph displays the colors of the gradient photo, with the brightness and contrast of the flower photo.](https://developer.apple.com/tutorials/images/com.apple.coreimage/media-3558775@2x.png)

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
- [class func labDeltaE() -> any CIFilter & CILabDeltaE](./labdeltae%28%29.md)
  Compares an image’s color values.
- [class func maskToAlpha() -> any CIFilter & CIMaskToAlpha](./masktoalpha%28%29.md)
  Converts an image to a white image with an alpha component.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifilter-swift.class/colormap())*