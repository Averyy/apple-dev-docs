# OSSystemExtensionRequest.ReplacementAction

**Framework**: System Extensions  
**Kind**: enum  
**Role**: Enumeration

Actions for describing how the extension manager should resolve a version conflict.

**Availability**:
- macOS 10.15+

## Declaration

```swift
enum ReplacementAction
```

```c
enum OSSystemExtensionReplacementAction : NSInteger;
```

## Topics

### Replacement Actions
- [OSSystemExtensionRequest.ReplacementAction.cancel](./replacementaction/cancel.md)
  An action that tells the manager to cancel replacement of a system extension.
- [OSSystemExtensionRequest.ReplacementAction.replace](./replacementaction/replace.md)
  An action that tells the manager to replace an existing system extension.
### Initializers
- [init?(rawValue: Int)](./replacementaction/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Handling Indeterminate Installs
- [func requestNeedsUserApproval(OSSystemExtensionRequest)](../ossystemextensionrequestdelegate/requestneedsuserapproval%28_%29.md)
  Tells the delegate that the user must grant approval before the manager can activate the extension.
- [func request(OSSystemExtensionRequest, actionForReplacingExtension: OSSystemExtensionProperties, withExtension: OSSystemExtensionProperties) -> OSSystemExtensionRequest.ReplacementAction](../ossystemextensionrequestdelegate/request%28_,actionforreplacingextension,withextension%29.md)
  Tells the delegate that the user has a different version of the extension installed on their system.
- [class OSSystemExtensionProperties](../ossystemextensionproperties.md)
  Properties that identify a specific version of a system extension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/systemextensions/ossystemextensionrequest/replacementaction)*