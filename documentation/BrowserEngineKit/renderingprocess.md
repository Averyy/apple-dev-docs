# RenderingProcess

**Framework**: BrowserEngineKit  
**Kind**: struct  
**Role**: Structure

A process that manages rendering in an app extension.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- macOS 14.3+

## Declaration

```swift
struct RenderingProcess
```

## Mentions

- [Managing the browser extension life cycle](./managing-the-browser-extension-lifecycle.md)

## Overview

A browser can have one or more rendering extensions, each of which need a separate bundle identifier. The app can launch only one instance of each rendering extension.

## Topics

### Creating and invalidating extension processes
- [init(bundleIdentifier: String?, onInterruption: () -> Void) async throws](./renderingprocess/init%28bundleidentifier,oninterruption%29.md)
  Launches a rendering extension process asynchronously.
- [func invalidate()](./renderingprocess/invalidate%28%29.md)
  Stops the rendering process.
### Creating XPC connections
- [func makeLibXPCConnection() throws -> xpc_connection_t](./renderingprocess/makelibxpcconnection%28%29.md)
  Creates a new XPC connection to the extension process.
### Coordinating processes
- [func grantCapability(ProcessCapability) throws -> ProcessCapability.Grant](./renderingprocess/grantcapability%28_%29.md)
  Grants the specified capability to the process.
- [func grantCapability(ProcessCapability, invalidationHandler: () -> Void) throws -> ProcessCapability.Grant](./renderingprocess/grantcapability%28_,invalidationhandler%29.md)
  Grants the specified capability to the process and observes an invalidation closure.
- [func createVisibilityPropagationInteraction() -> any UIInteraction](./renderingprocess/createvisibilitypropagationinteraction%28%29.md)
  Returns an interaction that associates a view with the rendering process.

## See Also

### Host app representations
- [struct WebContentProcess](./webcontentprocess.md)
  A process that manages webpage content in an app extension.
- [struct NetworkingProcess](./networkingprocess.md)
  A process that manages network connections in an app extension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/renderingprocess)*