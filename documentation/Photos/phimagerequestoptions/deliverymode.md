# deliveryMode

**Framework**: Photos  
**Kind**: property  
**Role**: Instance Property

The requested image quality and delivery priority.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var deliveryMode: PHImageRequestOptionsDeliveryMode { get set }
```

```objc
@property (nonatomic, assign) PHImageRequestOptionsDeliveryMode deliveryMode;
```

## Discussion

Use this property to tell Photos to provide an image quickly (possibly sacrificing image quality), to provide a high-quality image (possibly sacrificing speed), or to provide both automatically if needed. See [`PHImageRequestOptionsDeliveryMode`](../phimagerequestoptionsdeliverymode.md).

## See Also

### Specifying Image Request Options
- [var version: PHImageRequestOptionsVersion](./version.md)
  The version of the image to be requested.
- [enum PHImageRequestOptionsVersion](../phimagerequestoptionsversion.md)
  Options for requesting an image asset with or without adjustments, used by the [`version`](./version.md) property.
- [enum PHImageRequestOptionsDeliveryMode](../phimagerequestoptionsdeliverymode.md)
  Options for delivering requested image data, used by the [`deliveryMode`](./deliverymode.md) property.
- [var resizeMode: PHImageRequestOptionsResizeMode](./resizemode.md)
  A mode that specifies how to resize the requested image.
- [enum PHImageRequestOptionsResizeMode](../phimagerequestoptionsresizemode.md)
  Options for how to resize the requested image to fit a target size, used by the [`resizeMode`](./resizemode.md) property.
- [var normalizedCropRect: CGRect](./normalizedcroprect.md)
  A rectangle for requesting a cropped version of the original image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phimagerequestoptions/deliverymode)*