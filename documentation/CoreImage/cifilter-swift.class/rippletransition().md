# rippleTransition()

**Framework**: Core Image  
**Kind**: method  
**Role**: Type Method

Simulates a ripple in a pond to transiton from one image to another.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class func rippleTransition() -> any CIFilter & CIRippleTransition
```

```objc
+ (CIFilter<CIRippleTransition> *) rippleTransitionFilter;
```

## Return Value

The transition image.

## Discussion

This method applies the ripple transition filter to an image. The effect transitions from one image to another by creating a circular wave that expands from the center point, revealing the target image through the wave effect.

The ripple transition filter uses the following properties:

- **`inputImage`**: The starting image with the type [`CIImage`](../ciimage.md).
- **`targetImage`**: The ending image with the type [`CIImage`](../ciimage.md).
- **`center`**: A set of coordinates marking the center of the image as a [`CGPoint`](../../CoreFoundation/cgpoint.md).
- **`width`**: A `float` representing the width of the ripple effect as an [`NSNumber`](../../Foundation/nsnumber.md).
- **`extent`**: A [`CGRect`](../../CoreFoundation/cgrect.md) representing the size of the ripple effect.
- **`scale`**: A `float` representing the scale of the effect as an [`NSNumber`](../../Foundation/nsnumber.md).
- **`time`**: A `float` representing the parametric time of the transition from start (at time 0) to end (at time 1) as an [`NSNumber`](../../Foundation/nsnumber.md).

The following code creates a filter that transitions from the input image to the target image with a water-like ripple effect.

```swift
func ripple (inputImage: CIImage, targetImage: CIImage) -> CIImage {
    let rippleTransition = CIFilter.rippleTransition()
    rippleTransition.inputImage = inputImage
    rippleTransition.targetImage = targetImage
    rippleTransition.center = CGPoint(x: 250, y: 150)
    rippleTransition.width = 100
    rippleTransition.extent = CGRect(x: 54, y: 80, width: 300, height: 300)
    rippleTransition.scale = 22
    rippleTransition.time = 0.3
    return rippleTransition.outputImage!
}
```

![Three photographs. In the photo on the left, there are multiple small purple flowers photographed close up with good lighting, and the background has a slight blur. In the photograph on the right is a tall building with two trees directly in front of the building. In the center photograph, a ripple transition filter is applied, resulting in a still photo of the moving transition. The left photograph is overlaid on the phot on the right appearing as a ripple in a pond, slowly fading the flower image to become the city photograph.](https://developer.apple.com/tutorials/images/com.apple.coreimage/media-3616425@2x.png)

## See Also

### Filters
- [class func accordionFoldTransition() -> any CIFilter & CIAccordionFoldTransition](./accordionfoldtransition%28%29.md)
  Transitions by folding and crossfading an image to reveal the target image.
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
- [class func swipeTransition() -> any CIFilter & CISwipeTransition](./swipetransition%28%29.md)
  Gradually transitions from one image to another with a swiping motion.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifilter-swift.class/rippletransition())*