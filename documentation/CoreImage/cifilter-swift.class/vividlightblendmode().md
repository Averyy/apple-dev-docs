# vividLightBlendMode()

**Framework**: Core Image  
**Kind**: method  
**Role**: Type Method

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

```objc
+ (CIFilter<CICompositeOperation> *) vividLightBlendModeFilter;
```

#### Return Value

The blended image as a [`CIImage`](../ciimage.md).

#### Discussion

The vivid-light blend mode combines the color-dodge and color-burn blend modes (rescaled so that neutral colors become middle gray). If the input Images values are lighter than middle gray, the filter uses dodge; for darker values, the filter uses burn.

- **`inputImage`**: A [`CIImage`](../ciimage.md) containing the input image.
- **`backgroundImage`**: A [`CIImage`](../ciimage.md) containing the background image.

The following code sample applies the vivid-light blend mode filter to two images:

```swift
func vividLightBlendMode(inputImage: CIImage, backgroundImage: CIImage) -> CIImage {
    let filter = CIFilter.vividLightBlendMode()
    filter.inputImage = inputImage
    filter.backgroundImage = backgroundImage
    return filter.outputImage!
}
```

![Two images arranged vertically on the left and a third image on the right. The top left image contains a photograph of a vineyard. The lower third of the image contains gravel with a deep shadow in the foreground. The image on the bottom left is a closeup photograph of a cactus. The image on the right shows the result of applying the vivid-light blend mode filter.](https://developer.apple.com/tutorials/images/com.apple.coreimage/media-4407307@2x.png)

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

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifilter-swift.class/vividlightblendmode())*