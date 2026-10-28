# pointillize()

**Framework**: Core Image  
**Kind**: method  
**Role**: Type Method

Applies a pointillize effect to an image.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class func pointillize() -> any CIFilter & CIPointillize
```

```objc
+ (CIFilter<CIPointillize> *) pointillizeFilter;
```

## Return Value

A [`CIImage`](../ciimage.md) containing the pointillized image.

## Discussion

This filter applies a pointillize effect to an image. The effect generates an output image made of small, single-color, circular points distributed on a randomly perturbed grid.

The pointillize filter uses the following properties:

- **`inputImage`**: A [`CIImage`](../ciimage.md) containing the input image.
- **`radius`**: The radius in pixels of the circular points.
- **center**: Determines the origin of the grid.

The following code applies the pointillize filter with a radius of 40 pixels.

```swift
func pointillize(inputImage: CIImage) -> CIImage {
    let pointillizeFilter = CIFilter.pointillize()
    pointillizeFilter.inputImage = inputImage
    pointillizeFilter.radius = 40
    pointillizeFilter.center = CGPoint(x: 0,y: 0)
    return pointillizeFilter.outputImage!
}
```

![Two images arranged horizontally. The left image contains a photo of a colorful bunch of flowers. The right image shows the result of applying the pointillize filter. The image is made of small circular points. The color of each point matches up with the color at the location of the dot in the original image.](https://developer.apple.com/tutorials/images/com.apple.coreimage/media-4333706@2x.png)

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

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifilter-swift.class/pointillize())*