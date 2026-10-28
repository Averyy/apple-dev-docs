# authorization(with:rights:environment:)

**Framework**: Security Foundation  
**Kind**: method  
**Role**: Type Method

Returns an authorization object initialized with the specified flags, rights and environment.

**Availability**:
- macOS 10.10+

## Declaration

```swift
class func authorization(with flags: AuthorizationFlags, rights: UnsafePointer<AuthorizationRights>!, environment: UnsafePointer<AuthorizationEnvironment>!) -> Any!
```

```objc
+ (id) authorizationWithFlags:(AuthorizationFlags) flags rights:(const AuthorizationRights *) rights environment:(const AuthorizationEnvironment *) environment;
```

## Return value

The authorization object.

## Discussion

Normally, such initialization is not required, as you pass in flags, rights, and environmental data when you request authorization.

## Parameters

- `flags`: A bit mask for specifying authorization options. Use the following option sets:

  - Pass the constant [`kAuthorizationFlagDefaults`](../../Security/authorizationflags/kauthorizationflagdefaults.md) if no options are necessary.
  - Specify the [`extendRights`](../../Security/authorizationflags/extendrights.md) mask to request rights. You can also specify the [`interactionAllowed`](../../Security/authorizationflags/interactionallowed.md) mask to allow user interaction.
  - Specify the [`partialRights`](../../Security/authorizationflags/partialrights.md) and [`extendRights`](../../Security/authorizationflags/extendrights.md) masks to request partial rights. You can also specify the [`interactionAllowed`](../../Security/authorizationflags/interactionallowed.md) mask to allow user interaction.
  - Specify the [`preAuthorize`](../../Security/authorizationflags/preauthorize.md) and [`extendRights`](../../Security/authorizationflags/extendrights.md) masks to preauthorize rights.
  - Specify the [`destroyRights`](../../Security/authorizationflags/destroyrights.md) mask to prevent the Security framework from preserving the rights obtained during this call.
- `rights`: A pointer to a set of authorization rights you create. Pass `NULL` if the application requires no rights at this time.
- `environment`: Data used when authorizing or preauthorizing rights. In macOS 10.3 and later, you can pass icon or prompt data to be used in the authentication dialog box. Possible values for this parameter are listed in `Security.framework/Headers/AuthorizationTags.h`. The data passed in this parameter is not stored in the authorization reference; it is used only during authorization. If you are not passing any data in this parameter, pass the constant [`kAuthorizationEmptyEnvironment`](../../Security/kauthorizationemptyenvironment.md).

## See Also

### Allocating and initializing an authorization object
- [class func authorization() -> Any!](./authorization%28%29.md)
  Returns an authorization object initialized with a default environment, flags, and rights.
- [init!()](./init%28%29.md)
  Initializes an authorization object with default environment, flags, and rights.
- [init!(flags: AuthorizationFlags, rights: UnsafePointer<AuthorizationRights>!, environment: UnsafePointer<AuthorizationEnvironment>!)](./init%28flags,rights,environment%29.md)
  Initializes an authorization object with the specified flags, rights, and environment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/securityfoundation/sfauthorization/authorization(with:rights:environment:))*