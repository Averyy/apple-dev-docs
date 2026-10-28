# cannyEdgeDetector()

**Framework**: Core Image  
**Kind**: method  
**Role**: Type Method

Applies the Canny edge-detection algorithm to an image.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
class func cannyEdgeDetector() -> any CIFilter & CICannyEdgeDetector
```

```objc
+ (CIFilter<CICannyEdgeDetector> *) cannyEdgeDetectorFilter;
```

## Return Value

A [`CIImage`](../ciimage.md) with the detected edges.

## Discussion

This filter performs a Canny edge-detection on the input image, producing a black-and-white image with the detected edges. White pixels indicate an edge, and black pixels indicate no edge.

The Canny edge-detection filter uses the following properties:

- **`inputImage`**: The [`CIImage`](../ciimage.md) to use as an input for the effect.
- **`gaussianSigma`**: A `float` specifying the sigma of the Gaussian blur to apply, reducing high-frequency noise. Defaults to `1.6`.
- **`perceptual`**: A `Boolean` specifying whether to use a perceptual color space to compute the edge thresholds. Defaults to `false`.
- **`thresholdLow`**: A `float` specifying the threshold for weak edges. Defaults to `0.02`.
- **`thresholdHigh`**: A `float` specifying the threshold for strong edges. Defaults to `0.05`.
- **`hysteresisPasses`**: The number of hysteresis passes to apply to promote weak edge pixels. Minimum value is `0`, maximum value is `20`, and defaults to `1`.

The following code applies Canny edge-detection to an image:

```swift
func cannyEdgeDetector(inputImage: CIImage) -> CIImage {
    let filter = CIFilter.cannyEdgeDetector()
    filter.inputImage = inputImage
    filter.gaussianSigma = 5
    filter.perceptual = false
    filter.thresholdLow = 0.02
    filter.thresholdHigh = 0.05
    filter.hysteresisPasses = 1
    return filter.outputImage!
}
```

![Two images arranged horizontally. The left image contains a palm tree against a clear sky. The right image contains the result of running the Canny edge-detection filter. The result image contains the outline of the palm tree.](https://developer.apple.com/tutorials/images/com.apple.coreimage/media-4407284@2x.png)

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
- [class func hexagonalPixellate() -> any CIFilter & CIHexagonalPixellate](./hexagonalpixellate%28%29.md)
  Creates an image made of a series of colorful hexagons.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifilter-swift.class/cannyedgedetector())*