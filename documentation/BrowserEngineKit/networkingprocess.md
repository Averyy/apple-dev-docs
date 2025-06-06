# NetworkingProcess

**Framework**: BrowserEngineKit  
**Kind**: struct

An object that represents a running browser networking extension process.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- macOS 14.3+

## Declaration

```swift
struct NetworkingProcess
```

## Mentions

- [Managing the browser extension life cycle](managing-the-browser-extension-lifecycle.md)

#### Overview

Your browser app may have one or more networking extensions, which each need a separate bundle identifier. Your browser can launch one instance of each of its networking extensions.

## Topics

### Creating and invalidating extension processes
- [init(bundleIdentifier: String?, onInterruption: () -> Void) async throws](networkingprocess/init(bundleidentifier:oninterruption:).md)
  Launches a networking extension process asynchronously.
- [func invalidate()](networkingprocess/invalidate.md)
  Stops the extension process.
### Creating XPC connections
- [func makeLibXPCConnection() throws -> xpc_connection_t](networkingprocess/makelibxpcconnection.md)
  Creates a new XPC connection to the extension process.
### Coordinating processes
- [func grantCapability(ProcessCapability) throws -> ProcessCapability.Grant](networkingprocess/grantcapability(_:).md)
  Grants the specified capability to the process.
- [func grantCapability(ProcessCapability, invalidationHandler: () -> Void) throws -> ProcessCapability.Grant](networkingprocess/grantcapability(_:invalidationhandler:).md)
  Grants the specified capability to the process, calling the handler when the capability becomes invalid.

## See Also

- [struct WebContentProcess](webcontentprocess.md)
  An object that represents a running web content extension process.
- [struct RenderingProcess](renderingprocess.md)
  An object that represents a running browser rendering extension process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/networkingprocess)*