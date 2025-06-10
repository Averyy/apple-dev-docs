# AnonymousUserIdentity

**Framework**: Assignables  
**Kind**: struct

A user identity for unknown editors.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- visionOS ?+

## Declaration

```swift
struct AnonymousUserIdentity
```

## Topics

### Creating an anonymous identity
- [init()](anonymoususeridentity/init.md)
  Initializes an instance of `AnonymousUserIdentity`.
- [init(from: any Decoder) throws](anonymoususeridentity/init(from:).md)
  Creates a new instance by decoding from the given decoder.
### Inspecting an identity
- [var stringRepresentation: String](anonymoususeridentity/stringrepresentation.md)
  String representation of this user identity for display or debugging purposes.
- [var typeID: String](anonymoususeridentity/typeid-swift.property.md)
  A unique type identifier for this user identity.
- [static var typeID: String](anonymoususeridentity/typeid-swift.type.property.md)
  A unique type identifier for this user identity.
### Operators
- [static func == (AnonymousUserIdentity, AnonymousUserIdentity) -> Bool](anonymoususeridentity/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Instance Properties
- [var hashValue: Int](anonymoususeridentity/hashvalue.md)
  The hash value.
### Instance Methods
- [func encode(to: any Encoder) throws](anonymoususeridentity/encode(to:).md)
  Encodes this value into the given encoder.
- [func hash(into: inout Hasher)](anonymoususeridentity/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Default Implementations
- [Equatable Implementations](anonymoususeridentity/equatable-implementations.md)
- [UserIdentity Implementations](anonymoususeridentity/useridentity-implementations.md)

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [UserIdentity](useridentity.md)

## See Also

- [protocol UserIdentity](useridentity.md)
  Types conforming to this protocol can act as user identities for editors of a document.
- [struct AnyUserIdentity](anyuseridentity.md)
  A user identity that performs type erasure by wrapping another user identity.
- [struct StringUserIdentity](stringuseridentity.md)
  A user identity defined by a string.
- [class UserIdentityTypeRegistry](useridentitytyperegistry.md)
  A registry for user identity types. Assignable documents and document elements store user identity data as `Data` objects. In order for that data to be deserialized, the type to deserialize it as needs to be known to [`UserIdentityTypeRegistry`](useridentitytyperegistry.md). Without registration of the user identity, custom types won’t be deserializable.
- [enum UserIdentityFactory](useridentityfactory.md)
  A type that contains helpers for creating user identity objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/assignables/anonymoususeridentity)*