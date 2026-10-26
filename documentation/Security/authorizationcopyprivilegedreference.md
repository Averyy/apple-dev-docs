# AuthorizationCopyPrivilegedReference

**Framework**: Security  
**Kind**: func  
**Role**: Function

Retrieves the authorization reference passed by the AuthorizationExecuteWithPrivileges function.

**Availability**:
- macOS 10.1+ - Deprecated in 10.7

> **Deprecated**: Use a `launchd`-launched helper tool and/or the Service Management framework for this functionality.

## Declaration

```c
OSStatus AuthorizationCopyPrivilegedReference(AuthorizationRef*authorization, AuthorizationFlags flags);
```

#### Return Value

A result code. See [Authorization Services Result Codes](./authorization-services-result-codes.md).

#### Discussion

> ❗ **Important**:  This function is deprecated. Use a `launchd`-launched helper tool and/or the Service Management framework for this functionality.

This function retrieves the authorization reference you pass in the function [`AuthorizationExecuteWithPrivileges`](./authorizationexecutewithprivileges.md). The new process can use the authorization reference to verify authorizations obtained by the calling process.

## Parameters

- `authorization`: A pointer to an authorization reference. The Security Server allocates the authorization reference for you, so you do not need to call the function [`AuthorizationCreate(_:_:_:_:)`](./authorizationcreate%28_,_,_,_%29.md). On return, it points to a copy of the authorization reference used in the call to the [`AuthorizationExecuteWithPrivileges`](./authorizationexecutewithprivileges.md) function.
- `flags`: Reserved options. Pass the [`kAuthorizationFlagDefaults`](./authorizationflags/kauthorizationflagdefaults.md) constant.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/authorizationcopyprivilegedreference)*