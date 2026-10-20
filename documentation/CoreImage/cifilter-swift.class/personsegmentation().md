# personSegmentation()

**Framework**: Core Image  
**Kind**: method  
**Role**: Type Method

Creates a mask where red pixels indicate areas of the image that are likely to contain a person.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
class func personSegmentation() -> any CIFilter & CIPersonSegmentation
```

```objc
+ (CIFilter<CIPersonSegmentation> *) personSegmentationFilter;
```

#### Return Value

A [`CIImage`](../ciimage.md) containing the mask.

#### Discussion

The person-segmentation filter creates a mask that contains red pixels in the areas of the input image that are likely to contain people.

The person-segmentation filter takes the following properties:

- **`inputIImage`**: A [`CIImage`](../ciimage.md) containing the image to segment.
- **`qualityLevel`**: The size and quality of the resulting segmentation mask. 0 is accurate, `1` is balanced, and `2` is fast.

The following code applies the person-segmentation filter to an image:

```swift
func personSegmentation(inputImage: CIImage) -> CIImage {
    let personSegmentationFilter = CIFilter.personSegmentation()
    personSegmentationFilter.inputImage = inputImage
    personSegmentationFilter.qualityLevel = 0
    return personSegmentationFilter.outputImage!
}

```

![An illustration of two images, side-by-side. The original image, on the left, contains a single individual against a background of a field, trees, and buildings. The other image, on the right, shows the individual after segmentation. The background is all set to black and the pixels that make up the individual are all set to red.](https://developer.apple.com/tutorials/images/com.apple.coreimage/media-4407311@2x.png)

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

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifilter-swift.class/personsegmentation())*