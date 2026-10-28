# permitWithRight:flags:

**Framework**: Security Foundation  
**Kind**: method  
**Role**: Instance Method

Authorizes and preauthorizes one specific right.

**Availability**:
- macOS 10.0+ - Deprecated in 10.5

> **Deprecated**: Use [`obtain(withRight:flags:)`](./obtain%28withright,flags%29.md) instead.

## Declaration

```objc
- (OSStatus) permitWithRight:(AuthorizationString) rightName flags:(AuthorizationFlags) flags;
```

## Discussion

Use this method to authorize or preauthorize a single right.

## Parameters

- `rightName`: The name of an authorization right.
- `flags`: A bit mask for specifying authorization options. See [`permitWithRights:flags:environment:authorizedRights:`](./permitwithrights_flags_environment_authorizedrights_.md) for details about possible flag values.

## See Also

### Authorizing rights
- [- permitWithRights:flags:environment:authorizedRights:](./permitwithrights_flags_environment_authorizedrights_.md)
  Authorizes and preauthorizes rights to access a privileged operation and returns the granted rights.
- [func obtain(withRights: UnsafePointer<AuthorizationRights>!, flags: AuthorizationFlags, environment: UnsafePointer<AuthorizationEnvironment>!, authorizedRights: UnsafeMutablePointer<UnsafeMutablePointer<AuthorizationRights>?>!) throws](./obtain%28withrights,flags,environment,authorizedrights%29.md)
  Authorizes and preauthorizes rights to access a privileged operation and returns the granted rights.
- [func obtain(withRight: AuthorizationString!, flags: AuthorizationFlags) throws](./obtain%28withright,flags%29.md)
  Authorizes and preauthorizes one specific right.


---

*[View on Apple Developer](https://developer.apple.com/documentation/securityfoundation/sfauthorization/permitwithright:flags:)*