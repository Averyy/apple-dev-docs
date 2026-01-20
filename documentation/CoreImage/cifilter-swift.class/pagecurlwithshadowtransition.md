# pageCurlWithShadowTransition()

**Framework**: Core Image  
**Kind**: method

Simulates the curl of a page, revealing the target image with added shadow.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class func pageCurlWithShadowTransition() -> any CIFilter & CIPageCurlWithShadowTransition
```

## Mentions

- [Customizing Image Transitions](customizing-image-transitions.md)

#### Return Value

The transition image.

#### Discussion

This method applies the page curl with shadow transition filter to an image. The effect transitions from one image to another by simulating a curling page, revealing the target image as the page curls with a shadow effect from the backside image.

The page curl with shadow transition filter uses the following properties:

The following code creates a page curling back to reveal the target image with an added shadow.

```swift
func pageCurl(inputImage: CIImage, targetImage: CIImage, backsideImage: CIImage) -> CIImage {
    let pageCurlTransition = CIFilter.pageCurlWithShadowTransition()
    pageCurlTransition.inputImage = inputImage
    pageCurlTransition.targetImage = targetImage
    pageCurlTransition.backsideImage = backsideImage
    pageCurlTransition.extent = CGRect(x: 54, y: 90, width: 300, height: 300)
    pageCurlTransition.time = 0.5
    pageCurlTransition.angle = 4
    pageCurlTransition.radius = 100
    pageCurlTransition.shadowAmount = 10
    pageCurlTransition.shadowSize = 6
    pageCurlTransition.shadowExtent = CGRect(x: 32, y: 56, width: 400, height: 400)
    return pageCurlTransition.outputImage!
}
```

![Three photographs. In the photo on the left, there are multiple small purple flowers photographed close up with good lighting, and the background has a slight blur. In the photograph on the right is a tall building with two trees directly in front of the building. In the center photograph, a page curl with shadow filter is applied, resulting in a still photo of the moving transition. The left photograph is overlaid on the photo on the right with the left side of the overlaid image curling up to reveal more of the city image under. The curl has an added shadow to the underside.](https://docs-assets.developer.apple.com/published/88d677ea78614c06bec80dfe35c25d48/media-3616423%402x.png)

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
- [class func pageCurlTransition() -> any CIFilter & CIPageCurlTransition](cifilter-swift.class/pagecurltransition.md)
  Simulates the curl of a page, revealing the target image.
- [class func rippleTransition() -> any CIFilter & CIRippleTransition](cifilter-swift.class/rippletransition.md)
  Simulates a ripple in a pond to transiton from one image to another.
- [class func swipeTransition() -> any CIFilter & CISwipeTransition](cifilter-swift.class/swipetransition.md)
  Gradually transitions from one image to another with a swiping motion.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifilter-swift.class/pagecurlwithshadowtransition())*