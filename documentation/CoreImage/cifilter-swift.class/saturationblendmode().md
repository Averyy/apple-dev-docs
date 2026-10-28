# saturationBlendMode()

**Framework**: Core Image  
**Kind**: method  
**Role**: Type Method

Blends the colors and saturation values of two images.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class func saturationBlendMode() -> any CIFilter & CICompositeOperation
```

```objc
+ (CIFilter<CICompositeOperation> *) saturationBlendModeFilter;
```

## Return Value

The modified image.

## Discussion

This method applies the saturation-blend mode filter to an image. The effect uses the values of the hue and luminance from the background image with the saturation of the input image to produce the output.

The saturation-blend mode filter uses the following properties:

- **`inputImage`**: An image with the type [`CIImage`](../ciimage.md).
- **`backgroundImage`**: An image with the type [`CIImage`](../ciimage.md).

The following code creates a filter that results in the image taking on the colors of the background image with low saturated values becoming gray.

```swift
func saturationBlendMode(inputImage: CIImage, backgroundImage: CIImage) -> CIImage {
    let colorBlendFilter = CIFilter.saturationBlendMode()
    colorBlendFilter.inputImage = inputImage
    colorBlendFilter.backgroundImage = backgroundImage
    return colorBlendFilter.outputImage!
}
```

![The image on the top left shows a beach with multiple palm trees and a rainbow arching across the blue sky.  The image below is a gradient image displaying a gradual color shift from purple to a dark orange. The image on the right shows the output from applying a saturation-blend mode filter. The result displays a gray beach with not much visible detail and only the colors from the gradient photo visible.](https://developer.apple.com/tutorials/images/com.apple.coreimage/media-3546404@2x.png)

## See Also

### Filters
- [class func additionCompositing() -> any CIFilter & CICompositeOperation](./additioncompositing%28%29.md)
  Blends colors from two images by addition.
- [class func colorBlendMode() -> any CIFilter & CICompositeOperation](./colorblendmode%28%29.md)
  Blends color from two images using the luminance values from the background image and the hue and saturation values from the input image.
- [class func colorBurnBlendMode() -> any CIFilter & CICompositeOperation](./colorburnblendmode%28%29.md)
  Blends color from two images while darkening the image.
- [class func colorDodgeBlendMode() -> any CIFilter & CICompositeOperation](./colordodgeblendmode%28%29.md)
  Blends color from two images using dodging.
- [class func darkenBlendMode() -> any CIFilter & CICompositeOperation](./darkenblendmode%28%29.md)
  Blends colors from two images while darkening lighter pixels.
- [class func differenceBlendMode() -> any CIFilter & CICompositeOperation](./differenceblendmode%28%29.md)
  Subtracts color values to blend colors.
- [class func divideBlendMode() -> any CIFilter & CICompositeOperation](./divideblendmode%28%29.md)
  Divides color values to blend colors.
- [class func exclusionBlendMode() -> any CIFilter & CICompositeOperation](./exclusionblendmode%28%29.md)
  Subtracts color values to blend colors with less contrast.
- [class func hardLightBlendMode() -> any CIFilter & CICompositeOperation](./hardlightblendmode%28%29.md)
  Blends colors of two images by screening and multiplying.
- [class func hueBlendMode() -> any CIFilter & CICompositeOperation](./hueblendmode%28%29.md)
  Blends colors of two images by computing the sum of image color values.
- [class func lightenBlendMode() -> any CIFilter & CICompositeOperation](./lightenblendmode%28%29.md)
  Blends colors from two images by brightening colors.
- [class func linearBurnBlendMode() -> any CIFilter & CICompositeOperation](./linearburnblendmode%28%29.md)
  Blends color from two images while increasing contrast.
- [class func linearDodgeBlendMode() -> any CIFilter & CICompositeOperation](./lineardodgeblendmode%28%29.md)
  Blends colors of two images with dodging.
- [class func linearLightBlendMode() -> any CIFilter & CICompositeOperation](./linearlightblendmode%28%29.md)
  A combination of linear burn and linear dodge blend modes.
- [class func luminosityBlendMode() -> any CIFilter & CICompositeOperation](./luminosityblendmode%28%29.md)
  Blends color from two images by calculating the color, hue, and saturation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifilter-swift.class/saturationblendmode())*