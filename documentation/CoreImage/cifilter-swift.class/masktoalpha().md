# maskToAlpha()

**Framework**: Core Image  
**Kind**: method  
**Role**: Type Method

Converts an image to a white image with an alpha component.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class func maskToAlpha() -> any CIFilter & CIMaskToAlpha
```

```objc
+ (CIFilter<CIMaskToAlpha> *) maskToAlphaFilter;
```

## Return Value

The modified image.

## Discussion

This method applies the mask-to-alpha filter to an image. The value of the alpha component is determined by the grayscale value of the input image. Black pixels become completely transparent, white pixels are completely solid.

The mask-to-alpha filter uses the following properties:

- **`inputImage`**: An image with the type [`CIImage`](../ciimage.md).

The following code creates a filter that makes the input image’s background transparent:

```swift
func maskToAlpha(inputImage: CIImage) -> CIImage {
    let maskToAlphaFilter = CIFilter.maskToAlpha()
    maskToAlphaFilter.inputImage = inputImage
    return maskToAlphaFilter.outputImage!
}
```

![Two photographs of a triangle, hexagon, circle, and a square arranged in the center of the image on a black background. In the photo on the right, a mask-to-alpha filter is applied. The image no longer has a black background and all of the white shapes are now on a transparent layer.](https://developer.apple.com/tutorials/images/com.apple.coreimage/media-3545058@2x.png)

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
- [class func labDeltaE() -> any CIFilter & CILabDeltaE](./labdeltae%28%29.md)
  Compares an image’s color values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifilter-swift.class/masktoalpha())*