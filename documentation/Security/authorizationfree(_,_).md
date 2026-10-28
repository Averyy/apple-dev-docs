# AuthorizationFree(_:_:)

**Framework**: Security  
**Kind**: func  
**Role**: Function

Frees the memory associated with an authorization reference.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
func AuthorizationFree(_ authorization: AuthorizationRef, _ flags: AuthorizationFlags) -> OSStatus
```

```c
OSStatus AuthorizationFree(AuthorizationRef authorization, AuthorizationFlags flags);
```

## Return Value

A result code. See [Authorization Services Result Codes](./authorization-services-result-codes.md).

## Discussion

Call this function when your application no longer needs the authorization reference you created using the function [`AuthorizationCreate(_:_:_:_:)`](./authorizationcreate%28_,_,_,_%29.md).

## Parameters

- `authorization`: The authorization reference to free.
- `flags`: A bit mask. In most cases, pass the constant [`kAuthorizationFlagDefaults`](./authorizationflags/kauthorizationflagdefaults.md). To remove all shared and non-shared authorizations, pass the constant [`destroyRights`](./authorizationflags/destroyrights.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/authorizationfree(_:_:))*