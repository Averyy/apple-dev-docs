# UserIdentity Implementations

**Framework**: Assignables

## Topics

### Instance Methods
- [func eraseToAnyUserIdentity() -> AnyUserIdentity](stringuseridentity/erasetoanyuseridentity.md)
  Wraps this user identity with a type eraser.
- [func scope<R>(() async throws -> R) async rethrows -> R](stringuseridentity/scope(_:)-935zx.md)
  Sets the user identity for document-related operations that occur within the async closure passed in.
- [func scope<R>(() throws -> R) rethrows -> R](stringuseridentity/scope(_:)-93wrt.md)
  Sets the user identity for document-related operations that occur within the closure passed in.
### Type Aliases
- [StringUserIdentity.As](stringuseridentity/as.md)
  An alias for [`UserIdentityFactory`](useridentityfactory.md) for convenience.


---

*[View on Apple Developer](https://developer.apple.com/documentation/assignables/stringuseridentity/useridentity-implementations)*