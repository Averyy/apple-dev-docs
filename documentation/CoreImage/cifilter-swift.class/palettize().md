# palettize()

**Framework**: Core Image  
**Kind**: method  
**Role**: Type Method

Replaces colors with colors from a palette image.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class func palettize() -> any CIFilter & CIPalettize
```

```objc
+ (CIFilter<CIPalettize> *) palettizeFilter;
```

## Return Value

The modified image.

## Discussion

This method applies the palette filter to an image. The effect uses the palette image that is *K* x 1 pixels in size containing a set of colors, replacing the image colors.

The palettize filter uses the following properties:

- **`inputImage`**: An image with the type [`CIImage`](../ciimage.md).
- **`paletteImage`**: An image with the dimensions of *N* x 1 where *N* represents the colors to add to the image, with type [`CIImage`](../ciimage.md).
- **`perceptual`**: A Boolean value that specifies if the filter applies the color palette in a perceptual color space.

The following code creates a filter that replaces the colors of the input image with the specified colors found in the palette image:

```swift
func palettize(inputImage: CIImage, paletteImage: CIImage) -> CIImage {
    let palettizeFilter = CIFilter.palettize()
    palettizeFilter.inputImage = inputImage
    palettizeFilter.paletteImage = paletteImage
    palettizeFilter.perceptual = true
    return palettizeFilter.outputImage!
}
```

![One photograph on the left above a gradient image, and a second photograph on the right. The photograph on the left shows a pink flower surrounded by foliage. The image below it is a gradient image displaying a gradual color shift from a dark purple to a light pink. The photo on the right shows the same picture of the pink flower with a palettize filter applied. The photograph displays brightness of the flower image with only the colors provided in the color palette image.](https://developer.apple.com/tutorials/images/com.apple.coreimage/media-3558713@2x.png)

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

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifilter-swift.class/palettize())*