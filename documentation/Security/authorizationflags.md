# AuthorizationFlags

**Framework**: Security  
**Kind**: struct  
**Role**: Structure

The flags used to specify authorization options.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
struct AuthorizationFlags
```

```c
enum AuthorizationFlags : UInt32;
```

#### Overview

These flags instruct the Security Server how to proceed with the function in which you pass them. You bitwise `OR` them together to specify more than one at a time. Set all unused bits to `0` to allow for future expansion.

Use these flags in calls to the [`AuthorizationCreate(_:_:_:_:)`](./authorizationcreate%28_,_,_,_%29.md), [`AuthorizationFree(_:_:)`](./authorizationfree%28_,_%29.md), [`AuthorizationCopyRights(_:_:_:_:_:)`](./authorizationcopyrights%28_,_,_,_,_%29.md), and [`AuthorizationCopyRightsAsync(_:_:_:_:_:)`](./authorizationcopyrightsasync%28_,_,_,_,_%29.md) functions.

## Topics

### Initializers
- [init(rawValue: UInt32)](./authorizationflags/init%28rawvalue%29.md)
  Initializes an authorization flags structure.
### Type Properties
- [static var interactionAllowed: AuthorizationFlags](./authorizationflags/interactionallowed.md)
  A flag that permits user interaction as needed.
- [static var extendRights: AuthorizationFlags](./authorizationflags/extendrights.md)
  A flag that permits the Security Server to attempt to grant the rights requested.
- [static var partialRights: AuthorizationFlags](./authorizationflags/partialrights.md)
  A flag that permits the Security Server to grant rights on an individual basis.
- [static var destroyRights: AuthorizationFlags](./authorizationflags/destroyrights.md)
  A flag that instructs the Security Server to revoke authorization.
- [static var preAuthorize: AuthorizationFlags](./authorizationflags/preauthorize.md)
  A flag that instructs the Security Server to preauthorize the rights requested.
- [static var noData: AuthorizationFlags](./authorizationflags/nodata.md)
  Private flag. Do not use.
- [static var skipInternalAuth: AuthorizationFlags](./authorizationflags/skipinternalauth.md)
- [kAuthorizationFlagDefaults](./authorizationflags/kauthorizationflagdefaults.md)
  An empty flag set that you use as a placeholder when you don’t want any of the other flags.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../Swift/optionset.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [SetAlgebra](../Swift/setalgebra.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/authorizationflags)*