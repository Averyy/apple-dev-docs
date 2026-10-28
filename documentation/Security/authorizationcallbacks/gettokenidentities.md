# GetTokenIdentities

**Framework**: Security  
**Kind**: property  
**Role**: Instance Property

Returns an array of identities available on tokens.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```c
int (*)(struct __OpaqueAuthorizationEngine *, const void *, const struct __CFArray **) GetTokenIdentities;
```

## Discussion

The caller owns the returned array and is responsible for releasing it.

> ❗ **Important**:  This function is only available when the callback [`version`](./version.md) is 2 or higher.

## Parameters

- `inEngine`: An opaque handle that’s passed to your plug-in when the authorization engine calls your [`MechanismCreate`](../authorizationplugininterface/mechanismcreate.md) function.
- `context`: A local authentication context returned by the [`GetLAContext`](./getlacontext.md) call.
- `outValue`: A pointer the function uses to return an array of identities, each of which consists of two array elements: a [`SecIdentity`](../secidentity.md) instance and a text description of the identity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/authorizationcallbacks/gettokenidentities)*