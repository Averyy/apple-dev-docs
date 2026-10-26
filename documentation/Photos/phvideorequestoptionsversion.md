# PHVideoRequestOptionsVersion

**Framework**: Photos  
**Kind**: enum  
**Role**: Enumeration

Options for requesting a video asset with or without adjustments, used by the [`version`](./phvideorequestoptions/version.md) property.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
enum PHVideoRequestOptionsVersion
```

```c
enum PHVideoRequestOptionsVersion : NSInteger;
```

## Topics

### Constants
- [PHVideoRequestOptionsVersion.current](./phvideorequestoptionsversion/current.md)
  Request the most recent version of the video asset, reflecting all edits.
- [PHVideoRequestOptionsVersion.original](./phvideorequestoptionsversion/original.md)
  Request a version of the video asset without adjustments.
### Initializers
- [init?(rawValue: Int)](./phvideorequestoptionsversion/init%28rawvalue%29.md)

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
- [var deliveryMode: PHVideoRequestOptionsDeliveryMode](./phvideorequestoptions/deliverymode.md)
  A mode specifying the requested video quality and delivery priority.
- [enum PHVideoRequestOptionsDeliveryMode](./phvideorequestoptionsdeliverymode.md)
  Options for delivering requested video data, used by the [`deliveryMode`](./phvideorequestoptions/deliverymode.md) property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phvideorequestoptionsversion)*