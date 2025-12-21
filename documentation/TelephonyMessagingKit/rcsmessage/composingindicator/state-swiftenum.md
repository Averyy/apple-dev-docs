# RCSMessage.ComposingIndicator.State

**Framework**: TelephonyMessagingKit  
**Kind**: enum

An enumeration that represents the state of the indicator.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+

## Declaration

```swift
enum State
```

## Topics

### Working with composing indicator states
- [RCSMessage.ComposingIndicator.State.active](rcsmessage/composingindicator/state-swift.enum/active.md)
  The client is composing a message.
- [RCSMessage.ComposingIndicator.State.idle](rcsmessage/composingindicator/state-swift.enum/idle.md)
  The client is idle.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var state: RCSMessage.ComposingIndicator.State](rcsmessage/composingindicator/state-swift.property.md)
  The state of the composer.
- [var lastActive: Date?](rcsmessage/composingindicator/lastactive.md)
  The time of last activity.
- [var contentType: UTType?](rcsmessage/composingindicator/contenttype.md)
  The type of message being composed.
- [struct UTType](../UniformTypeIdentifiers/UTType-swift.struct.md)
  A structure that represents a type of data to load, send, or receive.
- [var refreshInterval: Duration?](rcsmessage/composingindicator/refreshinterval.md)
  The time interval after which the receiver can expect an update from the composer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/rcsmessage/composingindicator/state-swift.enum)*