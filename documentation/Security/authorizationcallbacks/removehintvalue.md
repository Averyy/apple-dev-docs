# RemoveHintValue

**Framework**: Security  
**Kind**: property  
**Role**: Instance Property

Removes a value stored by the plug-in authorization mechanism.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```c
int (*)(struct __OpaqueAuthorizationEngine *, const char *) RemoveHintValue;
```

#### Return Value

A result code. Possible results are [`errAuthorizationSuccess`](../errauthorizationsuccess.md) (no error) and [`errAuthorizationInternal`](../errauthorizationinternal.md) (Security Server internal error).

## Parameters

- `inEngine`: An opaque handle that is passed to your plug-in when the authorization engine calls your [`MechanismCreate`](../authorizationplugininterface/mechanismcreate.md) function.
- `inKey`: A key indicating which value you want to remove. This key must correspond to one you specified when you used the [`SetHintValue`](./sethintvalue.md) function to store a hint value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/authorizationcallbacks/removehintvalue)*