# OSSystemExtensionRequest.ReplacementAction

**Framework**: System Extensions  
**Kind**: enum

Actions for describing how the extension manager should resolve a version conflict.

**Availability**:
- macOS 10.15+

## Declaration

```swift
enum ReplacementAction
```

## Topics

### Replacement Actions
- [OSSystemExtensionRequest.ReplacementAction.cancel](ossystemextensionrequest/replacementaction/cancel.md)
  An action that tells the manager to cancel replacement of a system extension.
- [OSSystemExtensionRequest.ReplacementAction.replace](ossystemextensionrequest/replacementaction/replace.md)
  An action that tells the manager to replace an existing system extension.
### Initializers
- [init?(rawValue: Int)](ossystemextensionrequest/replacementaction/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [func requestNeedsUserApproval(OSSystemExtensionRequest)](ossystemextensionrequestdelegate/requestneedsuserapproval(_:).md)
  Tells the delegate that the user must grant approval before the manager can activate the extension.
- [func request(OSSystemExtensionRequest, actionForReplacingExtension: OSSystemExtensionProperties, withExtension: OSSystemExtensionProperties) -> OSSystemExtensionRequest.ReplacementAction](ossystemextensionrequestdelegate/request(_:actionforreplacingextension:withextension:).md)
  Tells the delegate that the user has a different version of the extension installed on their system.
- [class OSSystemExtensionProperties](ossystemextensionproperties.md)
  Properties that identify a specific version of a system extension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/systemextensions/ossystemextensionrequest/replacementaction)*