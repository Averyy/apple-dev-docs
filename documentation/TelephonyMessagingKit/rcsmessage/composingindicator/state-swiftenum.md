# RCSMessage.ComposingIndicator.State

**Framework**: TelephonyMessagingKit  
**Kind**: enum

An enumeration that represents the state of the indicator.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
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
### Encoding and decoding
- [init(from: any Decoder) throws](rcsmessage/composingindicator/state-swift.enum/init(from:).md)
  Creates a new instance by decoding from the given decoder.
### Operators
- [static func == (RCSMessage.ComposingIndicator.State, RCSMessage.ComposingIndicator.State) -> Bool](rcsmessage/composingindicator/state-swift.enum/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Instance Properties
- [var hashValue: Int](rcsmessage/composingindicator/state-swift.enum/hashvalue.md)
  The hash value.
### Instance Methods
- [func encode(to: any Encoder) throws](rcsmessage/composingindicator/state-swift.enum/encode(to:).md)
  Encodes this value into the given encoder.
- [func hash(into: inout Hasher)](rcsmessage/composingindicator/state-swift.enum/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Default Implementations
- [Equatable Implementations](rcsmessage/composingindicator/state-swift.enum/equatable-implementations.md)

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

- [let state: RCSMessage.ComposingIndicator.State](rcsmessage/composingindicator/state-swift.property.md)
  The state of the composer.
- [let lastActive: Date?](rcsmessage/composingindicator/lastactive.md)
  The time of last activity.
- [let contentType: UTType?](rcsmessage/composingindicator/contenttype.md)
  The type of message being composed.
- [struct UTType](../UniformTypeIdentifiers/UTType-swift.struct.md)
  A structure that represents a type of data to load, send, or receive.
- [let refreshInterval: Duration?](rcsmessage/composingindicator/refreshinterval.md)
  The time interval after which the receiver can expect an update from the composer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/rcsmessage/composingindicator/state-swift.enum)*