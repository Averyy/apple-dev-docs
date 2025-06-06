# AuthorizationCopyRights(_:_:_:_:_:)

**Framework**: Security  
**Kind**: func

Authorizes and preauthorizes rights synchronously.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
func AuthorizationCopyRights(_ authorization: AuthorizationRef, _ rights: UnsafePointer<AuthorizationRights>, _ environment: UnsafePointer<AuthorizationEnvironment>?, _ flags: AuthorizationFlags, _ authorizedRights: UnsafeMutablePointer<UnsafeMutablePointer<AuthorizationRights>?>?) -> OSStatus
```

## Mentions

- [Extending authorization services with plug-ins](extending-authorization-services-with-plug-ins.md)

#### Return Value

A result code. See [`Authorization Services Result Codes`](authorization-services-result-codes.md).

#### Discussion

There are three main reasons to use this function. The first reason is to preauthorize rights by specifying the [`preAuthorize`](authorizationflags/preauthorize.md), [`interactionAllowed`](authorizationflags/interactionallowed.md), and [`extendRights`](authorizationflags/extendrights.md) masks as authorization options. Preauthorization is most useful when a right has a zero timeout. For example, you can preauthorize in the application and if it succeeds, call the helper tool and request authorization. This eliminates calling the helper tool if the Security Server cannot later authorize the specified rights.

The second reason to use this function is to authorize rights before performing a privileged operation by specifying the [`interactionAllowed`](authorizationflags/interactionallowed.md), and [`extendRights`](authorizationflags/extendrights.md) masks as authorization options.

The third reason to use this function is to authorize partial rights. By specifying the [`partialRights`](authorizationflags/partialrights.md), [`interactionAllowed`](authorizationflags/interactionallowed.md), and [`extendRights`](authorizationflags/extendrights.md) masks as authorization options, the Security Server grants all rights it can authorize. On return, the authorized set contains all the rights.

If you do not specify the [`partialRights`](authorizationflags/partialrights.md) mask and the Security Server denies at least one right, then the status of this function on return is [`errAuthorizationDenied`](errauthorizationdenied.md).

If you do not specify the [`interactionAllowed`](authorizationflags/interactionallowed.md) mask and the Security Server requires user interaction, then the status of this function on return is [`errAuthorizationInteractionNotAllowed`](errauthorizationinteractionnotallowed.md).

If you specify the [`interactionAllowed`](authorizationflags/interactionallowed.md) mask and the user cancels the authentication process, then the status of this function on return is [`errAuthorizationCanceled`](errauthorizationcanceled.md).

## Parameters

- `authorization`: An authorization reference referring to the authorization session.
- `rights`: A pointer to a set of authorization rights you create. Pass   if the application requires no rights at this time.
- `environment`: Data used when authorizing or preauthorizing rights. Not used in OS X v10.2 and earlier. In macOS 10.3 and later, you can pass icon or prompt data to be used in the authentication dialog box. In macOS 10.4 and later, you can also pass a user name and password in order to authorize a user without displaying the authentication dialog box. Possible values for this parameter are listed in  . The data passed in this parameter is not stored in the authorization reference; it is used only during authorization. If you are not passing any data in this parameter, pass the constant  .
- `flags`: A bit mask for specifying authorization options. Use the following option sets.
- `authorizedRights`: A pointer to a newly allocated   structure. On return, this structure contains the rights granted by the Security framework. If you do not require this information, pass  . If you specify the   mask in the   parameter, the method returns all the requested rights, including those not granted, but the flags of the rights that could not be preauthorized include the   bit.   Free the memory associated with this set by calling the function  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/authorizationcopyrights(_:_:_:_:_:))*