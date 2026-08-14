# SFAuthorization

**Framework**: Security Foundation  
**Kind**: class

A class that allows you to restrict a user’s access to particular features in your Mac app or daemon.

**Availability**:
- macOS 10.3+

## Declaration

```swift
class SFAuthorization
```

#### Overview

> ❗ **Important**: The authorization services API is not supported within an app sandbox because it allows privilege escalation.

The [`SFAuthorization`](sfauthorization.md) class is an interface for some of the functions in the Authorization Services API. You can use the [`authorizationRef()`](sfauthorization/authorizationref().md) method to obtain an authorization reference, used in other calls to Authorization Services functions. The Authorization Services API is documented in [`Authorization Services`](https://developer.apple.com/documentation/security/authorization-services).

## Topics

### Allocating and initializing an authorization object
- [class func authorization() -> Any!](sfauthorization/authorization.md)
  Returns an authorization object initialized with a default environment, flags, and rights.
- [class func authorization(with: AuthorizationFlags, rights: UnsafePointer<AuthorizationRights>!, environment: UnsafePointer<AuthorizationEnvironment>!) -> Any!](sfauthorization/authorization(with:rights:environment:).md)
  Returns an authorization object initialized with the specified flags, rights and environment.
- [init!()](sfauthorization/init.md)
  Initializes an authorization object with default environment, flags, and rights.
- [init!(flags: AuthorizationFlags, rights: UnsafePointer<AuthorizationRights>!, environment: UnsafePointer<AuthorizationEnvironment>!)](sfauthorization/init(flags:rights:environment:).md)
  Initializes an authorization object with the specified flags, rights, and environment.
### Obtaining an authorization reference
- [func authorizationRef() -> AuthorizationRef!](sfauthorization/authorizationref.md)
  Returns the authorization reference for this object.
### Authorizing rights
- [func obtain(withRights: UnsafePointer<AuthorizationRights>!, flags: AuthorizationFlags, environment: UnsafePointer<AuthorizationEnvironment>!, authorizedRights: UnsafeMutablePointer<UnsafeMutablePointer<AuthorizationRights>?>!) throws](sfauthorization/obtain(withrights:flags:environment:authorizedrights:).md)
  Authorizes and preauthorizes rights to access a privileged operation and returns the granted rights.
- [func obtain(withRight: AuthorizationString!, flags: AuthorizationFlags) throws](sfauthorization/obtain(withright:flags:).md)
  Authorizes and preauthorizes one specific right.
### Preventing credentials from being shared
- [func invalidateCredentials()](sfauthorization/invalidatecredentials.md)
  Prevents any rights that were obtained by this object from being preserved.
### Initializers
- [init?(coder: NSCoder)](sfauthorization/init(coder:).md)

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCoding](../foundation/nscoding.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [NSSecureCoding](../foundation/nssecurecoding.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/securityfoundation/sfauthorization)*