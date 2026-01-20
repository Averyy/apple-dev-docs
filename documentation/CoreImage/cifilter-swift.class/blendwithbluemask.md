# blendWithBlueMask()

**Framework**: Core Image  
**Kind**: method

Blends two images by using a blue mask image.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class func blendWithBlueMask() -> any CIFilter & CIBlendWithMask
```

#### Return Value

The modified image.

#### Discussion

This method applies the blend with blue mask filter to an image. The effect uses values from the blue mask image to interpolate between the input and background images. The mask image is made of shades of blue that define the strength of the interpolation from zero (where the mask image is black) to the specified `radius` (where the mask image is blue).

The blend with blue mask filter uses the following properties:

The following code creates a filter that results in the replacement of blue in the mask image with the detail of the input image:

```swift
func blendWithBlueMask(inputimage: CIImage, backgroundimage: CIImage, maskimage: CIImage) -> CIImage {
    let  blendWithBlueMaskFilter = CIFilter.blendWithBlueMask()
    blendWithBlueMaskFilter.inputImage = inputimage
    blendWithBlueMaskFilter.maskImage = maskimage
    blendWithBlueMaskFilter.backgroundImage = backgroundimage
    return blendWithBlueMaskFilter.outputImage!
}
```

![A set of four photographs with two stacked on the left and two side by side on the right. The top photo on the left is of the New York City skyline taken from across the river on an overcast day, with a single boat in the center of the image. The bottom photo on the left is of multiple colorful rocks with green moss covering them. The first photograph on the right is a transparent image with a five-point triangle, hexagon, circle and square filled with a gradient of dark blue to green. The second photograph on the right is a blend with a blue mask filter applied, resulting in the skyline photo with the detail of the moss-covered rocks showing in the area that is dark blue from the mask image.](https://docs-assets.developer.apple.com/published/0c244bb3341e217960e71527cbdbcb6d/media-3624592%402x.png)

## See Also

- [class func blendWithAlphaMask() -> any CIFilter & CIBlendWithMask](cifilter-swift.class/blendwithalphamask.md)
  Blends two images by using an alpha mask image.
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

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifilter-swift.class/blendwithbluemask())*