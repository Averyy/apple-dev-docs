# PHImageRequestOptionsVersion

**Framework**: Photos  
**Kind**: enum  
**Role**: Enumeration

Options for requesting an image asset with or without adjustments, used by the [`version`](./phimagerequestoptions/version.md) property.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
enum PHImageRequestOptionsVersion
```

```c
enum PHImageRequestOptionsVersion : NSInteger;
```

## Topics

### Constants
- [PHImageRequestOptionsVersion.current](./phimagerequestoptionsversion/current.md)
  Request the most recent version of the image asset (the one that reflects all edits).
- [PHImageRequestOptionsVersion.unadjusted](./phimagerequestoptionsversion/unadjusted.md)
  Request a version of the image asset without adjustments.
- [PHImageRequestOptionsVersion.original](./phimagerequestoptionsversion/original.md)
  Request the original, highest-fidelity version of the image asset.
### Initializers
- [init?(rawValue: Int)](./phimagerequestoptionsversion/init%28rawvalue%29.md)

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
- [var deliveryMode: PHImageRequestOptionsDeliveryMode](./phimagerequestoptions/deliverymode.md)
  The requested image quality and delivery priority.
- [enum PHImageRequestOptionsDeliveryMode](./phimagerequestoptionsdeliverymode.md)
  Options for delivering requested image data, used by the [`deliveryMode`](./phimagerequestoptions/deliverymode.md) property.
- [var resizeMode: PHImageRequestOptionsResizeMode](./phimagerequestoptions/resizemode.md)
  A mode that specifies how to resize the requested image.
- [enum PHImageRequestOptionsResizeMode](./phimagerequestoptionsresizemode.md)
  Options for how to resize the requested image to fit a target size, used by the [`resizeMode`](./phimagerequestoptions/resizemode.md) property.
- [var normalizedCropRect: CGRect](./phimagerequestoptions/normalizedcroprect.md)
  A rectangle for requesting a cropped version of the original image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phimagerequestoptionsversion)*