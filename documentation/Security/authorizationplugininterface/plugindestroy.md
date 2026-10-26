# PluginDestroy

**Framework**: Security  
**Kind**: property  
**Role**: Instance Property

Notifies the plug-in that it is about to be unloaded.

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
int (*)(void *) PluginDestroy;
```

#### Return Value

A result code. Return [`errAuthorizationSuccess`](../errauthorizationsuccess.md) (no error) if the function completes successfully and [`errAuthorizationInternal`](../errauthorizationinternal.md) (Security Server internal error) if any error occurs.

#### Discussion

When this function is called, your plug-in should release any resources it is holding and do any other cleanup necessary (such as deleting temporary files) before it is unloaded.

## Parameters

- `inPlugin`: The authorization plug-in reference you assigned to the plug-in in the [`AuthorizationPluginCreate`](../authorizationplugincreate.md) function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/authorizationplugininterface/plugindestroy)*