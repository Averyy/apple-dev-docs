# lineOverlay()

**Framework**: Core Image  
**Kind**: method  
**Role**: Type Method

Creates an image that resembles a sketch of the outlines of objects.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class func lineOverlay() -> any CIFilter & CILineOverlay
```

```objc
+ (CIFilter<CILineOverlay> *) lineOverlayFilter;
```

## Return Value

The modified image.

## Discussion

This method applies the line overlay filter to an image. The effect creats a sketch that outlines the edges of the image in black, leaving the non-outlined portion of the image transparent.

The line overlay filter uses the following properties:

- **`inputImage`**: An image with the type [`CIImage`](../ciimage.md).
- **`nrNoiseLevel`**: A `float` representing the desired level of noise as an [`NSNumber`](../../Foundation/nsnumber.md).
- **`nrSharpness`**: A `float` representing the desired level of sharpness as an [`NSNumber`](../../Foundation/nsnumber.md).
- **`edgeIntensity`**: A `float` representing the Sobel gradient information for edge tracing as an [`NSNumber`](../../Foundation/nsnumber.md).
- **`threshold`**: A `float` representing the threshold of edge visibilty as an [`NSNumber`](../../Foundation/nsnumber.md).
- **`contrast`**: A `float` representing the desired contrast as an [`NSNumber`](../../Foundation/nsnumber.md).

The following code creates a filter that results in a monochrome image with lines outlining the edges of objects:

```swift
func lineOverlay(inputImage: CIImage) -> CIImage {
    let lineOverlay = CIFilter.lineOverlay()
    lineOverlay.inputImage = inputImage
    lineOverlay.nrNoiseLevel = 0.07
    lineOverlay.nrSharpness = 0.71
    lineOverlay.edgeIntensity = 1
    lineOverlay.threshold = 0.1
    lineOverlay.contrast = 50.00
    return lineOverlay.outputImage!
}
```

![Two pictures of a pink flower surrounded by foliage. The photo on the left shows a single flower photographed close up, in focus, with good light and no effects. In the photo on the right, the line overlay filter is applied, resulting in a monochrome image with the edges of objects outlined in black.](https://developer.apple.com/tutorials/images/com.apple.coreimage/media-3600001@2x.png)

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

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifilter-swift.class/lineoverlay())*