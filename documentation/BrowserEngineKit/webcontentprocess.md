# WebContentProcess

**Framework**: BrowserEngineKit  
**Kind**: struct

A process that manages webpage content in an app extension.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- macOS 14.3+

## Declaration

```swift
struct WebContentProcess
```

## Mentions

- [Managing the browser extension life cycle](managing-the-browser-extension-lifecycle.md)

#### Overview

A browser app can launch multiple web content extension processes. Each instance of this structure represents a separate process.

## Topics

### Creating and invalidating extension processes
- [init(bundleIdentifier: String?, onInterruption: () -> Void) async throws](webcontentprocess/init(bundleidentifier:oninterruption:).md)
  Launches a web content process asynchronously.
- [func invalidate()](webcontentprocess/invalidate.md)
  Stops the web content process.
### Creating XPC connections
- [func makeLibXPCConnection() throws -> xpc_connection_t](webcontentprocess/makelibxpcconnection.md)
  Creates a new XPC connection to the extension process.
### Coordinating processes
- [func grantCapability(ProcessCapability) throws -> ProcessCapability.Grant](webcontentprocess/grantcapability(_:).md)
  Grants the specified capability to the process.
- [func grantCapability(ProcessCapability, invalidationHandler: () -> Void) throws -> ProcessCapability.Grant](webcontentprocess/grantcapability(_:invalidationhandler:).md)
  Grants the specified capability to the process and observes an invalidation closure.
- [func createVisibilityPropagationInteraction() -> any UIInteraction](webcontentprocess/createvisibilitypropagationinteraction.md)
  Returns an interaction that associates a view with the web content process.

## See Also

- [struct NetworkingProcess](networkingprocess.md)
  A process that manages network connections in an app extension.
- [struct RenderingProcess](renderingprocess.md)
  A process that manages rendering in an app extension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/webcontentprocess)*