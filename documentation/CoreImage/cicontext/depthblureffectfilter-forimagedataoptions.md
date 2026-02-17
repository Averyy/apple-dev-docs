# depthBlurEffectFilter(forImageData:options:)

**Framework**: Core Image  
**Kind**: method

Create a [`CIFilter`](cifilter-swift.class.md) instance for the supplied image data that can be used to apply a depth blur effect.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+

## Declaration

```swift
func depthBlurEffectFilter(forImageData data: Data, options: [AnyHashable : Any]? = nil) -> CIFilter?
```

#### Discussion

The receiver context is used to render the image in order to get the facial landmarks used to create the effect.

## Parameters

- `data`: The image file data to apply the depth blur effect to.
- `options`: Reserved for future use.

## See Also

- [func depthBlurEffectFilter(for: CIImage, disparityImage: CIImage, portraitEffectsMatte: CIImage?, hairSemanticSegmentation: CIImage?, glassesMatte: CIImage?, gainMap: CIImage?, orientation: CGImagePropertyOrientation, options: [AnyHashable : Any]?) -> CIFilter?](cicontext/depthblureffectfilter(for:disparityimage:portraiteffectsmatte:hairsemanticsegmentation:glassesmatte:gainmap:orientation:options:).md)
  Create a [`CIFilter`](cifilter-swift.class.md) instance for the supplied image data that can be used to apply a depth blur effect created with the supplied auxiliary images.
- [func depthBlurEffectFilter(for: CIImage, disparityImage: CIImage, portraitEffectsMatte: CIImage?, hairSemanticSegmentation: CIImage?, orientation: CGImagePropertyOrientation, options: [AnyHashable : Any]?) -> CIFilter?](cicontext/depthblureffectfilter(for:disparityimage:portraiteffectsmatte:hairsemanticsegmentation:orientation:options:).md)
  Create a [`CIFilter`](cifilter-swift.class.md) instance for the supplied image data that can be used to apply a depth blur effect created with the supplied auxiliary images.
- [func depthBlurEffectFilter(for: CIImage, disparityImage: CIImage, portraitEffectsMatte: CIImage?, orientation: CGImagePropertyOrientation, options: [AnyHashable : Any]?) -> CIFilter?](cicontext/depthblureffectfilter(for:disparityimage:portraiteffectsmatte:orientation:options:).md)
  Create a [`CIFilter`](cifilter-swift.class.md) instance for the supplied image data that can be used to apply a depth blur effect created with the supplied auxiliary images.
- [func depthBlurEffectFilter(forImageURL: URL, options: [AnyHashable : Any]?) -> CIFilter?](cicontext/depthblureffectfilter(forimageurl:options:).md)
  Create a [`CIFilter`](cifilter-swift.class.md) instance for the supplied image URL that can be used to apply a depth blur effect.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cicontext/depthblureffectfilter(forimagedata:options:))*