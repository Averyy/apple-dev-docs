# AnyUserIdentity

**Framework**: Assignables  
**Kind**: struct

A user identity that performs type erasure by wrapping another user identity.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- visionOS ?+

## Declaration

```swift
struct AnyUserIdentity
```

## Topics

### Creating a user identity
- [init<T>(T)](anyuseridentity/init(_:).md)
  Initializes this type eraser with a user identity to wrap.
- [init(from: any Decoder) throws](anyuseridentity/init(from:).md)
  Creates a new instance by decoding from the given decoder.
### Setting the scope
- [func scope<R>(() throws -> R) rethrows -> R](anyuseridentity/scope(_:)-1wfwz.md)
  Sets the user identity for document-related operations that occur within the closure passed in.
- [func scope<R>(() async throws -> R) async rethrows -> R](anyuseridentity/scope(_:)-76dnq.md)
  Sets the user identity for document-related operations that occur within the async closure passed in.
### Inspecting an identity
- [var stringRepresentation: String](anyuseridentity/stringrepresentation.md)
  String representation of this user identity for display or debugging purposes.
- [var typeID: String](anyuseridentity/typeid.md)
  A unique type identifier for this user identity.
- [AnyUserIdentity.Error](anyuseridentity/error.md)
  Error type for this user identity.
### Instance Methods
- [func encode(to: any Encoder) throws](anyuseridentity/encode(to:).md)
  Encodes this value into the given encoder.
- [func hash(into: inout Hasher)](anyuseridentity/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Comparing identities
- [static func == (AnyUserIdentity, AnyUserIdentity) -> Bool](anyuseridentity/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Instance Properties
- [var hashValue: Int](anyuseridentity/hashvalue.md)
  The hash value.
### Default Implementations
- [Equatable Implementations](anyuseridentity/equatable-implementations.md)
- [UserIdentity Implementations](anyuseridentity/useridentity-implementations.md)

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [UserIdentity](useridentity.md)

## See Also

- [protocol UserIdentity](useridentity.md)
  Types conforming to this protocol can act as user identities for editors of a document.
- [struct AnonymousUserIdentity](anonymoususeridentity.md)
  A user identity for unknown editors.
- [struct StringUserIdentity](stringuseridentity.md)
  A user identity defined by a string.
- [class UserIdentityTypeRegistry](useridentitytyperegistry.md)
  A registry for user identity types. Assignable documents and document elements store user identity data as `Data` objects. In order for that data to be deserialized, the type to deserialize it as needs to be known to [`UserIdentityTypeRegistry`](useridentitytyperegistry.md). Without registration of the user identity, custom types won’t be deserializable.
- [enum UserIdentityFactory](useridentityfactory.md)
  A type that contains helpers for creating user identity objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/assignables/anyuseridentity)*