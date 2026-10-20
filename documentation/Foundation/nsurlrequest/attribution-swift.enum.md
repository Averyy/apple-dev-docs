# NSURLRequest.Attribution

**Framework**: Foundation  
**Kind**: enum  
**Role**: Enumeration

The entities that can make a network request.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
enum Attribution
```

```c
enum NSURLRequestAttribution : NSUInteger;
```

#### Overview

Use one of these values when setting the [`attribution`](../urlrequest/attribution-swift.property.md) parameter of a [`URLRequest`](../urlrequest.md). If you don’t set a value, the system assumes [`NSURLRequest.Attribution.developer`](./attribution-swift.enum/developer.md).

## Topics

### Request sources
- [NSURLRequest.Attribution.developer](./attribution-swift.enum/developer.md)
  A developer-initiated network request.
- [NSURLRequest.Attribution.user](./attribution-swift.enum/user.md)
  The user explicitly directs the app to make a network request.
### Initializers
- [init?(rawValue: UInt)](./attribution-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Indicating the source of the request
- [var attribution: NSURLRequest.Attribution](../nsmutableurlrequest/attribution.md)
  The entity that initiates the network request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsurlrequest/attribution-swift.enum)*