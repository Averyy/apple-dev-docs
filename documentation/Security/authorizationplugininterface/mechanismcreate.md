# MechanismCreate

**Framework**: Security  
**Kind**: property  
**Role**: Instance Property

Creates an authorization mechanism.

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
int (*)(void *, struct __OpaqueAuthorizationEngine *, const char *, void **) MechanismCreate;
```

## Return Value

A result code. Return [`errAuthorizationSuccess`](../errauthorizationsuccess.md) (no error) if the function completes successfully and [`errAuthorizationInternal`](../errauthorizationinternal.md) (Security Server internal error) if any error occurs.

## Discussion

A given authorization plug-in can implement any number of authorization mechanisms, distinguished by their mechanism names in the authorization policy database.

When the authorization engine calls your [`MechanismCreate`](./mechanismcreate.md) function, you should create a mechanism of the type specified by the mechanismID parameter and return an authorization mechanism reference. Subsequently, the authorization engine can call your [`MechanismInvoke`](./mechanisminvoke.md) function to perform an authorization, or can direct you to deactivate or destroy the mechanism instance by calling your [`MechanismDeactivate`](./mechanismdeactivate.md) or [`MechanismDestroy`](./mechanismdestroy.md) functions.

## Parameters

- `inPlugin`: The authorization plug-in reference you assigned to the plug-in in the [`AuthorizationPluginCreate`](../authorizationplugincreate.md) function.
- `inEngine`: An opaque handle that you must pass back to the authorization engine when you call one of the engine’s callback functions.
- `mechanismId`: The mechanism ID specified in the authorization policy database is passed to the plug-in so that the plug-in can create the appropriate mechanism.
- `outMechanism`: On output, points to an authorization mechanism reference that you define. The authorization engine includes this reference when it calls your plug-in so that you can identify which instance of a mechanism to invoke, deactivate, or destroy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/authorizationplugininterface/mechanismcreate)*