# GetArguments

**Framework**: Security  
**Kind**: property  
**Role**: Instance Property

Reads the arguments for this authorization mechanism from the authorization policy database.

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
int (*)(struct __OpaqueAuthorizationEngine *, const struct AuthorizationValueVector **) GetArguments;
```

## Return Value

A result code. Possible results are [`errAuthorizationSuccess`](../errauthorizationsuccess.md) (no error) and [`errAuthorizationInternal`](../errauthorizationinternal.md) (Security Server internal error).

## Discussion

The authorization policy database might contain arguments for each authentication mechanism. You can use this function to retrieve these arguments.

The authorization engine sends you the entry point to the [`GetArguments`](./getarguments.md) function in an [`AuthorizationCallbacks`](../authorizationcallbacks.md) structure when you call the [`AuthorizationPluginCreate`](../authorizationplugincreate.md) function.

## Parameters

- `inEngine`: An opaque handle that is passed to your plug-in when the authorization engine calls your [`MechanismCreate`](../authorizationplugininterface/mechanismcreate.md) function.
- `outArguments`: On input, allocate a pointer to an [`AuthorizationValueVector`](../authorizationvaluevector.md) structure. On output, the structure contains the number of arguments and a pointer to the data. Because your [`AuthorizationValueVector`](../authorizationvaluevector.md) structure does not own the data, you must not deallocate the structure or the data pointed to by the structure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/authorizationcallbacks/getarguments)*