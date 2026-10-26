# PHImageRequestOptionsResizeMode

**Framework**: Photos  
**Kind**: enum  
**Role**: Enumeration

Options for how to resize the requested image to fit a target size, used by the [`resizeMode`](./phimagerequestoptions/resizemode.md) property.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
enum PHImageRequestOptionsResizeMode
```

```c
enum PHImageRequestOptionsResizeMode : NSInteger;
```

#### Overview

Specify a `targetSize` parameter when you request an image with the [`requestImage(for:targetSize:contentMode:options:resultHandler:)`](./phimagemanager/requestimage%28for,targetsize,contentmode,options,resulthandler%29.md) method.

## Topics

### Constants
- [PHImageRequestOptionsResizeMode.none](./phimagerequestoptionsresizemode/none.md)
  Photos does not resize the image asset.
- [PHImageRequestOptionsResizeMode.fast](./phimagerequestoptionsresizemode/fast.md)
  Photos efficiently resizes the image to a size similar to, or slightly larger than, the target size.
- [PHImageRequestOptionsResizeMode.exact](./phimagerequestoptionsresizemode/exact.md)
  Photos resizes the image to match the target size exactly.
### Initializers
- [init?(rawValue: Int)](./phimagerequestoptionsresizemode/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Specifying Image Request Options
- [var version: PHImageRequestOptionsVersion](./phimagerequestoptions/version.md)
  The version of the image to be requested.
- [enum PHImageRequestOptionsVersion](./phimagerequestoptionsversion.md)
  Options for requesting an image asset with or without adjustments, used by the [`version`](./phimagerequestoptions/version.md) property.
- [var deliveryMode: PHImageRequestOptionsDeliveryMode](./phimagerequestoptions/deliverymode.md)
  The requested image quality and delivery priority.
- [enum PHImageRequestOptionsDeliveryMode](./phimagerequestoptionsdeliverymode.md)
  Options for delivering requested image data, used by the [`deliveryMode`](./phimagerequestoptions/deliverymode.md) property.
- [var resizeMode: PHImageRequestOptionsResizeMode](./phimagerequestoptions/resizemode.md)
  A mode that specifies how to resize the requested image.
- [var normalizedCropRect: CGRect](./phimagerequestoptions/normalizedcroprect.md)
  A rectangle for requesting a cropped version of the original image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phimagerequestoptionsresizemode)*