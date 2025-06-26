# Handle

**Framework**: LiveCommunicationKit  
**Kind**: struct

A way to reach a participant, such as a phone number or email address.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- visionOS 1.1+
- watchOS 10.4+

## Declaration

```swift
struct Handle
```

## Mentions

- [Preparing your app to be the default dialer app](preparing-your-app-to-be-the-default-dialer-app.md)

## Topics

### Creation
- [init(type: Handle.Kind, value: String, displayName: String?)](handle/init(type:value:displayname:).md)
  Creates a new handle that identifies a participant in a conversation.
- [init(from: any Decoder) throws](handle/init(from:).md)
  Creates a new instance by decoding from the given decoder.
### Type
- [var type: Handle.Kind](handle/type.md)
  The type of the handle; for example a phone number or email address.
- [Handle.Kind](handle/kind.md)
  Values that define the handle that identifies a participant in a conversation.
### Attributes
- [var displayName: String](handle/displayname.md)
  The name for a participant in a conversation that appears in the conversation UI.
- [var value: String](handle/value.md)
  The raw value of the handle.
### Operators
- [static func == (Handle, Handle) -> Bool](handle/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Instance Properties
- [var hashValue: Int](handle/hashvalue.md)
  The hash value.
### Instance Methods
- [func encode(to: any Encoder) throws](handle/encode(to:).md)
  Encodes this value into the given encoder.
- [func hash(into: inout Hasher)](handle/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Default Implementations
- [Equatable Implementations](handle/equatable-implementations.md)

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/livecommunicationkit/handle)*