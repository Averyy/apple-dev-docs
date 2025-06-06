# WebContentProcess

**Framework**: BrowserEngineKit  
**Kind**: struct

An object that represents a running web content extension process.

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

A web browser app may launch multiple web content extension processes, and each instance of this object represents a separate process.

## Topics

### Creating and invalidating extension processes
- [init(bundleIdentifier: String?, onInterruption: () -> Void) async throws](webcontentprocess/init(bundleidentifier:oninterruption:).md)
  Launches a web content process asynchronously.
- [func invalidate()](webcontentprocess/invalidate.md)
  Stops the extension process.
### Creating XPC connections
- [func makeLibXPCConnection() throws -> xpc_connection_t](webcontentprocess/makelibxpcconnection.md)
  Creates a new XPC connection to the extension process.
### Coordinating processes
- [func grantCapability(ProcessCapability) throws -> ProcessCapability.Grant](webcontentprocess/grantcapability(_:).md)
  Grants the specified capability to the process.
- [func grantCapability(ProcessCapability, invalidationHandler: () -> Void) throws -> ProcessCapability.Grant](webcontentprocess/grantcapability(_:invalidationhandler:).md)
  Grants the specified capability to the process, calling the handler when the capability becomes invalid.
- [func createVisibilityPropagationInteraction() -> any UIInteraction](webcontentprocess/createvisibilitypropagationinteraction.md)
  Returns an interaction that associates a view with the web content process.

## See Also

- [struct NetworkingProcess](networkingprocess.md)
  An object that represents a running browser networking extension process.
- [struct RenderingProcess](renderingprocess.md)
  An object that represents a running browser rendering extension process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/webcontentprocess)*