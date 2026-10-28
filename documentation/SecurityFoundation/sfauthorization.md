# SFAuthorization

**Framework**: Security Foundation  
**Kind**: class  
**Role**: Class

A class that allows you to restrict a user’s access to particular features in your Mac app or daemon.

**Availability**:
- macOS 10.3+

## Declaration

```swift
class SFAuthorization
```

```objc
@interface SFAuthorization : NSObject
```

## Overview

> ❗ **Important**: The authorization services API is not supported within an app sandbox because it allows privilege escalation.

The [`SFAuthorization`](./sfauthorization.md) class is an interface for some of the functions in the Authorization Services API. You can use the [`authorizationRef()`](./sfauthorization/authorizationref%28%29.md) method to obtain an authorization reference, used in other calls to Authorization Services functions. The Authorization Services API is documented in [Authorization Services](../Security/authorization-services.md).

## Topics

### Allocating and initializing an authorization object
- [class func authorization() -> Any!](./sfauthorization/authorization%28%29.md)
  Returns an authorization object initialized with a default environment, flags, and rights.
- [class func authorization(with: AuthorizationFlags, rights: UnsafePointer<AuthorizationRights>!, environment: UnsafePointer<AuthorizationEnvironment>!) -> Any!](./sfauthorization/authorization%28with,rights,environment%29.md)
  Returns an authorization object initialized with the specified flags, rights and environment.
- [init!()](./sfauthorization/init%28%29.md)
  Initializes an authorization object with default environment, flags, and rights.
- [init!(flags: AuthorizationFlags, rights: UnsafePointer<AuthorizationRights>!, environment: UnsafePointer<AuthorizationEnvironment>!)](./sfauthorization/init%28flags,rights,environment%29.md)
  Initializes an authorization object with the specified flags, rights, and environment.
### Obtaining an authorization reference
- [func authorizationRef() -> AuthorizationRef!](./sfauthorization/authorizationref%28%29.md)
  Returns the authorization reference for this object.
### Authorizing rights
- [func obtain(withRights: UnsafePointer<AuthorizationRights>!, flags: AuthorizationFlags, environment: UnsafePointer<AuthorizationEnvironment>!, authorizedRights: UnsafeMutablePointer<UnsafeMutablePointer<AuthorizationRights>?>!) throws](./sfauthorization/obtain%28withrights,flags,environment,authorizedrights%29.md)
  Authorizes and preauthorizes rights to access a privileged operation and returns the granted rights.
- [func obtain(withRight: AuthorizationString!, flags: AuthorizationFlags) throws](./sfauthorization/obtain%28withright,flags%29.md)
  Authorizes and preauthorizes one specific right.
- [- permitWithRights:flags:environment:authorizedRights:](./sfauthorization/permitwithrights_flags_environment_authorizedrights_.md)
  Authorizes and preauthorizes rights to access a privileged operation and returns the granted rights.
- [- permitWithRight:flags:](./sfauthorization/permitwithright_flags_.md)
  Authorizes and preauthorizes one specific right.
### Preventing credentials from being shared
- [func invalidateCredentials()](./sfauthorization/invalidatecredentials%28%29.md)
  Prevents any rights that were obtained by this object from being preserved.
### Initializers
- [init?(coder: NSCoder)](./sfauthorization/init%28coder%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/securityfoundation/sfauthorization)*