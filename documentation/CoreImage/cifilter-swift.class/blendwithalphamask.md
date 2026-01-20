# blendWithAlphaMask()

**Framework**: Core Image  
**Kind**: method

Blends two images by using an alpha mask image.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class func blendWithAlphaMask() -> any CIFilter & CIBlendWithMask
```

#### Return Value

The modified image.

#### Discussion

This method applies the blend with alpha mask filter to an image. The effect uses values from the grayscale mask image to interpolate between the input and background images. The mask image consists of shades of gray that define the strength of the interpolation from zero (where the mask image is black) to the specified `radius` (where the mask image is white).

The blend with alpha mask filter uses the following properties:

The following code creates a filter that results in the replacement of white in the mask image with the detail of the input image:

```swift
func blendWithAlphaMask(inputimage: CIImage, backgroundimage: CIImage, maskimage: CIImage) -> CIImage {
    let blendWithAlphaMaskFilter = CIFilter.blendWithAlphaMask()
    blendWithAlphaMaskFilter.inputImage = inputimage
    blendWithAlphaMaskFilter.maskImage = maskimage
    blendWithAlphaMaskFilter.backgroundImage = backgroundimage
    return blendWithAlphaMaskFilter.outputImage!
}
```

![A set of four photographs with two stacked on the left and two side by side on the right. The top photo on the left is of the New York City skyline taken from across the river on an overcast day, with a single boat in the center of the image. The bottom photo on the left is of multiple colorful rocks with moss covering them. The first photograph on the right is a transparent image with a five-point triangle, hexagon, circle, and square filled with white. The second photograph on the right is a blend with an alpha mask filter applied, resulting in the skyline photo with the detail of the moss covered rocks showing in the area that is white from the mask image.](https://docs-assets.developer.apple.com/published/9fa21135b87a43a7eb3a8e4c6699f41c/media-3624591%402x.png)

## See Also

- [class func blendWithBlueMask() -> any CIFilter & CIBlendWithMask](cifilter-swift.class/blendwithbluemask.md)
  Blends two images by using a blue mask image.
- [class func blendWithMask() -> any CIFilter & CIBlendWithMask](cifilter-swift.class/blendwithmask.md)
  Blends two images by using a mask image.
- [class func blendWithRedMask() -> any CIFilter & CIBlendWithMask](cifilter-swift.class/blendwithredmask.md)
  Blends two images by using a red mask image.
- [class func bloom() -> any CIFilter & CIBloom](cifilter-swift.class/bloom.md)
  Adjusts an image’s colors by applying a blur effect.
- [class func cannyEdgeDetector() -> any CIFilter & CICannyEdgeDetector](cifilter-swift.class/cannyedgedetector.md)
  Applies the Canny edge-detection algorithm to an image.
- [class func comicEffect() -> any CIFilter & CIComicEffect](cifilter-swift.class/comiceffect.md)
  Creates an image with a comic book effect.
- [class func coreMLModel() -> any CIFilter & CICoreMLModel](cifilter-swift.class/coremlmodel.md)
  Filters an image with a Core ML model.
- [class func crystallize() -> any CIFilter & CICrystallize](cifilter-swift.class/crystallize.md)
  Creates an image made with a series of colorful polygons.
- [class func depthOfField() -> any CIFilter & CIDepthOfField](cifilter-swift.class/depthoffield.md)
  Simulates a depth of field effect.
- [class func edges() -> any CIFilter & CIEdges](cifilter-swift.class/edges.md)
  Hilghlights edges of objects found within an image.
- [class func edgeWork() -> any CIFilter & CIEdgeWork](cifilter-swift.class/edgework.md)
  Produces a black-and-white image that looks similar to a woodblock print.
- [class func gaborGradients() -> any CIFilter & CIGaborGradients](cifilter-swift.class/gaborgradients.md)
  Highlights textures in an image.
- [class func gloom() -> any CIFilter & CIGloom](cifilter-swift.class/gloom.md)
  Adjusts an image’s color by applying a gloom filter.
- [class func heightFieldFromMask() -> any CIFilter & CIHeightFieldFromMask](cifilter-swift.class/heightfieldfrommask.md)
  Creates a realistic shaded height-field image.
- [class func hexagonalPixellate() -> any CIFilter & CIHexagonalPixellate](cifilter-swift.class/hexagonalpixellate.md)
  Creates an image made of a series of colorful hexagons.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifilter-swift.class/blendwithalphamask())*