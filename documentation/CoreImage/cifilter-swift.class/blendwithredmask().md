# blendWithRedMask()

**Framework**: Core Image  
**Kind**: method  
**Role**: Type Method

Blends two images by using a red mask image.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class func blendWithRedMask() -> any CIFilter & CIBlendWithMask
```

```objc
+ (CIFilter<CIBlendWithMask> *) blendWithRedMaskFilter;
```

## Return Value

The modified image.

## Discussion

This method applies the blend with red mask filter to an image. The effect uses values from the red mask image to interpolate between the input and background images. The mask image consists of shades of red that define the strength of the interpolation from zero (where the mask image is black) to the specified `radius` (where the mask image is red).

The blend with red mask filter uses the following properties:

- **`inputImage`**: An image with the type [`CIImage`](../ciimage.md).
- **`maskImage`**: An image that masks an area on the background image with the type [`CIImage`](../ciimage.md).
- **`backgroundImage`**: An image with the type [`CIImage`](../ciimage.md).

The following code creates a filter that results in the replacement of green in the mask image with the detail of the input image:

```swift
func blendWithRedMask(inputimage: CIImage, backgroundimage: CIImage, maskimage: CIImage) -> CIImage {
    let  blendWithRedMaskFilter = CIFilter.blendWithRedMask()
    blendWithRedMaskFilter.inputImage = inputimage
    blendWithRedMaskFilter.maskImage = maskimage
    blendWithRedMaskFilter.backgroundImage = backgroundimage
    return blendWithRedMaskFilter.outputImage!
}
```

![A set of four photographs with two stacked on the left and two side by side on the right. The top photo on the left is of the New York City skyline taken from across the river on an overcast day, with a single boat in the center of the image. The bottom photo on the left is of multiple colorful rocks with green moss covering them. The first photograph on the right is a transparent image with a five-point triangle, hexagon, circle and square filled with a gradient of red to light blue. The second photograph on the right a blend with red mask filter applied, resulting in the skyline photo with the detail of the moss covered rocks showing in the area that is red from the mask image.](https://developer.apple.com/tutorials/images/com.apple.coreimage/media-3624593@2x.png)

## See Also

### Filters
- [class func blendWithAlphaMask() -> any CIFilter & CIBlendWithMask](./blendwithalphamask%28%29.md)
  Blends two images by using an alpha mask image.
- [class func blendWithBlueMask() -> any CIFilter & CIBlendWithMask](./blendwithbluemask%28%29.md)
  Blends two images by using a blue mask image.
- [class func blendWithMask() -> any CIFilter & CIBlendWithMask](./blendwithmask%28%29.md)
  Blends two images by using a mask image.
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
- [class func hexagonalPixellate() -> any CIFilter & CIHexagonalPixellate](./hexagonalpixellate%28%29.md)
  Creates an image made of a series of colorful hexagons.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifilter-swift.class/blendwithredmask())*