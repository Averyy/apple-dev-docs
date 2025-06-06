# deactivationRequest(forExtensionWithIdentifier:queue:)

**Framework**: System Extensions  
**Kind**: method

Creates a request to deactivate a System Extension.

**Availability**:
- macOS 10.15+

## Declaration

```swift
class func deactivationRequest(forExtensionWithIdentifier identifier: String, queue: dispatch_queue_t) -> Self
```

## Mentions

- [Installing System Extensions and Drivers](installing-system-extensions-and-drivers.md)

#### Discussion

The system discovers existing system extensions in the `Contents/Library/SystemExtensions` directory of the main app bundle.

A deactivation request may require a restart before deactivating the extension. If the request succeeds but requires a restart to complete, the extension may still appear operational until the next restart.

## Parameters

- `identifier`: The bundle identifier of the extension to deactivate.
- `queue`: The dispatch queue to use when calling delegate methods.

## See Also

- [class func activationRequest(forExtensionWithIdentifier: String, queue: dispatch_queue_t) -> Self](ossystemextensionrequest/activationrequest(forextensionwithidentifier:queue:).md)
  Creates a request to activate a System Extension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/systemextensions/ossystemextensionrequest/deactivationrequest(forextensionwithidentifier:queue:))*