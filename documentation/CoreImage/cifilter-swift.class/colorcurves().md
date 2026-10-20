# colorCurves()

**Framework**: Core Image  
**Kind**: method  
**Role**: Type Method

Adjusts an image’s color curves.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class func colorCurves() -> any CIFilter & CIColorCurves
```

```objc
+ (CIFilter<CIColorCurves> *) colorCurvesFilter;
```

#### Return Value

The modified image.

#### Discussion

This method applies the color curves filter to an image. The effect uses a three-channel one-dimensional color table to transform the source image pixels. The color table must be comprised of floating-point RGB value.

The color curves filter uses the following properties:

- **`colorSpace`**: A [`CGColorSpace`](../../CoreGraphics/cgcolorspace.md) representing the color space for the color curve.
- **`curvesData`**: Data containing a color table of floating-point RGB values as [`NSData`](../../Foundation/nsdata.md).
- **`curvesDomain`**: A two-element vector that defines the minimum and maximum values of the curve data as a [`CIVector`](../civector.md).
- **`inputImage`**: An image with the type [`CIImage`](../ciimage.md).

The following code creates a filter that adds brightness to the input image:

```swift
func colorCurves(inputImage: CIImage) -> CIImage {
    let colorCurvesEffect = CIFilter.colorCurves()
    colorCurvesEffect.inputImage = inputImage
    colorCurvesEffect.curvesDomain = CIVector(x: 0, y: 1)
    colorCurvesEffect.curvesData = Data(
        bytes: [Float32]([
            0.0,0.0,0.0,
            0.8,0.8,0.8,
            1.0,1.0,1.0
        ]), count: 36)
    colorCurvesEffect.colorSpace = CGColorSpaceCreateDeviceRGB()
    return colorCurvesEffect.outputImage!
}
```

![Two pictures of a pink flower surrounded by foliage. The photo on the left shows a single flower photographed close-up, in focus, with good light and no effects. In the photo on the right, a color curves filter is applied, resulting in the photo becoming brighter.](https://developer.apple.com/tutorials/images/com.apple.coreimage/media-3545017@2x.png)

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
- [class func maskToAlpha() -> any CIFilter & CIMaskToAlpha](./masktoalpha%28%29.md)
  Converts an image to a white image with an alpha component.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifilter-swift.class/colorcurves())*