# OSSystemExtensionRequest

**Framework**: System Extensions  
**Kind**: class  
**Role**: Class

A request to activate or deactivate a system extension.

**Availability**:
- macOS 10.15+

## Declaration

```swift
class OSSystemExtensionRequest
```

```objc
@interface OSSystemExtensionRequest : NSObject
```

## Mentions

- [Installing System Extensions and Drivers](./installing-system-extensions-and-drivers.md)

## Topics

### Creating Requests
- [class func activationRequest(forExtensionWithIdentifier: String, queue: dispatch_queue_t) -> Self](./ossystemextensionrequest/activationrequest%28forextensionwithidentifier,queue%29.md)
  Creates a request to activate a System Extension.
- [class func deactivationRequest(forExtensionWithIdentifier: String, queue: dispatch_queue_t) -> Self](./ossystemextensionrequest/deactivationrequest%28forextensionwithidentifier,queue%29.md)
  Creates a request to deactivate a System Extension.
### Working with a Delegate
- [var delegate: (any OSSystemExtensionRequestDelegate)?](./ossystemextensionrequest/delegate.md)
  A delegate to receive updates about the progress of a request.
- [protocol OSSystemExtensionRequestDelegate](./ossystemextensionrequestdelegate.md)
  A type that receives updates about the progress of a request.
### Identifying the Target Extension
- [var identifier: String](./ossystemextensionrequest/identifier.md)
  The bundle identifier of the target extension.
### Type Methods
- [class func propertiesRequest(forExtensionWithIdentifier: String, queue: dispatch_queue_t) -> Self](./ossystemextensionrequest/propertiesrequest%28forextensionwithidentifier,queue%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Extension activation and deactivation
- [Installing System Extensions and Drivers](./installing-system-extensions-and-drivers.md)
  Activate system extensions and drivers to make them available to the system, and update or deactivate them as needed.
- [class OSSystemExtensionManager](./ossystemextensionmanager.md)
  A type that facilitates activation and deactivation of system extensions.
- [System Extension Redistributable Entitlement](../BundleResources/entitlements/com.apple.developer.system-extension.redistributable.md)
  A Boolean value that indicates whether other development teams may distribute a system extension you create.


---

*[View on Apple Developer](https://developer.apple.com/documentation/systemextensions/ossystemextensionrequest)*