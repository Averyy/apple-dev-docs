# UserIdentity

**Framework**: Assignables  
**Kind**: protocol

Types conforming to this protocol can act as user identities for editors of a document.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- visionOS ?+

## Declaration

```swift
protocol UserIdentity : Decodable, Encodable, Hashable, Sendable
```

## Topics

### Inspecting an identity
- [var stringRepresentation: String](useridentity/stringrepresentation.md)
  String representation of this user identity for display or debugging purposes.
- [var typeID: String](useridentity/typeid.md)
  A unique type identifier for this user identity.
### Setting the scope
- [func scope<R>(() throws -> R) rethrows -> R](useridentity/scope(_:)-esta.md)
  Sets the user identity for document-related operations that occur within the closure passed in.
- [func scope<R>(() async throws -> R) async rethrows -> R](useridentity/scope(_:)-j2jq.md)
  Sets the user identity for document-related operations that occur within the async closure passed in.
### Getting a type eraser
- [func eraseToAnyUserIdentity() -> AnyUserIdentity](useridentity/erasetoanyuseridentity.md)
  Wraps this user identity with a type eraser.
- [UserIdentity.As](useridentity/as.md)
  An alias for [`UserIdentityFactory`](useridentityfactory.md) for convenience.

## Relationships

### Inherits From
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
### Conforming Types
- [AnonymousUserIdentity](anonymoususeridentity.md)
- [AnyUserIdentity](anyuseridentity.md)
- [StringUserIdentity](stringuseridentity.md)

## See Also

- [struct AnonymousUserIdentity](anonymoususeridentity.md)
  A user identity for unknown editors.
- [struct AnyUserIdentity](anyuseridentity.md)
  A user identity that performs type erasure by wrapping another user identity.
- [struct StringUserIdentity](stringuseridentity.md)
  A user identity defined by a string.
- [class UserIdentityTypeRegistry](useridentitytyperegistry.md)
  A registry for user identity types. Assignable documents and document elements store user identity data as `Data` objects. In order for that data to be deserialized, the type to deserialize it as needs to be known to [`UserIdentityTypeRegistry`](useridentitytyperegistry.md). Without registration of the user identity, custom types won’t be deserializable.
- [enum UserIdentityFactory](useridentityfactory.md)
  A type that contains helpers for creating user identity objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/assignables/useridentity)*