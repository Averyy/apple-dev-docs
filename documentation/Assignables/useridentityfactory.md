# UserIdentityFactory

**Framework**: Assignables  
**Kind**: enum

A type that contains helpers for creating user identity objects.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- visionOS ?+

## Declaration

```swift
enum UserIdentityFactory
```

## Topics

### Getting the anonymous identity
- [static var anonymous: AnonymousUserIdentity](useridentityfactory/anonymous.md)
  The anonymous user identity.
### Creating an identity
- [static func string(String) -> StringUserIdentity](useridentityfactory/string(_:).md)
  Creates a [`StringUserIdentity`](stringuseridentity.md) with the given string value.

## See Also

- [protocol UserIdentity](useridentity.md)
  Types conforming to this protocol can act as user identities for editors of a document.
- [struct AnonymousUserIdentity](anonymoususeridentity.md)
  A user identity for unknown editors.
- [struct AnyUserIdentity](anyuseridentity.md)
  A user identity that performs type erasure by wrapping another user identity.
- [struct StringUserIdentity](stringuseridentity.md)
  A user identity defined by a string.
- [class UserIdentityTypeRegistry](useridentitytyperegistry.md)
  A registry for user identity types. Assignable documents and document elements store user identity data as `Data` objects. In order for that data to be deserialized, the type to deserialize it as needs to be known to [`UserIdentityTypeRegistry`](useridentitytyperegistry.md). Without registration of the user identity, custom types won’t be deserializable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/assignables/useridentityfactory)*