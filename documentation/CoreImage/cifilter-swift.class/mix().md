# mix()

**Framework**: Core Image  
**Kind**: method  
**Role**: Type Method

Blends two images together.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class func mix() -> any CIFilter & CIMix
```

```objc
+ (CIFilter<CIMix> *) mixFilter;
```

## Return Value

The modified image.

## Discussion

This method applies the mix filter to an image. The effect uses the amount property to interpolate between the input image and the background image, resulting in both images visible in the output image.

The mix filter uses the following properties:

- **`inputImage`**: An image with the type [`CIImage`](../ciimage.md).
- **`backgroundImage`**: An image representing the background image with the type [`CIImage`](../ciimage.md).
- **`amount`**: A `float` representing the strength of the effect as an [`NSNumber`](../../Foundation/nsnumber.md).

The following code creates a filter that combines the input and background images to create one image with both images visible:

```swift
func mix(inputImage: CIImage, backgroundImage: CIImage) -> CIImage {
    let mixFilter = CIFilter.mix()
    mixFilter.inputImage = inputImage
    mixFilter.backgroundImage = backgroundImage
    mixFilter.amount = 0.25
    return mixFilter.outputImage!
}
```

![Three pictures side by side. The first photo on the left is of the New York City skyline taken from across a river on an overcast day, with a single boat in the center of the image. The center photo is of multiple colorful rocks with green moss covering them. In the photo on the right, a mix filter is applied, and the image has detail from both the city skyline and mossy rock photo.](https://developer.apple.com/tutorials/images/com.apple.coreimage/media-3600009@2x.png)

## See Also

### Filters
- [class func blendWithAlphaMask() -> any CIFilter & CIBlendWithMask](./blendwithalphamask%28%29.md)
  Blends two images by using an alpha mask image.
- [class func blendWithBlueMask() -> any CIFilter & CIBlendWithMask](./blendwithbluemask%28%29.md)
  Blends two images by using a blue mask image.
- [class func blendWithMask() -> any CIFilter & CIBlendWithMask](./blendwithmask%28%29.md)
  Blends two images by using a mask image.
- [class func blendWithRedMask() -> any CIFilter & CIBlendWithMask](./blendwithredmask%28%29.md)
  Blends two images by using a red mask image.
- [class func bloom() -> any CIFilter & CIBloom](./bloom%28%29.md)
  Adjusts an image’s colors by applying a blur effect.
- [class func cannyEdgeDetector() -> any CIFilter & CICannyEdgeDetector](./cannyedgedetector%28%29.md)
  Applies the Canny edge-detection algorithm to an image.
- [class func comicEffect() -> any CIFilter & CIComicEffect](./comiceffect%28%29.md)
  Creates an image with a comic book effect.
- [class func coreMLModel() -> any CIFilter & CICoreMLModel](./coremlmodel%28%29.md)
  Filters an image with a Core ML model.
- [class func crystallize() -> any CIFilter & CICrystallize](./crystallize%28%29.md)
  Creates an image made with a series of colorful polygons.
- [class func depthOfField() -> any CIFilter & CIDepthOfField](./depthoffield%28%29.md)
  Simulates a depth of field effect.
- [class func edges() -> any CIFilter & CIEdges](./edges%28%29.md)
  Hilghlights edges of objects found within an image.
- [class func edgeWork() -> any CIFilter & CIEdgeWork](./edgework%28%29.md)
  Produces a black-and-white image that looks similar to a woodblock print.
- [class func gaborGradients() -> any CIFilter & CIGaborGradients](./gaborgradients%28%29.md)
  Highlights textures in an image.
- [class func gloom() -> any CIFilter & CIGloom](./gloom%28%29.md)
  Adjusts an image’s color by applying a gloom filter.
- [class func heightFieldFromMask() -> any CIFilter & CIHeightFieldFromMask](./heightfieldfrommask%28%29.md)
  Creates a realistic shaded height-field image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifilter-swift.class/mix())*