# pageCurlTransition()

**Framework**: Core Image  
**Kind**: method

Simulates the curl of a page, revealing the target image.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class func pageCurlTransition() -> any CIFilter & CIPageCurlTransition
```

#### Return Value

The transition image.

#### Discussion

This method applies the page curl transition filter to an image. The effect transitions from one image to another by simulating a curling page, revealing the target image as the page curls.

The page curl transition filter uses the following properties:

- **`inputImage`**: The starting image with the type [`CIImage`](ciimage.md).
- **`targetImage`**: The ending image with the type [`CIImage`](ciimage.md).
- **`backsideImage`**: An image used as the backside of the curl with the type [`CIImage`](ciimage.md).
- **`extent`**: A [`CGRect`](https://developer.apple.com/documentation/CoreFoundation/CGRect) representing the size of the effect.
- **`time`**: A `float` representing the parametric time of the transition from start (at time 0) to end (at time 1) as an [`NSNumber`](https://developer.apple.com/documentation/Foundation/NSNumber).
- **`angle`**: A `float` representing the angle of the motion of the curl as an [`NSNumber`](https://developer.apple.com/documentation/Foundation/NSNumber).
- **`radius`**: A `float` representing the radius of the curl as an [`NSNumber`](https://developer.apple.com/documentation/Foundation/NSNumber).

The following code creates a filter that produces a page curling back to reveal the target image.

```swift
func pageCurl(inputImage: CIImage, targetImage: CIImage, backsideImage: CIImage) -> CIImage {
    let pageCurlTransition = CIFilter.pageCurlTransition()
    pageCurlTransition.inputImage = inputImage
    pageCurlTransition.targetImage = targetImage
    pageCurlTransition.backsideImage = backsideImage
    pageCurlTransition.extent = CGRect(x: 54, y: 90, width: 300, height: 300)
    pageCurlTransition.time = 5.6
    pageCurlTransition.angle = 0.9
    pageCurlTransition.radius = 150
    return pageCurlTransition.outputImage!
}
```

![Three photographs. In the photo on the left, there are multiple small purple flowers photographed close up with good lighting, and the background has a slight blur. In the photograph on the right is a tall building with two trees directly in front of the building. In the center photograph, a page curl transition filter is applied, resulting in a still photo of the moving transition. The left photograph is overlaid on the photo on the right with the bottom left corner of the top image appearing to be curled to reveal the city photograph, like the page of a book.](https://docs-assets.developer.apple.com/published/9a5feb03780a0c06783547cf574ceb08/media-3616422%402x.png)

## See Also

- [class func accordionFoldTransition() -> any CIFilter & CIAccordionFoldTransition](cifilter-swift.class/accordionfoldtransition.md)
  Transitions by folding and crossfading an image to reveal the target image.
- [class func barsSwipeTransition() -> any CIFilter & CIBarsSwipeTransition](cifilter-swift.class/barsswipetransition.md)
  Transitions between two images by removing rectangular portions of an image.
- [class func copyMachineTransition() -> any CIFilter & CICopyMachineTransition](cifilter-swift.class/copymachinetransition.md)
  Simulates the effect of a copy machine scanner light to transiton between two images.
- [class func disintegrateWithMaskTransition() -> any CIFilter & CIDisintegrateWithMaskTransition](cifilter-swift.class/disintegratewithmasktransition.md)
  Transitions between two images using a mask image.
- [class func dissolveTransition() -> any CIFilter & CIDissolveTransition](cifilter-swift.class/dissolvetransition.md)
  Transitions between two images with a fade effect.
- [class func flashTransition() -> any CIFilter & CIFlashTransition](cifilter-swift.class/flashtransition.md)
  Creates a flash of light to transition between two images.
- [class func modTransition() -> any CIFilter & CIModTransition](cifilter-swift.class/modtransition.md)
  Transitions between two images by applying irregularly shaped holes.
- [class func pageCurlWithShadowTransition() -> any CIFilter & CIPageCurlWithShadowTransition](cifilter-swift.class/pagecurlwithshadowtransition.md)
  Simulates the curl of a page, revealing the target image with added shadow.
- [class func rippleTransition() -> any CIFilter & CIRippleTransition](cifilter-swift.class/rippletransition.md)
  Simulates a ripple in a pond to transiton from one image to another.
- [class func swipeTransition() -> any CIFilter & CISwipeTransition](cifilter-swift.class/swipetransition.md)
  Gradually transitions from one image to another with a swiping motion.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifilter-swift.class/pagecurltransition())*