# MechanismInvoke

**Framework**: Security  
**Kind**: property  
**Role**: Instance Property

Invokes an authorization mechanism to perform an authorization operation.

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
int (*)(void *) MechanismInvoke;
```

## Mentions

- [Extending authorization services with plug-ins](../extending-authorization-services-with-plug-ins.md)

#### Return Value

A result code. Return [`errAuthorizationSuccess`](../errauthorizationsuccess.md) (no error) if the function completes successfully and [`errAuthorizationInternal`](../errauthorizationinternal.md) (Security Server internal error) if any error occurs.

#### Discussion

When the authorization engine calls your `MechanismInvoke` function, you should perform the authorization operation indicated by the mechanism reference. You can use the functions [`GetArguments`](../authorizationcallbacks/getarguments.md), [`GetContextValue`](../authorizationcallbacks/getcontextvalue.md), and [`GetHintValue`](../authorizationcallbacks/gethintvalue.md) to get more information, if any, about the authorization.

## Parameters

- `inMechanism`: An authorization mechanism reference that you returned when your [`MechanismCreate`](./mechanismcreate.md) function was called to create the mechanism.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/authorizationplugininterface/mechanisminvoke)*