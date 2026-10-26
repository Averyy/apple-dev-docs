# permitWithRights:flags:environment:authorizedRights:

**Framework**: Security Foundation  
**Kind**: method  
**Role**: Instance Method

Authorizes and preauthorizes rights to access a privileged operation and returns the granted rights.

**Availability**:
- macOS 10.0+ - Deprecated in 10.5

> **Deprecated**: Use [`obtain(withRights:flags:environment:authorizedRights:)`](./obtain%28withrights,flags,environment,authorizedrights%29.md) instead.

## Declaration

```objc
- (OSStatus) permitWithRights:(const AuthorizationRights *) rights flags:(AuthorizationFlags) flags environment:(const AuthorizationEnvironment *) environment authorizedRights:(AuthorizationRights *) authorizedRights;
```

#### Discussion

There are three main reasons to use this method. The first reason is to preauthorize rights by specifying the [`preAuthorize`](../../Security/authorizationflags/preauthorize.md), [`interactionAllowed`](../../Security/authorizationflags/interactionallowed.md), and [`extendRights`](../../Security/authorizationflags/extendrights.md) masks as authorization options. Preauthorization is most useful when a right has a zero timeout. For example, you can preauthorize in the application and if it succeeds, call the helper tool and request authorization. This eliminates calling the helper tool if the Security framework cannot later authorize the specified rights.

The second reason to use this method is to authorize rights before performing a privileged operation by specifying the [`interactionAllowed`](../../Security/authorizationflags/interactionallowed.md), and [`extendRights`](../../Security/authorizationflags/extendrights.md) masks as authorization options.

The third reason to use this method is to authorize partial rights. By specifying the [`partialRights`](../../Security/authorizationflags/partialrights.md), [`interactionAllowed`](../../Security/authorizationflags/interactionallowed.md), and [`extendRights`](../../Security/authorizationflags/extendrights.md) masks as authorization options, the Security framework grants all rights it can authorize. On return, the authorized set contains all the rights.

If you do not specify the [`partialRights`](../../Security/authorizationflags/partialrights.md) mask and the Security framework denies at least one right, then the status of this method on return is [`errAuthorizationDenied`](../../Security/errauthorizationdenied.md).

If you do not specify the [`interactionAllowed`](../../Security/authorizationflags/interactionallowed.md) mask and the Security framework requires user interaction, then the status of this method on return is [`errAuthorizationInteractionNotAllowed`](../../Security/errauthorizationinteractionnotallowed.md).

If you specify the [`interactionAllowed`](../../Security/authorizationflags/interactionallowed.md) mask and the user cancels the authentication process, then the status of this method on return is [`errAuthorizationCanceled`](../../Security/errauthorizationcanceled.md).

##### Special considerations

The `authorizedRights` parameter is not supported in OS X v10.3; use the Authorization Services function `AuthorizationCopyRights` instead. In OS X v10.3 there is an error in the signature in the header file for this parameter. If you pass this argument as (AuthorizationRights **)`authorizedRights`, as shown in this document, it works as described.

## Parameters

- `rights`: A pointer to a set of authorization rights you create. Pass `NULL` if the application requires no rights at this time.
- `flags`: A bit mask for specifying authorization options. Use the following option sets:

  - Pass the constant [`kAuthorizationFlagDefaults`](../../Security/authorizationflags/kauthorizationflagdefaults.md) if no options are necessary.
  - Specify the [`extendRights`](../../Security/authorizationflags/extendrights.md) mask to request rights. You can also specify the [`interactionAllowed`](../../Security/authorizationflags/interactionallowed.md) mask to allow user interaction.
  - Specify the [`partialRights`](../../Security/authorizationflags/partialrights.md) and [`extendRights`](../../Security/authorizationflags/extendrights.md) masks to request partial rights. You can also specify the [`interactionAllowed`](../../Security/authorizationflags/interactionallowed.md) mask to allow user interaction.
  - Specify the [`preAuthorize`](../../Security/authorizationflags/preauthorize.md) and [`extendRights`](../../Security/authorizationflags/extendrights.md) masks to preauthorize rights.
  - Specify the [`destroyRights`](../../Security/authorizationflags/destroyrights.md) mask to prevent the Security framework from preserving the rights obtained during this call.
- `environment`: Data used when authorizing or preauthorizing rights. In macOS 10.3 and later, you can pass icon or prompt data to be used in the authentication dialog box. Possible values for this parameter are listed in `Security/AuthorizationTags.h`. If you are not passing any data in this parameter, pass the constant [`kAuthorizationEmptyEnvironment`](../../Security/kauthorizationemptyenvironment.md).
- `authorizedRights`: A pointer to a newly allocated [`AuthorizationRights`](../../Security/authorizationrights.md) structure. On return, this structure contains the rights granted by the Security framework. If you do not require this information, pass `NULL`. If you specify the [`preAuthorize`](../../Security/authorizationflags/preauthorize.md) mask in the `flags` parameter, the method returns all the requested rights, including those not granted, but the flags of the rights that could not be preauthorized include the [`kAuthorizationFlagCanNotPreAuthorize`](../../Security/kauthorizationflagcannotpreauthorize.md) bit. Free the memory associated with this set of rights by calling the Authorization Services function [`AuthorizationFreeItemSet(_:)`](../../Security/authorizationfreeitemset%28_%29.md).

## See Also

### Authorizing rights
- [func obtain(withRights: UnsafePointer<AuthorizationRights>!, flags: AuthorizationFlags, environment: UnsafePointer<AuthorizationEnvironment>!, authorizedRights: UnsafeMutablePointer<UnsafeMutablePointer<AuthorizationRights>?>!) throws](./obtain%28withrights,flags,environment,authorizedrights%29.md)
  Authorizes and preauthorizes rights to access a privileged operation and returns the granted rights.
- [- permitWithRight:flags:](./permitwithright_flags_.md)
  Authorizes and preauthorizes one specific right.
- [func obtain(withRight: AuthorizationString!, flags: AuthorizationFlags) throws](./obtain%28withright,flags%29.md)
  Authorizes and preauthorizes one specific right.


---

*[View on Apple Developer](https://developer.apple.com/documentation/securityfoundation/sfauthorization/permitwithrights:flags:environment:authorizedrights:)*