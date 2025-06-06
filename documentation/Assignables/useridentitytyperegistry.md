# UserIdentityTypeRegistry

**Framework**: Assignables  
**Kind**: class

A registry for user identity types. Assignable documents and document elements store user identity data as `Data` objects. In order for that data to be deserialized, the type to deserialize it as needs to be known to [`UserIdentityTypeRegistry`](useridentitytyperegistry.md). Without registration of the user identity, custom types won’t be deserializable.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- visionOS ?+

## Declaration

```swift
class UserIdentityTypeRegistry
```

## Topics

### Registering an identity
- [static func registerUserIdentityType<UI>(typeID: String, type: UI.Type)](useridentitytyperegistry/registeruseridentitytype(typeid:type:).md)
  Registers a user identity type for use when deserializing the user identity from `Data`.

## See Also

- [protocol UserIdentity](useridentity.md)
  Types conforming to this protocol can act as user identities for editors of a document.
- [struct AnonymousUserIdentity](anonymoususeridentity.md)
  A user identity for unknown editors.
- [struct AnyUserIdentity](anyuseridentity.md)
  A user identity that performs type erasure by wrapping another user identity.
- [struct StringUserIdentity](stringuseridentity.md)
  A user identity defined by a string.
- [enum UserIdentityFactory](useridentityfactory.md)
  A type that contains helpers for creating user identity objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/assignables/useridentitytyperegistry)*