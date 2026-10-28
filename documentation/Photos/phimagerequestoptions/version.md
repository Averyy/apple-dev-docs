# version

**Framework**: Photos  
**Kind**: property  
**Role**: Instance Property

The version of the image to be requested.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var version: PHImageRequestOptionsVersion { get set }
```

```objc
@property (nonatomic, assign) PHImageRequestOptionsVersion version;
```

## Discussion

Use this property to request a version of the image with or without adjustments, or to request high-quality original data (for example, a RAW file) if such is available. See [`PHImageRequestOptionsVersion`](../phimagerequestoptionsversion.md).

## See Also

### Specifying Image Request Options
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
- [var normalizedCropRect: CGRect](./normalizedcroprect.md)
  A rectangle for requesting a cropped version of the original image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phimagerequestoptions/version)*