# RCSMessage.ComposingIndicator.State

**Framework**: TelephonyMessagingKit  
**Kind**: enum

An enumeration that represents the state of the indicator.

**Availability**:
- iOS 26.0+

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
- [Decodable](../swift/decodable.md)
- [Encodable](../swift/encodable.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [var state: RCSMessage.ComposingIndicator.State](rcsmessage/composingindicator/state-swift.property.md)
  The state of the composer.
- [var lastActive: Date?](rcsmessage/composingindicator/lastactive.md)
  The time of last activity.
- [var contentType: UTType?](rcsmessage/composingindicator/contenttype.md)
  The type of message being composed.
- [struct UTType](../uniformtypeidentifiers/uttype-swift.struct.md)
  A structure that represents a type of data to load, send, or receive.
- [var refreshInterval: Duration?](rcsmessage/composingindicator/refreshinterval.md)
  The time interval after which the receiver can expect an update from the composer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/rcsmessage/composingindicator/state-swift.enum)*