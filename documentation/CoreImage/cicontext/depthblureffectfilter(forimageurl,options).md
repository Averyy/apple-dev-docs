# depthBlurEffectFilter(forImageURL:options:)

**Framework**: Core Image  
**Kind**: method  
**Role**: Instance Method

Create a [`CIFilter`](../cifilter-swift.class.md) instance for the supplied image URL that can be used to apply a depth blur effect.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+

## Declaration

```swift
func depthBlurEffectFilter(forImageURL url: URL, options: [AnyHashable : Any]? = nil) -> CIFilter?
```

```objc
- (CIFilter *) depthBlurEffectFilterForImageURL:(NSURL *) url options:(NSDictionary *) options;
```

## Discussion

The receiver context is used to render the image in order to get the facial landmarks used to create the effect.

## Parameters

- `url`: The URL location of the image to apply the depth blur effect to.
- `options`: Reserved for future use.

## See Also

### Creating Depth Blur Filters
- [func depthBlurEffectFilter(for: CIImage, disparityImage: CIImage, portraitEffectsMatte: CIImage?, hairSemanticSegmentation: CIImage?, glassesMatte: CIImage?, gainMap: CIImage?, orientation: CGImagePropertyOrientation, options: [AnyHashable : Any]?) -> CIFilter?](./depthblureffectfilter%28for,disparityimage,portraiteffectsmatte,hairsemanticsegmentation,glassesmatte,gainmap,orientation,options%29.md)
  Create a [`CIFilter`](../cifilter-swift.class.md) instance for the supplied image data that can be used to apply a depth blur effect created with the supplied auxiliary images.
- [func depthBlurEffectFilter(for: CIImage, disparityImage: CIImage, portraitEffectsMatte: CIImage?, hairSemanticSegmentation: CIImage?, orientation: CGImagePropertyOrientation, options: [AnyHashable : Any]?) -> CIFilter?](./depthblureffectfilter%28for,disparityimage,portraiteffectsmatte,hairsemanticsegmentation,orientation,options%29.md)
  Create a [`CIFilter`](../cifilter-swift.class.md) instance for the supplied image data that can be used to apply a depth blur effect created with the supplied auxiliary images.
- [func depthBlurEffectFilter(for: CIImage, disparityImage: CIImage, portraitEffectsMatte: CIImage?, orientation: CGImagePropertyOrientation, options: [AnyHashable : Any]?) -> CIFilter?](./depthblureffectfilter%28for,disparityimage,portraiteffectsmatte,orientation,options%29.md)
  Create a [`CIFilter`](../cifilter-swift.class.md) instance for the supplied image data that can be used to apply a depth blur effect created with the supplied auxiliary images.
- [func depthBlurEffectFilter(forImageData: Data, options: [AnyHashable : Any]?) -> CIFilter?](./depthblureffectfilter%28forimagedata,options%29.md)
  Create a [`CIFilter`](../cifilter-swift.class.md) instance for the supplied image data that can be used to apply a depth blur effect.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cicontext/depthblureffectfilter(forimageurl:options:))*