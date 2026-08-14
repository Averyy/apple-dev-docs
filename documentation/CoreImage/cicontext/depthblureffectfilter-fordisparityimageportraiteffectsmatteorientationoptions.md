# depthBlurEffectFilter(for:disparityImage:portraitEffectsMatte:orientation:options:)

**Framework**: Core Image  
**Kind**: method

Create a [`CIFilter`](cifilter-swift.class.md) instance for the supplied image data that can be used to apply a depth blur effect created with the supplied auxiliary images.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+

## Declaration

```swift
func depthBlurEffectFilter(for image: CIImage, disparityImage: CIImage, portraitEffectsMatte: CIImage?, orientation: CGImagePropertyOrientation, options: [AnyHashable : Any]? = nil) -> CIFilter?
```

#### Discussion

The receiver context is used to render the image in order to get the facial landmarks used to create the effect. The auxiliary images used to create the filter can be obtained from a JPEG or HEIC file containing embedded portrait effects matte data.

## Parameters

- `image`: The image object to apply the depth blur effect to.
- `disparityImage`: The auxiliary disparity image. For more information, see [`auxiliaryDisparity`](ciimageoption/auxiliarydisparity.md).
- `portraitEffectsMatte`: The portrait effects matte image. For more information, see [`auxiliaryPortraitEffectsMatte`](ciimageoption/auxiliaryportraiteffectsmatte.md).
- `orientation`: The intended display orientation for the image.
- `options`: Reserved for future use.

## See Also

- [struct CIImageOption](ciimageoption.md)
- [Configuring camera capture to collect a Portrait Effects matte](../avfoundation/configuring-camera-capture-to-collect-a-portrait-effects-matte.md)
  Prepare your app to capture a portrait effects matte when taking photos.
- [func depthBlurEffectFilter(for: CIImage, disparityImage: CIImage, portraitEffectsMatte: CIImage?, hairSemanticSegmentation: CIImage?, glassesMatte: CIImage?, gainMap: CIImage?, orientation: CGImagePropertyOrientation, options: [AnyHashable : Any]?) -> CIFilter?](cicontext/depthblureffectfilter(for:disparityimage:portraiteffectsmatte:hairsemanticsegmentation:glassesmatte:gainmap:orientation:options:).md)
  Create a [`CIFilter`](cifilter-swift.class.md) instance for the supplied image data that can be used to apply a depth blur effect created with the supplied auxiliary images.
- [func depthBlurEffectFilter(for: CIImage, disparityImage: CIImage, portraitEffectsMatte: CIImage?, hairSemanticSegmentation: CIImage?, orientation: CGImagePropertyOrientation, options: [AnyHashable : Any]?) -> CIFilter?](cicontext/depthblureffectfilter(for:disparityimage:portraiteffectsmatte:hairsemanticsegmentation:orientation:options:).md)
  Create a [`CIFilter`](cifilter-swift.class.md) instance for the supplied image data that can be used to apply a depth blur effect created with the supplied auxiliary images.
- [func depthBlurEffectFilter(forImageData: Data, options: [AnyHashable : Any]?) -> CIFilter?](cicontext/depthblureffectfilter(forimagedata:options:).md)
  Create a [`CIFilter`](cifilter-swift.class.md) instance for the supplied image data that can be used to apply a depth blur effect.
- [func depthBlurEffectFilter(forImageURL: URL, options: [AnyHashable : Any]?) -> CIFilter?](cicontext/depthblureffectfilter(forimageurl:options:).md)
  Create a [`CIFilter`](cifilter-swift.class.md) instance for the supplied image URL that can be used to apply a depth blur effect.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cicontext/depthblureffectfilter(for:disparityimage:portraiteffectsmatte:orientation:options:))*