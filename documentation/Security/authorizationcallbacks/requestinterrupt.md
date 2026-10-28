# RequestInterrupt

**Framework**: Security  
**Kind**: property  
**Role**: Instance Property

Requests the authorization engine to interrupt the currently active authorization mechanism.

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
int (*)(struct __OpaqueAuthorizationEngine *) RequestInterrupt;
```

## Return Value

A result code. Possible results are [`errAuthorizationSuccess`](../errauthorizationsuccess.md) (no error) and [`errAuthorizationInternal`](../errauthorizationinternal.md) (Security Server internal error).

## Discussion

When you call this function, the security engine calls the [`MechanismDeactivate`](../authorizationplugininterface/mechanismdeactivate.md) function for your plug-in’s currently-active mechanism; that is, the mechanism that was last invoked and that has not yet called the [`SetResult`](./setresult.md) function to report its result. Your mechanism should then stop any active processing and call the [`DidDeactivate`](./diddeactivate.md) function. When all mechanisms are inactive (that is, they have called either [`SetResult`](./setresult.md) or [`DidDeactivate`](./diddeactivate.md)), the authorization engine calls the [`MechanismInvoke`](../authorizationplugininterface/mechanisminvoke.md) function for the mechanism that called [`RequestInterrupt`](./requestinterrupt.md) so that it can resume the authorization process from that point. After all mechanisms have called [`SetResult`](./setresult.md), the authorization engine calls each mechanism’s [`MechanismDestroy`](../authorizationplugininterface/mechanismdestroy.md) function.

If your mechanism spins off a separate process or UI thread, that thread can call the [`RequestInterrupt`](./requestinterrupt.md) function to re-invoke the mechanism, even if that mechanism has already called the [`SetResult`](./setresult.md) function. For example, if your plug-in implements a smart card authentication method, reading and evaluating the card might take several minutes to perform. Therefore, in order to avoid blocking other processing while the card is being evaluated, you might spin off a UI thread to interact with the user and then return from [`MechanismInvoke`](../authorizationplugininterface/mechanisminvoke.md). When the card has been read, the UI thread calls the [`SetResult`](./setresult.md) function with a value of [`kAuthorizationResultAllow`](../authorizationresult/kauthorizationresultallow.md) and changes the UI to request the user’s PIN. The authorization engine calls the next mechanism, which verifies the PIN. If the user pulls out the card before the verification is complete, the UI thread can call [`RequestInterrupt`](./requestinterrupt.md). The authorization engine then calls the active mechanism’s [`MechanismDeactivate`](../authorizationplugininterface/mechanismdeactivate.md) function, causing it to terminate the PIN verification and call [`DidDeactivate`](./diddeactivate.md). Then the authorization engine calls your UI mechanism’s [`MechanismInvoke`](../authorizationplugininterface/mechanisminvoke.md) function again. Your UI can then prompt the user to reinsert the card.

To understand this sequence better, suppose your plug-in contains three mechanisms: A, B, and C. Mechanism A has called [`SetResult`](./setresult.md) and has no active processes. Mechanism B has called [`SetResult`](./setresult.md), but still has a UI thread running. Mechanism C is running and has not yet called [`SetResult`](./setresult.md). The user clicks Cancel or otherwise interrupts the UI thread, causing the UI thread to call the [`RequestInterrupt`](./requestinterrupt.md) function. The following sequence of events occurs:

1. The authorization engine calls mechanism C’s [`MechanismDeactivate`](../authorizationplugininterface/mechanismdeactivate.md) function.
2. Mechanism C stops active processing and calls the [`DidDeactivate`](./diddeactivate.md) function.
3. The authorization engine calls mechanism B’s [`MechanismInvoke`](../authorizationplugininterface/mechanisminvoke.md) function (because mechanism B is the one that called [`RequestInterrupt`](./requestinterrupt.md)).
4. Mechanism B updates the UI and calls the [`SetResult`](./setresult.md) function with the value [`kAuthorizationResultAllow`](../authorizationresult/kauthorizationresultallow.md).
5. The authorization engine calls mechanism C’s [`MechanismInvoke`](../authorizationplugininterface/mechanisminvoke.md) function.
6. Mechanism C completes processing and calls [`SetResult`](./setresult.md) with [`kAuthorizationResultAllow`](../authorizationresult/kauthorizationresultallow.md).
7. The authorization engine calls the [`MechanismDestroy`](../authorizationplugininterface/mechanismdestroy.md) function of each mechanism in turn (A, B, then C).

The authorization engine sends you the entry point to the [`RequestInterrupt`](./requestinterrupt.md) function in an [`AuthorizationCallbacks`](../authorizationcallbacks.md) structure when you call the [`AuthorizationPluginCreate`](../authorizationplugincreate.md) function.

## Parameters

- `inEngine`: An opaque handle that is passed to your plug-in when the authorization engine calls your [`MechanismCreate`](../authorizationplugininterface/mechanismcreate.md) function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/authorizationcallbacks/requestinterrupt)*