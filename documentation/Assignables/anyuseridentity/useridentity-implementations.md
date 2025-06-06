# UserIdentity Implementations

**Framework**: Assignables

## Topics

### Instance Methods
- [func eraseToAnyUserIdentity() -> AnyUserIdentity](anyuseridentity/erasetoanyuseridentity.md)
  Wraps this user identity with a type eraser.
- [func scope<R>(() async throws -> R) async rethrows -> R](anyuseridentity/scope(_:)-3xtwb.md)
  Sets the user identity for document-related operations that occur within the async closure passed in.
- [func scope<R>(() throws -> R) rethrows -> R](anyuseridentity/scope(_:)-6mjm1.md)
  Sets the user identity for document-related operations that occur within the closure passed in.
### Type Aliases
- [AnyUserIdentity.As](anyuseridentity/as.md)
  An alias for [`UserIdentityFactory`](useridentityfactory.md) for convenience.


---

*[View on Apple Developer](https://developer.apple.com/documentation/assignables/anyuseridentity/useridentity-implementations)*