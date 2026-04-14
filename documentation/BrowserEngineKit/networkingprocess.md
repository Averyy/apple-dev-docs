# NetworkingProcess

**Framework**: BrowserEngineKit  
**Kind**: struct

A process that manages network connections in an app extension.

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

A browser app can have one or more networking extensions, each of which need a separate bundle identifier. The app can launch only one instance of each networking extension.

## Topics

### Creating and invalidating extension processes
- [init(bundleIdentifier: String?, onInterruption: () -> Void) async throws](networkingprocess/init(bundleidentifier:oninterruption:).md)
  Launches a networking extension process asynchronously.
- [func invalidate()](networkingprocess/invalidate.md)
  Stops the networking process.
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
  A process that manages webpage content in an app extension.
- [struct RenderingProcess](renderingprocess.md)
  A process that manages rendering in an app extension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/networkingprocess)*