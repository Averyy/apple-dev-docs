# GetImmutableHintValue

**Framework**: Security  
**Kind**: property  
**Role**: Instance Property

Reads an immutable value stored by the plug-in authorization mechanism.

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
int (*)(struct __OpaqueAuthorizationEngine *, const char *, const struct AuthorizationValue **) GetImmutableHintValue;
```

#### Return Value

A result code. Possible results are [`errAuthorizationSuccess`](../errauthorizationsuccess.md) (no error) and [`errAuthorizationInternal`](../errauthorizationinternal.md) (Security Server internal error).

#### Discussion

This function behaves like [`GetHintValue`](./gethintvalue.md), except that the hint is immutable.

## Parameters

- `inEngine`: An opaque handle that is passed to your plug-in when the authorization engine calls your [`MechanismCreate`](../authorizationplugininterface/mechanismcreate.md) function.
- `inKey`: A key indicating which value you want to retrieve. This key must correspond to one you specified when you used the [`SetHintValue`](./sethintvalue.md) function to store a hint value.
- `outValue`: On input, allocate a pointer to an [`AuthorizationValue`](../authorizationvalue.md) structure. On output, the structure contains the size of the data and a pointer to the data. Because your [`AuthorizationValue`](../authorizationvalue.md) structure does not own the data, you must not deallocate the structure or the data pointed to by the structure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/authorizationcallbacks/getimmutablehintvalue)*