# AnyUserIdentity.Error

**Framework**: Assignables  
**Kind**: enum

Error type for this user identity.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- visionOS ?+

## Declaration

```swift
enum Error
```

## Topics

### Decode error
- [AnyUserIdentity.Error.cannotDecode](anyuseridentity/error/cannotdecode.md)
  Unable to decode the user identity.
### Operators
- [static func == (AnyUserIdentity.Error, AnyUserIdentity.Error) -> Bool](anyuseridentity/error/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Instance Properties
- [var hashValue: Int](anyuseridentity/error/hashvalue.md)
  The hash value.
### Instance Methods
- [func hash(into: inout Hasher)](anyuseridentity/error/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Default Implementations
- [Equatable Implementations](anyuseridentity/error/equatable-implementations.md)
- [Error Implementations](anyuseridentity/error/error-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Error](../Swift/Error.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var stringRepresentation: String](anyuseridentity/stringrepresentation.md)
  String representation of this user identity for display or debugging purposes.
- [var typeID: String](anyuseridentity/typeid.md)
  A unique type identifier for this user identity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/assignables/anyuseridentity/error)*