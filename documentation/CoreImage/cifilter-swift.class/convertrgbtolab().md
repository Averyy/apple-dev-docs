# convertRGBtoLab()

**Framework**: Core Image  
**Kind**: method  
**Role**: Type Method

Converts an image from RGB to CIELAB color space.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
class func convertRGBtoLab() -> any CIFilter & CIConvertLab
```

```objc
+ (CIFilter<CIConvertLab> *) convertRGBtoLabFilter;
```

## Return Value

The converted [`CIImage`](../ciimage.md).

## Discussion

This filter converts an image from RGB to CIELAB color space. The CIELAB color space expresses color as three values: L* for the perceptual lightness, and a*b* for the colors red, green, blue, and yellow. The RGB color space expresses colors using the intensities of the three primary colors: red, green, and blue.

- **`inputImage`**: A [`CIImage`](../ciimage.md) containing the `RGB` image.
- **`normalize`**: If true, the three output channels are in the range 0 to 1. If false, the L* channel is in the range 0 to 100 and the a*b* channels are in the range -128 to 128.

The following code applies the `convertRGBToLabFilter` to an image with the `normalize` flag set to the `true`:

```swift
func convertRGBToLab(inputImage: CIImage) -> CIImage {
    let convertRGBToLabFilter = CIFilter.convertRGBtoLab()
    convertRGBToLabFilter.inputImage = inputImage
    convertRGBToLabFilter.normalize = true
    return convertRGBToLabFilter.outputImage!
}
```

![Two images arranged horizontally. The left image contains a photo of the Golden Gate Bridge with a clear sky as the background. The right image shows the result of applying the convert-RGB-to-Lab filter with the normalize flag set to true. The bridge is a light cyan color and the sky is a gradient from yellow-green through to red-pink.](https://developer.apple.com/tutorials/images/com.apple.coreimage/media-4407334@2x.png)

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

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifilter-swift.class/convertrgbtolab())*