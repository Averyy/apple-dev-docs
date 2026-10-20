# OSSystemExtensionRequestDelegate

**Framework**: System Extensions  
**Kind**: protocol  
**Role**: Protocol

A type that receives updates about the progress of a request.

**Availability**:
- macOS 10.15+

## Declaration

```swift
protocol OSSystemExtensionRequestDelegate : NSObjectProtocol
```

```objc
@protocol OSSystemExtensionRequestDelegate <NSObject>
```

## Mentions

- [Installing System Extensions and Drivers](./installing-system-extensions-and-drivers.md)

## Topics

### Handling Success and Failure
- [func request(OSSystemExtensionRequest, didFinishWithResult: OSSystemExtensionRequest.Result)](./ossystemextensionrequestdelegate/request%28_,didfinishwithresult%29.md)
  Tells the delegate that the manager completed the request.
- [OSSystemExtensionRequest.Result](./ossystemextensionrequest/result.md)
  The result of a completed request, possibly including additional information about the extension’s state.
- [func request(OSSystemExtensionRequest, didFailWithError: any Error)](./ossystemextensionrequestdelegate/request%28_,didfailwitherror%29.md)
  Tells the delegate the manager failed to complete the request.
### Handling Indeterminate Installs
- [func requestNeedsUserApproval(OSSystemExtensionRequest)](./ossystemextensionrequestdelegate/requestneedsuserapproval%28_%29.md)
  Tells the delegate that the user must grant approval before the manager can activate the extension.
- [func request(OSSystemExtensionRequest, actionForReplacingExtension: OSSystemExtensionProperties, withExtension: OSSystemExtensionProperties) -> OSSystemExtensionRequest.ReplacementAction](./ossystemextensionrequestdelegate/request%28_,actionforreplacingextension,withextension%29.md)
  Tells the delegate that the user has a different version of the extension installed on their system.
- [class OSSystemExtensionProperties](./ossystemextensionproperties.md)
  Properties that identify a specific version of a system extension.
- [OSSystemExtensionRequest.ReplacementAction](./ossystemextensionrequest/replacementaction.md)
  Actions for describing how the extension manager should resolve a version conflict.
### Instance Methods
- [func request(OSSystemExtensionRequest, foundProperties: [OSSystemExtensionProperties])](./ossystemextensionrequestdelegate/request%28_,foundproperties%29.md)

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Working with a Delegate
- [var delegate: (any OSSystemExtensionRequestDelegate)?](./ossystemextensionrequest/delegate.md)
  A delegate to receive updates about the progress of a request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/systemextensions/ossystemextensionrequestdelegate)*