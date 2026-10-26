# resizeMode

**Framework**: Photos  
**Kind**: property  
**Role**: Instance Property

A mode that specifies how to resize the requested image.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var resizeMode: PHImageRequestOptionsResizeMode { get set }
```

```objc
@property (nonatomic, assign) PHImageRequestOptionsResizeMode resizeMode;
```

#### Discussion

Use this property to choose how to fit the image to the target size you specified when requesting image data. The default value for this property is [`PHImageRequestOptionsResizeMode.fast`](../phimagerequestoptionsresizemode/fast.md).

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
- [enum PHImageRequestOptionsResizeMode](../phimagerequestoptionsresizemode.md)
  Options for how to resize the requested image to fit a target size, used by the [`resizeMode`](./resizemode.md) property.
- [var normalizedCropRect: CGRect](./normalizedcroprect.md)
  A rectangle for requesting a cropped version of the original image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phimagerequestoptions/resizemode)*