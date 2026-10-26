# DidDeactivate

**Framework**: Security  
**Kind**: property  
**Role**: Instance Property

Reports the successful deactivation of an authorization mechanism.

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
int (*)(struct __OpaqueAuthorizationEngine *) DidDeactivate;
```

#### Return Value

A result code. Possible results are [`errAuthorizationSuccess`](../errauthorizationsuccess.md) (no error) and [`errAuthorizationInternal`](../errauthorizationinternal.md) (Security Server internal error).

#### Discussion

Call this function after deactivating your authorization mechanism in response to a call to your [`MechanismDeactivate`](../authorizationplugininterface/mechanismdeactivate.md) function. The authorization engine waits for confirmation that all mechanisms have deactivated before continuing.

The authorization engine sends you the entry point to the [`DidDeactivate`](./diddeactivate.md) function in an [`AuthorizationCallbacks`](../authorizationcallbacks.md) structure when you call the [`AuthorizationPluginCreate`](../authorizationplugincreate.md) function.

## Parameters

- `inEngine`: An opaque handle that is passed to your plug-in when the authorization engine calls your [`MechanismCreate`](../authorizationplugininterface/mechanismcreate.md) function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/authorizationcallbacks/diddeactivate)*