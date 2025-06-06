# AuthorizationFlags

**Framework**: Security  
**Kind**: struct

The flags used to specify authorization options.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
struct AuthorizationFlags
```

#### Overview

These flags instruct the Security Server how to proceed with the function in which you pass them. You bitwise `OR` them together to specify more than one at a time. Set all unused bits to `0` to allow for future expansion.

Use these flags in calls to the [`AuthorizationCreate(_:_:_:_:)`](authorizationcreate(_:_:_:_:).md), [`AuthorizationFree(_:_:)`](authorizationfree(_:_:).md), [`AuthorizationCopyRights(_:_:_:_:_:)`](authorizationcopyrights(_:_:_:_:_:).md), and [`AuthorizationCopyRightsAsync(_:_:_:_:_:)`](authorizationcopyrightsasync(_:_:_:_:_:).md) functions.

## Topics

### Initializers
- [init(rawValue: UInt32)](authorizationflags/init(rawvalue:).md)
  Initializes an authorization flags structure.
### Type Properties
- [static var interactionAllowed: AuthorizationFlags](authorizationflags/interactionallowed.md)
  A flag that permits user interaction as needed.
- [static var extendRights: AuthorizationFlags](authorizationflags/extendrights.md)
  A flag that permits the Security Server to attempt to grant the rights requested.
- [static var partialRights: AuthorizationFlags](authorizationflags/partialrights.md)
  A flag that permits the Security Server to grant rights on an individual basis.
- [static var destroyRights: AuthorizationFlags](authorizationflags/destroyrights.md)
  A flag that instructs the Security Server to revoke authorization.
- [static var preAuthorize: AuthorizationFlags](authorizationflags/preauthorize.md)
  A flag that instructs the Security Server to preauthorize the rights requested.
- [static var noData: AuthorizationFlags](authorizationflags/nodata.md)
  Private flag. Do not use.
- [static var skipInternalAuth: AuthorizationFlags](authorizationflags/skipinternalauth.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SetAlgebra](../Swift/SetAlgebra.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/authorizationflags)*