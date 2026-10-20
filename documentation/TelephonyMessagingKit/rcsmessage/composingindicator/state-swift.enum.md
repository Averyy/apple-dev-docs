# RCSMessage.ComposingIndicator.State

**Framework**: TelephonyMessagingKit  
**Kind**: enum  
**Role**: Enumeration

An enumeration that represents the state of the indicator.

**Availability**:
- iOS 26.0+

## Declaration

```swift
enum State
```

## Topics

### Working with composing indicator states
- [RCSMessage.ComposingIndicator.State.active](./state-swift.enum/active.md)
  The client is composing a message.
- [RCSMessage.ComposingIndicator.State.idle](./state-swift.enum/idle.md)
  The client is idle.

## Relationships

### Conforms To
- [Decodable](../../../Swift/decodable.md)
- [Encodable](../../../Swift/encodable.md)
- [Equatable](../../../Swift/equatable.md)
- [Hashable](../../../Swift/hashable.md)
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)

## See Also

### Accessing composing indicator properties
- [var state: RCSMessage.ComposingIndicator.State](./state-swift.property.md)
  The state of the composer.
- [var lastActive: Date?](./lastactive.md)
  The time of last activity.
- [var contentType: UTType?](./contenttype.md)
  The type of message being composed.
- [struct UTType](../../../UniformTypeIdentifiers/uttype-swift.struct.md)
  A structure that represents a type of data to load, send, or receive.
- [var refreshInterval: Duration?](./refreshinterval.md)
  The time interval after which the receiver can expect an update from the composer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/rcsmessage/composingindicator/state-swift.enum)*