# OSSystemExtensionRequestDelegate

**Framework**: System Extensions  
**Kind**: protocol

A type that receives updates about the progress of a request.

**Availability**:
- macOS 10.15+

## Declaration

```swift
protocol OSSystemExtensionRequestDelegate : NSObjectProtocol
```

## Mentions

- [Installing System Extensions and Drivers](installing-system-extensions-and-drivers.md)

## Topics

### Handling Success and Failure
- [func request(OSSystemExtensionRequest, didFinishWithResult: OSSystemExtensionRequest.Result)](ossystemextensionrequestdelegate/request(_:didfinishwithresult:).md)
  Tells the delegate that the manager completed the request.
- [OSSystemExtensionRequest.Result](ossystemextensionrequest/result.md)
  The result of a completed request, possibly including additional information about the extension’s state.
- [func request(OSSystemExtensionRequest, didFailWithError: any Error)](ossystemextensionrequestdelegate/request(_:didfailwitherror:).md)
  Tells the delegate the manager failed to complete the request.
### Handling Indeterminate Installs
- [func requestNeedsUserApproval(OSSystemExtensionRequest)](ossystemextensionrequestdelegate/requestneedsuserapproval(_:).md)
  Tells the delegate that the user must grant approval before the manager can activate the extension.
- [func request(OSSystemExtensionRequest, actionForReplacingExtension: OSSystemExtensionProperties, withExtension: OSSystemExtensionProperties) -> OSSystemExtensionRequest.ReplacementAction](ossystemextensionrequestdelegate/request(_:actionforreplacingextension:withextension:).md)
  Tells the delegate that the user has a different version of the extension installed on their system.
- [class OSSystemExtensionProperties](ossystemextensionproperties.md)
  Properties that identify a specific version of a system extension.
- [OSSystemExtensionRequest.ReplacementAction](ossystemextensionrequest/replacementaction.md)
  Actions for describing how the extension manager should resolve a version conflict.
### Instance Methods
- [func request(OSSystemExtensionRequest, foundProperties: [OSSystemExtensionProperties])](ossystemextensionrequestdelegate/request(_:foundproperties:).md)

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [var delegate: (any OSSystemExtensionRequestDelegate)?](ossystemextensionrequest/delegate.md)
  A delegate to receive updates about the progress of a request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/systemextensions/ossystemextensionrequestdelegate)*