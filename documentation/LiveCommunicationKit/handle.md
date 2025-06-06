# Handle

**Framework**: LiveCommunicationKit  
**Kind**: struct

Uniquely identifies a member in a `Conversation`.

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

## Topics

### Operators
- [static func == (Handle, Handle) -> Bool](handle/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Initializers
- [init(from: any Decoder) throws](handle/init(from:).md)
  Creates a new instance by decoding from the given decoder.
- [init(type: Handle.Kind, value: String, displayName: String?)](handle/init(type:value:displayname:).md)
  Creates a new `Handle`.
### Instance Properties
- [var displayName: String](handle/displayname.md)
  The value that should be displayed to the user at the UI layer.
- [var hashValue: Int](handle/hashvalue.md)
  The hash value.
- [var type: Handle.Kind](handle/type.md)
  The type of handle (e.g. a phone number or email address)
- [var value: String](handle/value.md)
  The raw value of the handle.
### Instance Methods
- [func encode(to: any Encoder) throws](handle/encode(to:).md)
  Encodes this value into the given encoder.
- [func hash(into: inout Hasher)](handle/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Enumerations
- [Handle.Kind](handle/kind.md)
  The type of the handle.
### Default Implementations
- [Equatable Implementations](handle/equatable-implementations.md)

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/livecommunicationkit/handle)*