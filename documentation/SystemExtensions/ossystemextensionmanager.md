# OSSystemExtensionManager

**Framework**: System Extensions  
**Kind**: class

A type that facilitates activation and deactivation of system extensions.

**Availability**:
- macOS 10.15+

## Declaration

```swift
class OSSystemExtensionManager
```

## Mentions

- [Installing System Extensions and Drivers](installing-system-extensions-and-drivers.md)

#### Overview

Create an instance of [`OSSystemExtensionRequest`](ossystemextensionrequest.md) with the class methods on that type, and submit it to the shared instance of the extension manager with [`submitRequest(_:)`](ossystemextensionmanager/submitrequest(_:).md). Set the [`delegate`](ossystemextensionrequest/delegate.md) on the request to receive the result of the activation or deactivation. The delegate also receives notifications if the user needs to authorize the extension or if a version conflict occurs.

## Topics

### Accessing the Shared Extension Manager
- [class var shared: OSSystemExtensionManager](ossystemextensionmanager/shared.md)
  The shared instance of the extension manager.
### Submitting Requests
- [func submitRequest(OSSystemExtensionRequest)](ossystemextensionmanager/submitrequest(_:).md)
  Submits a system extension request to the manager.
- [class OSSystemExtensionRequest](ossystemextensionrequest.md)
  A request to activate or deactivate a system extension.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [Installing System Extensions and Drivers](installing-system-extensions-and-drivers.md)
  Activate system extensions and drivers to make them available to the system, and update or deactivate them as needed.
- [class OSSystemExtensionRequest](ossystemextensionrequest.md)
  A request to activate or deactivate a system extension.
- [System Extension Redistributable Entitlement](../BundleResources/Entitlements/com.apple.developer.system-extension.redistributable.md)
  A Boolean value that indicates whether other development teams may distribute a system extension you create.


---

*[View on Apple Developer](https://developer.apple.com/documentation/systemextensions/ossystemextensionmanager)*