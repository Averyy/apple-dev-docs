# deactivationRequest(forExtensionWithIdentifier:queue:)

**Framework**: System Extensions  
**Kind**: method  
**Role**: Type Method

Creates a request to deactivate a System Extension.

**Availability**:
- macOS 10.15+

## Declaration

```swift
class func deactivationRequest(forExtensionWithIdentifier identifier: String, queue: dispatch_queue_t) -> Self
```

```objc
+ (instancetype) deactivationRequestForExtension:(NSString *) identifier queue:(dispatch_queue_t) queue;
```

## Mentions

- [Installing System Extensions and Drivers](../installing-system-extensions-and-drivers.md)

#### Discussion

The system discovers existing system extensions in the `Contents/Library/SystemExtensions` directory of the main app bundle.

A deactivation request may require a restart before deactivating the extension. If the request succeeds but requires a restart to complete, the extension may still appear operational until the next restart.

## Parameters

- `identifier`: The bundle identifier of the extension to deactivate.
- `queue`: The dispatch queue to use when calling delegate methods.

## See Also

### Creating Requests
- [class func activationRequest(forExtensionWithIdentifier: String, queue: dispatch_queue_t) -> Self](./activationrequest%28forextensionwithidentifier,queue%29.md)
  Creates a request to activate a System Extension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/systemextensions/ossystemextensionrequest/deactivationrequest(forextensionwithidentifier:queue:))*