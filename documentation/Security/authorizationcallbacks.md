# AuthorizationCallbacks

**Framework**: Security  
**Kind**: struct  
**Role**: Structure

The interface implemented by the Security Server.

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
typedef struct AuthorizationCallbacks { ... } AuthorizationCallbacks;
```

## Mentions

- [Extending authorization services with plug-ins](./extending-authorization-services-with-plug-ins.md)

#### Overview

This structure declares the functions that your authorization plug-in uses to communicate with the authorization engine. These functions are passed to your plug-in through the [`AuthorizationPluginCreate`](./authorizationplugincreate.md) function.

## Topics

### Instance Properties
- [SetResult](./authorizationcallbacks/setresult.md)
  Returns the result of an authorization operation.
- [RequestInterrupt](./authorizationcallbacks/requestinterrupt.md)
  Requests the authorization engine to interrupt the currently active authorization mechanism.
- [DidDeactivate](./authorizationcallbacks/diddeactivate.md)
  Reports the successful deactivation of an authorization mechanism.
- [GetContextValue](./authorizationcallbacks/getcontextvalue.md)
  Reads a value collected during authorization.
- [SetContextValue](./authorizationcallbacks/setcontextvalue.md)
  Stores data collected during authorization as a key-value pair.
- [RemoveContextValue](./authorizationcallbacks/removecontextvalue.md)
  Removes a value collected during authorization.
- [GetHintValue](./authorizationcallbacks/gethintvalue.md)
  Reads a value stored by the plug-in authorization mechanism.
- [GetImmutableHintValue](./authorizationcallbacks/getimmutablehintvalue.md)
  Reads an immutable value stored by the plug-in authorization mechanism.
- [SetHintValue](./authorizationcallbacks/sethintvalue.md)
  Stores data needed during authorization as a key-value pair.
- [RemoveHintValue](./authorizationcallbacks/removehintvalue.md)
  Removes a value stored by the plug-in authorization mechanism.
- [GetArguments](./authorizationcallbacks/getarguments.md)
  Reads the arguments for this authorization mechanism from the authorization policy database.
- [GetSessionId](./authorizationcallbacks/getsessionid.md)
  Reads the session ID.
- [GetLAContext](./authorizationcallbacks/getlacontext.md)
  Constructs a local authentication context.
- [GetTokenIdentities](./authorizationcallbacks/gettokenidentities.md)
  Returns an array of identities available on tokens.
- [GetTKTokenWatcher](./authorizationcallbacks/gettktokenwatcher.md)
  Constructs a token watcher.
- [version](./authorizationcallbacks/version.md)
  The engine callback version.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/authorizationcallbacks)*