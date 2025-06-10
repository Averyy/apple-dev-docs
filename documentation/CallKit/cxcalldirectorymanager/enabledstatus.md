# CXCallDirectoryManager.EnabledStatus

**Framework**: CallKit  
**Kind**: enum

The enabled status of a Call Directory app extension, as reported by the [`getEnabledStatusForExtension(withIdentifier:completionHandler:)`](cxcalldirectorymanager/getenabledstatusforextension(withidentifier:completionhandler:).md) method.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 10.0+
- visionOS 1.0+

## Declaration

```swift
enum EnabledStatus
```

## Topics

### Constants
- [CXCallDirectoryManager.EnabledStatus.unknown](cxcalldirectorymanager/enabledstatus/unknown.md)
  Indicates that the enabled status for the extension is unknown.
- [CXCallDirectoryManager.EnabledStatus.disabled](cxcalldirectorymanager/enabledstatus/disabled.md)
  Indicates that the extension is disabled.
- [CXCallDirectoryManager.EnabledStatus.enabled](cxcalldirectorymanager/enabledstatus/enabled.md)
  Indicates that the extension is enabled.
### Initializers
- [init?(rawValue: Int)](cxcalldirectorymanager/enabledstatus/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func getEnabledStatusForExtension(withIdentifier: String, completionHandler: (CXCallDirectoryManager.EnabledStatus, (any Error)?) -> Void)](cxcalldirectorymanager/getenabledstatusforextension(withidentifier:completionhandler:).md)
  Asynchronously returns the enabled status of the extension with the specified identifier.
- [func reloadExtension(withIdentifier: String, completionHandler: (((any Error)?) -> Void)?)](cxcalldirectorymanager/reloadextension(withidentifier:completionhandler:).md)
  Asynchronously reloads the extension with the specified identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/callkit/cxcalldirectorymanager/enabledstatus)*