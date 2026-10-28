# requestNeedsUserApproval(_:)

**Framework**: System Extensions  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Tells the delegate that the user must grant approval before the manager can activate the extension.

**Availability**:
- macOS 10.15+

## Declaration

```swift
func requestNeedsUserApproval(_ request: OSSystemExtensionRequest)
```

```objc
- (void) requestNeedsUserApproval:(OSSystemExtensionRequest *) request;
```

## Discussion

Activating an extension may require explicit user approval to proceed. For example, this occurs when the user hasn’t approved the extension. The manager calls this method to notify the delegate. Activation remains pending until the user grants or denies permission, or until the app quits.

## See Also

### Handling Indeterminate Installs
- [func request(OSSystemExtensionRequest, actionForReplacingExtension: OSSystemExtensionProperties, withExtension: OSSystemExtensionProperties) -> OSSystemExtensionRequest.ReplacementAction](./request%28_,actionforreplacingextension,withextension%29.md)
  Tells the delegate that the user has a different version of the extension installed on their system.
- [class OSSystemExtensionProperties](../ossystemextensionproperties.md)
  Properties that identify a specific version of a system extension.
- [OSSystemExtensionRequest.ReplacementAction](../ossystemextensionrequest/replacementaction.md)
  Actions for describing how the extension manager should resolve a version conflict.


---

*[View on Apple Developer](https://developer.apple.com/documentation/systemextensions/ossystemextensionrequestdelegate/requestneedsuserapproval(_:))*