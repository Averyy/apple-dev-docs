# accordionFoldTransition()

**Framework**: Core Image  
**Kind**: method  
**Role**: Type Method

Transitions by folding and crossfading an image to reveal the target image.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class func accordionFoldTransition() -> any CIFilter & CIAccordionFoldTransition
```

```objc
+ (CIFilter<CIAccordionFoldTransition> *) accordionFoldTransitionFilter;
```

## Return Value

The transition image.

## Discussion

This method applies the accordion fold transition filter to an image. The effect transitions from one image to another by unfolding and crossfading.

The accordion fold transition filter uses the following properties:

- **`inputImage`**: The starting image with the type [`CIImage`](../ciimage.md).
- **`targetImage`**: The ending image with the type [`CIImage`](../ciimage.md).
- **`time`**: A `float` representing the parametric time of the transition from start (at time 0) to end (at time 1) as an [`NSNumber`](../../Foundation/nsnumber.md).
- **`numberOfFolds`**: A `float` representing the number of accordion folds as a [`NSNumber`](../../Foundation/nsnumber.md).
- **`foldShadowAmount`**: A `float` representing the strength of the shadow as a [`NSNumber`](../../Foundation/nsnumber.md).

The following code creates a filter that produces folds in the input image and fades to the target image:

```swift
func accordionFold(inputImage: CIImage, targetImage: CIImage) -> CIImage {
    let accordionFoldTransiton = CIFilter.accordionFoldTransition()
    accordionFoldTransiton.inputImage = inputImage
    accordionFoldTransiton.targetImage = targetImage
    accordionFoldTransiton.time = 0.5
    accordionFoldTransiton.numberOfFolds = 6
    accordionFoldTransiton.foldShadowAmount = 2
    return accordionFoldTransiton.outputImage!
}
```

![Three photographs. In the photo on the left, multiple sets of small purple flowers are photographed close up with good lighting, and the background has a slight blur. In the photograph on the right is a tall city building with two trees directly in front of the building. In the center photo, a bar swipe transition is applied, resulting in a still photograph of the moving transition. The left photograph is overlaid on the right photo and slowly folding up to reveal the target image.](https://developer.apple.com/tutorials/images/com.apple.coreimage/media-3616429@2x.png)

## See Also

### Filters
- [class func barsSwipeTransition() -> any CIFilter & CIBarsSwipeTransition](./barsswipetransition%28%29.md)
  Transitions between two images by removing rectangular portions of an image.
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

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifilter-swift.class/accordionfoldtransition())*