# PHVideoRequestOptionsDeliveryMode

**Framework**: Photos  
**Kind**: enum  
**Role**: Enumeration

Options for delivering requested video data, used by the [`deliveryMode`](./phvideorequestoptions/deliverymode.md) property.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
enum PHVideoRequestOptionsDeliveryMode
```

```c
enum PHVideoRequestOptionsDeliveryMode : NSInteger;
```

## Topics

### Constants
- [PHVideoRequestOptionsDeliveryMode.automatic](./phvideorequestoptionsdeliverymode/automatic.md)
  Photos automatically determines which quality of video data to provide based on the request and current conditions.
- [PHVideoRequestOptionsDeliveryMode.highQualityFormat](./phvideorequestoptionsdeliverymode/highqualityformat.md)
  Photos provides only the highest quality video available.
- [PHVideoRequestOptionsDeliveryMode.mediumQualityFormat](./phvideorequestoptionsdeliverymode/mediumqualityformat.md)
  Photos provides a video of moderate quality unless a higher quality version is locally cached.
- [PHVideoRequestOptionsDeliveryMode.fastFormat](./phvideorequestoptionsdeliverymode/fastformat.md)
  Photos provides whatever quality of video can be most quickly loaded.
### Initializers
- [init?(rawValue: Int)](./phvideorequestoptionsdeliverymode/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Specifying Video Request Options
- [var version: PHVideoRequestOptionsVersion](./phvideorequestoptions/version.md)
  The version of the video to request.
- [enum PHVideoRequestOptionsVersion](./phvideorequestoptionsversion.md)
  Options for requesting a video asset with or without adjustments, used by the [`version`](./phvideorequestoptions/version.md) property.
- [var deliveryMode: PHVideoRequestOptionsDeliveryMode](./phvideorequestoptions/deliverymode.md)
  A mode specifying the requested video quality and delivery priority.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phvideorequestoptionsdeliverymode)*