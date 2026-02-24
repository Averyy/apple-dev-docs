# obtain(withRights:flags:environment:authorizedRights:)

**Framework**: Security Foundation  
**Kind**: method

Authorizes and preauthorizes rights to access a privileged operation and returns the granted rights.

**Availability**:
- macOS 10.10+

## Declaration

```swift
func obtain(withRights rights: UnsafePointer<AuthorizationRights>!, flags: AuthorizationFlags, environment: UnsafePointer<AuthorizationEnvironment>!, authorizedRights: UnsafeMutablePointer<UnsafeMutablePointer<AuthorizationRights>?>!) throws
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if operation completes successfully.

#### Discussion

There are three main reasons to use this method. The first reason is to preauthorize rights by specifying the `kAuthorizationFlagPreAuthorize`, `kAuthorizationFlagInteractionAllowed`, and `kAuthorizationFlagExtendRights` masks as authorization options. Preauthorization is most useful when a right has a zero timeout. For example, you can preauthorize in the application and if it succeeds, call the helper tool and request authorization. This eliminates calling the helper tool if the Security framework cannot later authorize the specified rights.

The second reason to use this method is to authorize rights before performing a privileged operation by specifying the `kAuthorizationFlagInteractionAllowed`, and `kAuthorizationFlagExtendRights` masks as authorization options.

The third reason to use this method is to authorize partial rights. By specifying the `kAuthorizationFlagPartialRights`, `kAuthorizationFlagInteractionAllowed`, and `kAuthorizationFlagExtendRights` masks as authorization options, the Security framework grants all rights it can authorize. On return, the authorized set contains all the rights.

If you do not specify the `kAuthorizationFlagPartialRights` mask and the Security framework denies at least one right, then the method returns [`false`](https://developer.apple.com/documentation/Swift/false) and the `error` parameter returns `errAuthorizationDenied`.

If you do not specify the `kAuthorizationFlagInteractionAllowed` mask and the Security framework requires user interaction, then the method returns [`false`](https://developer.apple.com/documentation/Swift/false) and the `error` parameter returns `errAuthorizationInteractionNotAllowed`.

If you specify the `kAuthorizationFlagInteractionAllowed` mask and the user cancels the authentication process, then the method returns [`false`](https://developer.apple.com/documentation/Swift/false) and the `error` parameter returns `errAuthorizationCanceled`.

> **Note**: In Swift, this method returns `Void` and is marked with the `throws` keyword to indicate that it throws an error in cases of failure. You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [`Error Handling`](https://developer.apple.comhttps://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [`The Swift Programming Language`](https://developer.apple.comhttps://docs.swift.org/swift-book/) and [`About Imported Cocoa Error Parameters`](https://developer.apple.com/documentation/Swift/about-imported-cocoa-error-parameters).

## Parameters

- `rights`: A pointer to a set of authorization rights you create. Pass `NULL` if the application requires no rights at this time.
- `flags`: A bit mask for specifying authorization options. Use the following option sets: - Pass the constant [`kAuthorizationFlagDefaults`](https://developer.apple.com/documentation/Security/AuthorizationFlags/kAuthorizationFlagDefaults) if no options are necessary.
- Specify the [`extendRights`](https://developer.apple.com/documentation/Security/AuthorizationFlags/extendRights) mask to request rights. You can also specify the [`interactionAllowed`](https://developer.apple.com/documentation/Security/AuthorizationFlags/interactionAllowed) mask to allow user interaction.
- Specify the [`partialRights`](https://developer.apple.com/documentation/Security/AuthorizationFlags/partialRights) and [`extendRights`](https://developer.apple.com/documentation/Security/AuthorizationFlags/extendRights) masks to request partial rights. You can also specify the [`interactionAllowed`](https://developer.apple.com/documentation/Security/AuthorizationFlags/interactionAllowed) mask to allow user interaction.
- Specify the [`preAuthorize`](https://developer.apple.com/documentation/Security/AuthorizationFlags/preAuthorize) and [`extendRights`](https://developer.apple.com/documentation/Security/AuthorizationFlags/extendRights) masks to preauthorize rights.
- Specify the [`destroyRights`](https://developer.apple.com/documentation/Security/AuthorizationFlags/destroyRights) mask to prevent the Security framework from preserving the rights obtained during this call.
- `environment`: Data used when authorizing or preauthorizing rights. In macOS 10.3 and later, you can pass icon or prompt data to be used in the authentication dialog box. Possible values for this parameter are listed in `Security/AuthorizationTags.h`. If you are not passing any data in this parameter, pass the constant [`kAuthorizationEmptyEnvironment`](https://developer.apple.com/documentation/Security/kAuthorizationEmptyEnvironment).
- `authorizedRights`: A pointer to a newly allocated [`AuthorizationRights`](https://developer.apple.com/documentation/Security/AuthorizationRights) structure. On return, this structure contains the rights granted by the Security framework. If you do not require this information, pass `NULL`. If you specify the [`preAuthorize`](https://developer.apple.com/documentation/Security/AuthorizationFlags/preAuthorize) mask in the `flags` parameter, the method returns all the requested rights, including those not granted, but the flags of the rights that could not be preauthorized include the [`kAuthorizationFlagCanNotPreAuthorize`](https://developer.apple.com/documentation/Security/kAuthorizationFlagCanNotPreAuthorize) bit. Free the memory associated with this set of rights by calling the Authorization Services function [`AuthorizationFreeItemSet(_:)`](https://developer.apple.com/documentation/Security/AuthorizationFreeItemSet(_:)).

## See Also

- [func obtain(withRight: AuthorizationString!, flags: AuthorizationFlags) throws](sfauthorization/obtain(withright:flags:).md)
  Authorizes and preauthorizes one specific right.


---

*[View on Apple Developer](https://developer.apple.com/documentation/securityfoundation/sfauthorization/obtain(withrights:flags:environment:authorizedrights:))*