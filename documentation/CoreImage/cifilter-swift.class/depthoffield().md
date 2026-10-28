# depthOfField()

**Framework**: Core Image  
**Kind**: method  
**Role**: Type Method

Simulates a depth of field effect.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class func depthOfField() -> any CIFilter & CIDepthOfField
```

```objc
+ (CIFilter<CIDepthOfField> *) depthOfFieldFilter;
```

## Return Value

The modified image.

## Discussion

This method applies the depth of field filter to an image. The effect simulates changing the focus of the camera before taking a photograph.

The depth of field filter uses the following properties:

- **`inputImage`**: An image with the type [`CIImage`](../ciimage.md).
- **`radius`**: A `float` representing the area of effect as an [`NSNumber`](../../Foundation/nsnumber.md).
- **`point0`**: A set of coordinates marking the first point to be focused on as a [`CGPoint`](../../CoreFoundation/cgpoint.md).
- **`point1`**: A set of coordinates marking the second point to be focused on as a [`CGPoint`](../../CoreFoundation/cgpoint.md).
- **`unsharpMaskRadius`**: A `float` representing the radius of the unsharpened mask effect applied to the in-focus area of effect as an [`NSNumber`](../../Foundation/nsnumber.md).
- **`unsharpMaskIntensity`**: A `float` representing the intensity of the unsharp mask effect as an [`NSNumber`](../../Foundation/nsnumber.md).

The following code creates a filter that results in the center cilantro being in focus while gradually blurring to the top and bottom of the image:

```swift
func depthOfField(inputImage: CIImage) -> CIImage {
    let depthOfFieldFilter = CIFilter.depthOfField()
    depthOfFieldFilter.inputImage = inputImage
    depthOfFieldFilter.radius = 5
    depthOfFieldFilter.point0 = CGPoint(x: 2349, y: 846)
    depthOfFieldFilter.point1 = CGPoint(x: 571, y: 3121)
    depthOfFieldFilter.unsharpMaskRadius = 7
    depthOfFieldFilter.unsharpMaskIntensity = 10
    return depthOfFieldFilter.outputImage!
}
```

![Two photographs of a pile of cilantro. The photo on the left is clear and crisp with good lighting. In the photo on the right, a depth of field filter is applied, resulting in the cilantro in the image’s periphery becoming blurred while the center remains in focus.](https://developer.apple.com/tutorials/images/com.apple.coreimage/media-3599997@2x.png)

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

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifilter-swift.class/depthoffield())*