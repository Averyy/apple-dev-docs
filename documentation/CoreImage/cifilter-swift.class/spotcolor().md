# spotColor()

**Framework**: Core Image  
**Kind**: method  
**Role**: Type Method

Replaces colors of an image with specifed colors.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class func spotColor() -> any CIFilter & CISpotColor
```

```objc
+ (CIFilter<CISpotColor> *) spotColorFilter;
```

#### Return Value

The modified image.

#### Discussion

This method applies the spot color filter to an image. The effect replaces one or more of the color ranges of the input image with properties.

The spot color filter uses the following properties:

- **`inputImage`**: An image with the type [`CIImage`](../ciimage.md).
- **`centerColor1`**: A [`CIColor`](../cicolor.md) representing the median value of the first color to be replaced.
- **`centerColor2`**: A [`CIColor`](../cicolor.md) representing the median value of the second color to be replaced.
- **`centerColor3`**: A [`CIColor`](../cicolor.md) representing the median value of the third color to be replaced.
- **`replacementColor1`**: A [`CIColor`](../cicolor.md) to replace the first color.
- **`replacementColor2`**: A [`CIColor`](../cicolor.md) to replace the second color.
- **`replacementColor3`**: A [`CIColor`](../cicolor.md) to replace the third color.
- **`closeness1`**: A `float` representing how closely the first center color must match before it’s replaced.
- **`closeness2`**: A `float` representing how closely the second center color must match before it’s replaced.
- **`closeness3`**: A `float` representing how closely the third center color must match before it’s replaced.
- **`contrast1`**: A `float` representing the contrast of the first replacement color as an [`NSNumber`](../../Foundation/nsnumber.md).
- **`contrast2`**: A `float` representing the contrast of the second replacement color as an [`NSNumber`](../../Foundation/nsnumber.md).
- **`contrast3`**: A `float` representing the contrast of the third replacement color as an [`NSNumber`](../../Foundation/nsnumber.md).

The following code creates a filter that replaces the colors of the input image with the specified colors:

```swift
func spotColor(inputImage: CIImage) -> CIImage {
    let spotColorFilter = CIFilter.spotColor()
    spotColorFilter.inputImage = inputImage
    spotColorFilter.centerColor1 = .red
    spotColorFilter.replacementColor1 = .green
    spotColorFilter.closeness1 = 5
    spotColorFilter.contrast1 = 1
    return spotColorFilter.outputImage!
}
```

![Two pictures of a pink flower surrounded by foliage. The photo on the left has no modifications to color. In the photo on the right, a spot color filter is applied, resulting in less color in the image with the center flower becoming brown and the foliage becoming a solid light green.](https://developer.apple.com/tutorials/images/com.apple.coreimage/media-3600008@2x.png)

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

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifilter-swift.class/spotcolor())*