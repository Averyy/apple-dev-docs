# flashTransition()

**Framework**: Core Image  
**Kind**: method

Creates a flash of light to transition between two images.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class func flashTransition() -> any CIFilter & CIFlashTransition
```

#### Return Value

The transition image.

#### Discussion

This method applies the flash transition filter to an image. The effect transitions from the input image to the target image by creating a flash that fills the image and fades to the target image.

The flash transition filter uses the following properties:

The following code creates a filter that transitions from the input image with a large flash of light and fades to the target image.

```swift
func flash (inputImage: CIImage, targetImage: CIImage) -> CIImage {
    let flashTransition = CIFilter.flashTransition()
    flashTransition.inputImage = inputImage
    flashTransition.targetImage = targetImage
    flashTransition.center = CGPoint(x: 253, y: 372)
    flashTransition.extent = CGRect(x: 0, y: 0, width: 300, height: 300)
    flashTransition.color = .white
    flashTransition.time = 0.5
    flashTransition.maxStriationRadius = 2.58
    flashTransition.striationStrength = 0.5
    flashTransition.striationContrast = 1.375
    flashTransition.fadeThreshold = 0.06
    return flashTransition.outputImage!
}
```

![Three photographs. In the photo on the left, there are multiple small purple flowers photographed close up with good lighting, and the background has a slight blur. In the photograph on the right is a tall building with two trees directly in front of the building. In the center photograph, a flash transition filter is applied, resulting in a still photo of the moving transition. The left photograph is overlaid on the photo on the right while transitioning by creating a flash of light and slowly fading to the city image.](https://docs-assets.developer.apple.com/published/1cc800de07fe8e9fc18f3a1e056ae18c/media-3616427%402x.png)

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
- [class func modTransition() -> any CIFilter & CIModTransition](cifilter-swift.class/modtransition.md)
  Transitions between two images by applying irregularly shaped holes.
- [class func pageCurlTransition() -> any CIFilter & CIPageCurlTransition](cifilter-swift.class/pagecurltransition.md)
  Simulates the curl of a page, revealing the target image.
- [class func pageCurlWithShadowTransition() -> any CIFilter & CIPageCurlWithShadowTransition](cifilter-swift.class/pagecurlwithshadowtransition.md)
  Simulates the curl of a page, revealing the target image with added shadow.
- [class func rippleTransition() -> any CIFilter & CIRippleTransition](cifilter-swift.class/rippletransition.md)
  Simulates a ripple in a pond to transiton from one image to another.
- [class func swipeTransition() -> any CIFilter & CISwipeTransition](cifilter-swift.class/swipetransition.md)
  Gradually transitions from one image to another with a swiping motion.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifilter-swift.class/flashtransition())*