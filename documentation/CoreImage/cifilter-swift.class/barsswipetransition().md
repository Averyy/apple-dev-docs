# barsSwipeTransition()

**Framework**: Core Image  
**Kind**: method  
**Role**: Type Method

Transitions between two images by removing rectangular portions of an image.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class func barsSwipeTransition() -> any CIFilter & CIBarsSwipeTransition
```

```objc
+ (CIFilter<CIBarsSwipeTransition> *) barsSwipeTransitionFilter;
```

## Mentions

- [Customizing Image Transitions](../customizing-image-transitions.md)

#### Return Value

The transition image.

#### Discussion

This method applies the bar swipe transition filter to an image. The effect transitions from one image to another by a series of moving bars passing over the target image.

The bar swipe transition filter uses the following properties:

- **`inputImage`**: The starting image with the type [`CIImage`](../ciimage.md).
- **`targetImage`**: The ending image with the type [`CIImage`](../ciimage.md).
- **`time`**: A `float` representing the parametric time of the transition from start (at time 0) to end (at time 1) as an [`NSNumber`](../../Foundation/nsnumber.md).
- **`angle`**: A `float` representing the angle of the motion as an [`NSNumber`](../../Foundation/nsnumber.md).
- **`width`**: A `float` representing the width of the bars in pixels as an [`NSNumber`](../../Foundation/nsnumber.md).
- **`barOffset`**: A `float` representing the offset of one bar in relation to others as a [`NSNumber`](../../Foundation/nsnumber.md).

The following code creates a filter that produces falling bars from the input image to transition to the target image:

```swift
func barSwipe(inputImage: CIImage, targetImage: CIImage) -> CIImage {
    let barSwipeTranstion = CIFilter.barsSwipeTransition()
    barSwipeTranstion.inputImage = inputImage
    barSwipeTranstion.targetImage = targetImage
    barSwipeTranstion.time = 0.5
    barSwipeTranstion.angle = 0.09
    barSwipeTranstion.width = 30
    barSwipeTranstion.barOffset = 10   
    return barSwipeTranstion.outputImage!
}
```

![Three photographs. In the photo on the left, multiple sets of small purple flowers are photographed close up with good lighting, and the background has a slight blur. In the photograph on the right is a tall city building with two trees directly in front of the building. The center photograph is a snapshot of the moment that the bar swipe transition creates, where the left photo slowly fades away by sized bars moving out of frame, revealing the city building.](https://developer.apple.com/tutorials/images/com.apple.coreimage/media-3616431@2x.png)

## See Also

### Filters
- [class func accordionFoldTransition() -> any CIFilter & CIAccordionFoldTransition](./accordionfoldtransition%28%29.md)
  Transitions by folding and crossfading an image to reveal the target image.
- [class func copyMachineTransition() -> any CIFilter & CICopyMachineTransition](./copymachinetransition%28%29.md)
  Simulates the effect of a copy machine scanner light to transiton between two images.
- [class func disintegrateWithMaskTransition() -> any CIFilter & CIDisintegrateWithMaskTransition](./disintegratewithmasktransition%28%29.md)
  Transitions between two images using a mask image.
- [class func dissolveTransition() -> any CIFilter & CIDissolveTransition](./dissolvetransition%28%29.md)
  Transitions between two images with a fade effect.
- [class func flashTransition() -> any CIFilter & CIFlashTransition](./flashtransition%28%29.md)
  Creates a flash of light to transition between two images.
- [class func modTransition() -> any CIFilter & CIModTransition](./modtransition%28%29.md)
  Transitions between two images by applying irregularly shaped holes.
- [class func pageCurlTransition() -> any CIFilter & CIPageCurlTransition](./pagecurltransition%28%29.md)
  Simulates the curl of a page, revealing the target image.
- [class func pageCurlWithShadowTransition() -> any CIFilter & CIPageCurlWithShadowTransition](./pagecurlwithshadowtransition%28%29.md)
  Simulates the curl of a page, revealing the target image with added shadow.
- [class func rippleTransition() -> any CIFilter & CIRippleTransition](./rippletransition%28%29.md)
  Simulates a ripple in a pond to transiton from one image to another.
- [class func swipeTransition() -> any CIFilter & CISwipeTransition](./swipetransition%28%29.md)
  Gradually transitions from one image to another with a swiping motion.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifilter-swift.class/barsswipetransition())*