# CXCallDirectoryManager.EnabledStatus

**Framework**: CallKit  
**Kind**: enum  
**Role**: Enumeration

The enabled status of a Call Directory app extension, as reported by the [`getEnabledStatusForExtension(withIdentifier:completionHandler:)`](./getenabledstatusforextension%28withidentifier,completionhandler%29.md) method.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 10.0+
- visionOS 1.0+

## Declaration

```swift
enum EnabledStatus
```

```c
enum CXCallDirectoryEnabledStatus : NSInteger;
```

## Topics

### Constants
- [CXCallDirectoryManager.EnabledStatus.unknown](./enabledstatus/unknown.md)
  Indicates that the enabled status for the extension is unknown.
- [CXCallDirectoryManager.EnabledStatus.disabled](./enabledstatus/disabled.md)
  Indicates that the extension is disabled.
- [CXCallDirectoryManager.EnabledStatus.enabled](./enabledstatus/enabled.md)
  Indicates that the extension is enabled.
### Initializers
- [init?(rawValue: Int)](./enabledstatus/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Working with a Call Directory App Extension
- [func getEnabledStatusForExtension(withIdentifier: String, completionHandler: (CXCallDirectoryManager.EnabledStatus, (any Error)?) -> Void)](./getenabledstatusforextension%28withidentifier,completionhandler%29.md)
  Asynchronously returns the enabled status of the extension with the specified identifier.
- [func reloadExtension(withIdentifier: String, completionHandler: (((any Error)?) -> Void)?)](./reloadextension%28withidentifier,completionhandler%29.md)
  Asynchronously reloads the extension with the specified identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/callkit/cxcalldirectorymanager/enabledstatus)*