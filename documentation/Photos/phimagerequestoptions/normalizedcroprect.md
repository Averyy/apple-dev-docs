# normalizedCropRect

**Framework**: Photos  
**Kind**: property  
**Role**: Instance Property

A rectangle for requesting a cropped version of the original image.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var normalizedCropRect: CGRect { get set }
```

```objc
@property (nonatomic, assign) CGRect normalizedCropRect;
```

## Discussion

To request a cropped image, specify the crop rectangle in a unit coordinate space relative to the image. In this coordinate system, the point `{0.0,0.0}` refers to the upper left corner of the image, and the point `{1.0,1.0}` refers to the opposite corner regardless of the image’s aspect ratio.

This property defaults to [`CGRectZero`](../../CoreGraphics/cgrectzero.md), which specifies no cropping.

If you specify a crop rectangle, you must also specify the [`PHImageRequestOptionsResizeMode.exact`](../phimagerequestoptionsresizemode/exact.md) option for the [`resizeMode`](./resizemode.md) property.

## See Also

### Specifying Image Request Options
- [var version: PHImageRequestOptionsVersion](./version.md)
  The version of the image to be requested.
- [enum PHImageRequestOptionsVersion](../phimagerequestoptionsversion.md)
  Options for requesting an image asset with or without adjustments, used by the [`version`](./version.md) property.
- [var deliveryMode: PHImageRequestOptionsDeliveryMode](./deliverymode.md)
  The requested image quality and delivery priority.
- [enum PHImageRequestOptionsDeliveryMode](../phimagerequestoptionsdeliverymode.md)
  Options for delivering requested image data, used by the [`deliveryMode`](./deliverymode.md) property.
- [var resizeMode: PHImageRequestOptionsResizeMode](./resizemode.md)
  A mode that specifies how to resize the requested image.
- [enum PHImageRequestOptionsResizeMode](../phimagerequestoptionsresizemode.md)
  Options for how to resize the requested image to fit a target size, used by the [`resizeMode`](./resizemode.md) property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phimagerequestoptions/normalizedcroprect)*