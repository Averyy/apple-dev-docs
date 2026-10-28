# MechanismDestroy

**Framework**: Security  
**Kind**: property  
**Role**: Instance Property

Destroys an authorization mechanism.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.4+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```c
int (*)(void *) MechanismDestroy;
```

## Return Value

A result code. Return [`errAuthorizationSuccess`](../errauthorizationsuccess.md) (no error) if the function completes successfully and [`errAuthorizationInternal`](../errauthorizationinternal.md) (Security Server internal error) if any error occurs.

## Discussion

When the authorization engine calls your [`MechanismDestroy`](./mechanismdestroy.md) function, you must release all resources owned by your mechanism and do any other cleanup necessary (such as deleting temporary files).

## Parameters

- `inMechanism`: An authorization mechanism reference that you returned when your [`MechanismCreate`](./mechanismcreate.md) function was called to create the mechanism.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/authorizationplugininterface/mechanismdestroy)*