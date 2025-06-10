# Handle.Kind

**Framework**: LiveCommunicationKit  
**Kind**: enum

Values that define the handle that identifies a participant in a conversation.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- visionOS 1.1+
- watchOS 10.4+

## Declaration

```swift
enum Kind
```

## Topics

### Types
- [Handle.Kind.emailAddress](handle/kind/emailaddress.md)
  An email address.
- [Handle.Kind.phoneNumber](handle/kind/phonenumber.md)
  A phone number.
- [Handle.Kind.generic](handle/kind/generic.md)
  An unspecified handle type.
### Initializers
- [init?(rawValue: Int)](handle/kind/init(rawvalue:).md)
  Creates a new instance with the specified raw value.
### Instance Properties
- [var rawValue: Int](handle/kind/rawvalue-swift.property.md)
  The corresponding value of the raw type.
### Type Aliases
- [Handle.Kind.RawValue](handle/kind/rawvalue-swift.typealias.md)
  The raw type that can be used to represent all values of the conforming type.
### Default Implementations
- [Equatable Implementations](handle/kind/equatable-implementations.md)
- [RawRepresentable Implementations](handle/kind/rawrepresentable-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var type: Handle.Kind](handle/type.md)
  The type of the handle; for example a phone number or email address.


---

*[View on Apple Developer](https://developer.apple.com/documentation/livecommunicationkit/handle/kind)*