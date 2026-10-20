# spotLight()

**Framework**: Core Image  
**Kind**: method  
**Role**: Type Method

Highlights a definined area of the image.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class func spotLight() -> any CIFilter & CISpotLight
```

```objc
+ (CIFilter<CISpotLight> *) spotLightFilter;
```

#### Return Value

The modified image.

#### Discussion

This method applies the spotlight filter to an image. The effect applies a directional spotlight effect to an image while creating a transparent area not highlighted by the spotlight.

The spotlight filter uses the following properties:

- **`inputImage`**: An image with the type [`CIImage`](../ciimage.md).
- **`lightPointsAt`**: A [`CIVector`](../civector.md) with the x and y positions that the spotlight points at.
- **`brightness`**: A `float` representing the brightness of the spotlight as an [`NSNumber`](../../Foundation/nsnumber.md).
- **`lightPosition`**: A [`CIVector`](../civector.md) containing the x and y position of the spotlight.
- **`concentration`**: A `float` representing the size of the spotlight in pixels as an [`NSNumber`](../../Foundation/nsnumber.md).
- **`color`**: A [`CIColor`](../cicolor.md) representing the spotlight color.

The following code creates a filter that results in only the bottom left of the image becoming visible while the rest of the image gradually becomes transparent:

```swift
func spotlight(inputImage: CIImage) -> CIImage {
    let spotlightFilter = CIFilter.spotLight()
    spotlightFilter.inputImage = inputImage
    spotlightFilter.lightPointsAt = CIVector(x: 100, y: 100)
    spotlightFilter.brightness = 10
    spotlightFilter.lightPosition = CIVector(x: 100, y: 100)
    spotlightFilter.concentration = 20
    return spotlightFilter.outputImage!
}
```

![Two pictures of a large amount of colorful  flowers. The photo on the left shows a group of flowers, in focus, with good light and no effects. In the photo on the right a spotlight  filter is applied, resulting in the photo becoming transparent with the bottom left corner being the most visible glimpse of the original image.](https://developer.apple.com/tutorials/images/com.apple.coreimage/media-3600004@2x.png)

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

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifilter-swift.class/spotlight())*