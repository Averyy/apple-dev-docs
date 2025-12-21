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
### Inspecting an identity
- [var stringRepresentation: String](anonymoususeridentity/stringrepresentation.md)
  String representation of this user identity for display or debugging purposes.
- [var typeID: String](anonymoususeridentity/typeid-swift.property.md)
  A unique type identifier for this user identity.
- [static var typeID: String](anonymoususeridentity/typeid-swift.type.property.md)
  A unique type identifier for this user identity.

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