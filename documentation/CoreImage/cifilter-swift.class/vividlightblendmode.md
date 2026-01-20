# vividLightBlendMode()

**Framework**: Core Image  
**Kind**: method

A combination of color-burn and color-dodge blend modes.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
class func vividLightBlendMode() -> any CIFilter & CICompositeOperation
```

#### Return Value

The blended image as a [`CIImage`](ciimage.md).

#### Discussion

The vivid-light blend mode combines the color-dodge and color-burn blend modes (rescaled so that neutral colors become middle gray). If the input Images values are lighter than middle gray, the filter uses dodge; for darker values, the filter uses burn.

The following code sample applies the vivid-light blend mode filter to two images:

```swift
func vividLightBlendMode(inputImage: CIImage, backgroundImage: CIImage) -> CIImage {
    let filter = CIFilter.vividLightBlendMode()
    filter.inputImage = inputImage
    filter.backgroundImage = backgroundImage
    return filter.outputImage!
}
```

![Two images arranged vertically on the left and a third image on the right. The top left image contains a photograph of a vineyard. The lower third of the image contains gravel with a deep shadow in the foreground. The image on the bottom left is a closeup photograph of a cactus. The image on the right shows the result of applying the vivid-light blend mode filter.](https://docs-assets.developer.apple.com/published/7a399b3bb44e1bdda387b6c2966a1d99/media-4407307%402x.png)

## See Also

- [class func additionCompositing() -> any CIFilter & CICompositeOperation](cifilter-swift.class/additioncompositing.md)
  Blends colors from two images by addition.
- [class func colorBlendMode() -> any CIFilter & CICompositeOperation](cifilter-swift.class/colorblendmode.md)
  Blends color from two images using the luminance values from the background image and the hue and saturation values from the input image.
- [class func colorBurnBlendMode() -> any CIFilter & CICompositeOperation](cifilter-swift.class/colorburnblendmode.md)
  Blends color from two images while darkening the image.
- [class func colorDodgeBlendMode() -> any CIFilter & CICompositeOperation](cifilter-swift.class/colordodgeblendmode.md)
  Blends color from two images using dodging.
- [class func darkenBlendMode() -> any CIFilter & CICompositeOperation](cifilter-swift.class/darkenblendmode.md)
  Blends colors from two images while darkening lighter pixels.
- [class func differenceBlendMode() -> any CIFilter & CICompositeOperation](cifilter-swift.class/differenceblendmode.md)
  Subtracts color values to blend colors.
- [class func divideBlendMode() -> any CIFilter & CICompositeOperation](cifilter-swift.class/divideblendmode.md)
  Divides color values to blend colors.
- [class func exclusionBlendMode() -> any CIFilter & CICompositeOperation](cifilter-swift.class/exclusionblendmode.md)
  Subtracts color values to blend colors with less contrast.
- [class func hardLightBlendMode() -> any CIFilter & CICompositeOperation](cifilter-swift.class/hardlightblendmode.md)
  Blends colors of two images by screening and multiplying.
- [class func hueBlendMode() -> any CIFilter & CICompositeOperation](cifilter-swift.class/hueblendmode.md)
  Blends colors of two images by computing the sum of image color values.
- [class func lightenBlendMode() -> any CIFilter & CICompositeOperation](cifilter-swift.class/lightenblendmode.md)
  Blends colors from two images by brightening colors.
- [class func linearBurnBlendMode() -> any CIFilter & CICompositeOperation](cifilter-swift.class/linearburnblendmode.md)
  Blends color from two images while increasing contrast.
- [class func linearDodgeBlendMode() -> any CIFilter & CICompositeOperation](cifilter-swift.class/lineardodgeblendmode.md)
  Blends colors of two images with dodging.
- [class func linearLightBlendMode() -> any CIFilter & CICompositeOperation](cifilter-swift.class/linearlightblendmode.md)
  A combination of linear burn and linear dodge blend modes.
- [class func luminosityBlendMode() -> any CIFilter & CICompositeOperation](cifilter-swift.class/luminosityblendmode.md)
  Blends color from two images by calculating the color, hue, and saturation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifilter-swift.class/vividlightblendmode())*