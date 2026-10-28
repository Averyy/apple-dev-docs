# SetResult

**Framework**: Security  
**Kind**: property  
**Role**: Instance Property

Returns the result of an authorization operation.

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
int (*)(struct __OpaqueAuthorizationEngine *, enum AuthorizationResult) SetResult;
```

## Mentions

- [Extending authorization services with plug-ins](../extending-authorization-services-with-plug-ins.md)

## Return Value

A result code. Possible results are [`errAuthorizationSuccess`](../errauthorizationsuccess.md) (no error) and [`errAuthorizationInternal`](../errauthorizationinternal.md) (Security Server internal error).

## Discussion

When an application calls the [`AuthorizationCopyRights(_:_:_:_:_:)`](../authorizationcopyrights%28_,_,_,_,_%29.md) function to request a specific authorization right, the Security Agent looks for that right in the authorization policy database. If that right corresponds to your plug-in, the authorization engine calls the [`MechanismInvoke`](../authorizationplugininterface/mechanisminvoke.md) function for each mechanism listed in the policy database for your plug-in.

When the authorization engine calls your [`MechanismInvoke`](../authorizationplugininterface/mechanisminvoke.md) function, your plug-in should invoke the specified mechanism to attempt an authorization operation. You use the `SetResult` function to return the results of this operation. If the mechanism returns [`kAuthorizationResultAllow`](../authorizationresult/kauthorizationresultallow.md), then the authorization engine calls the next mechanism (if any) specified in the authorization policy database for the policy. If any of the mechanisms report a result other than [`kAuthorizationResultAllow`](../authorizationresult/kauthorizationresultallow.md), the authorization attempt fails. If all of the mechanisms report results of [`kAuthorizationResultAllow`](../authorizationresult/kauthorizationresultallow.md), the authorization is considered to have succeeded.

Note that you can spin off a separate process and return from [`MechanismInvoke`](../authorizationplugininterface/mechanisminvoke.md) before calling `SetResult`. For example, you might do so to avoid blocking the Security Server if your mechanism takes a significant amount of time to complete or if you want to be able to cancel the operation by calling the [`RequestInterrupt`](./requestinterrupt.md) function (if, for example, the user has clicked Cancel).In that case, your separate process must call the `SetResult` function to report the result; the authorization engine does not call the next mechanism until you do so.

The authorization engine sends you the entry point to the `SetResult` function in an [`AuthorizationCallbacks`](../authorizationcallbacks.md) structure when you call the [`AuthorizationPluginCreate`](../authorizationplugincreate.md) function.

## Parameters

- `inEngine`: An opaque handle that is passed to your plug-in when the authorization engine calls your [`MechanismCreate`](../authorizationplugininterface/mechanismcreate.md) function.
- `inResult`: The result of the authorization attempt. See [`AuthorizationResult`](../authorizationresult.md) for possible values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/authorizationcallbacks/setresult)*