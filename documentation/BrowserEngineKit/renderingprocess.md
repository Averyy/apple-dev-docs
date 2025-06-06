# RenderingProcess

**Framework**: BrowserEngineKit  
**Kind**: struct

An object that represents a running browser rendering extension process.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- macOS 14.3+

## Declaration

```swift
struct RenderingProcess
```

## Mentions

- [Managing the browser extension life cycle](managing-the-browser-extension-lifecycle.md)

#### Overview

Your browser app may have one or more rendering extensions, which each need a separate bundle identifier. Your browser can launch one instance of each of its rendering extensions.

## Topics

### Creating and invalidating extension processes
- [init(bundleIdentifier: String?, onInterruption: () -> Void) async throws](renderingprocess/init(bundleidentifier:oninterruption:).md)
  Launches a rendering extension process asynchronously.
- [func invalidate()](renderingprocess/invalidate.md)
  Stops the extension process.
### Creating XPC connections
- [func makeLibXPCConnection() throws -> xpc_connection_t](renderingprocess/makelibxpcconnection.md)
  Creates a new XPC connection to the extension process.
### Coordinating processes
- [func grantCapability(ProcessCapability) throws -> ProcessCapability.Grant](renderingprocess/grantcapability(_:).md)
  Grants the specified capability to the process.
- [func grantCapability(ProcessCapability, invalidationHandler: () -> Void) throws -> ProcessCapability.Grant](renderingprocess/grantcapability(_:invalidationhandler:).md)
  Grants the specified capability to the process, calling the handler when the capability becomes invalid.
- [func createVisibilityPropagationInteraction() -> any UIInteraction](renderingprocess/createvisibilitypropagationinteraction.md)
  Returns an interaction that associates a view with the rendering process.

## See Also

- [struct WebContentProcess](webcontentprocess.md)
  An object that represents a running web content extension process.
- [struct NetworkingProcess](networkingprocess.md)
  An object that represents a running browser networking extension process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/renderingprocess)*