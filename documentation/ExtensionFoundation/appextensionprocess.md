# AppExtensionProcess

**Framework**: ExtensionFoundation  
**Kind**: struct

An object that represents a running app extension process.

**Availability**:
- macOS 13.0+

## Declaration

```swift
struct AppExtensionProcess
```

#### Overview

The system guarantees that the extension process has launched by the time any init methods return. If the extension process exits, the system calls [`onInterruption`](appextensionprocess/configuration/oninterruption.md) on configuration object you passed to the init method.

## Topics

### Finding or Launching Extensions
- [init(configuration: AppExtensionProcess.Configuration) throws](appextensionprocess/init(configuration:)-2g0cy.md)
  Synchronously finds an existing extension process or launches a new one.
- [init(configuration: AppExtensionProcess.Configuration) async throws](appextensionprocess/init(configuration:)-38zf.md)
  Asynchronously finds an existing extension process or launches a one.
- [AppExtensionProcess.Configuration](appextensionprocess/configuration.md)
  An object that holds configuration options for an app extension process.
### Managing the Extension Process
- [func makeXPCConnection() throws -> NSXPCConnection](appextensionprocess/makexpcconnection.md)
  Creates a new XPC connection to the extension process.
- [func invalidate()](appextensionprocess/invalidate.md)
  Stop the extension process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/extensionfoundation/appextensionprocess)*