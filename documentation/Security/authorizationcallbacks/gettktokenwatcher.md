# GetTKTokenWatcher

**Framework**: Security  
**Kind**: property  
**Role**: Instance Property

Constructs a token watcher.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.13.4+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```c
int (*)(struct __OpaqueAuthorizationEngine *, const void **) GetTKTokenWatcher;
```

#### Discussion

The caller owns the returned token watcher and is responsible for releasing it.

> ❗ **Important**:  This function is only available when the callback [`version`](./version.md) is 3 or higher.

## Parameters

- `inEngine`: An opaque handle that’s passed to your plug-in when the authorization engine calls your [`MechanismCreate`](../authorizationplugininterface/mechanismcreate.md) function.
- `outValue`: A pointer the function uses to return the [`TKTokenWatcher`](../../CryptoTokenKit/tktokenwatcher.md) instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/authorizationcallbacks/gettktokenwatcher)*