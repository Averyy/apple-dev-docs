# CXErrorCodeCallDirectoryManagerError.Code

**Framework**: CallKit  
**Kind**: enum  
**Role**: Enumeration

Error codes the CallKit framework returns.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 10.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
enum Code
```

```c
enum CXErrorCodeCallDirectoryManagerError : NSInteger;
```

## Topics

### Constants
- [CXErrorCodeCallDirectoryManagerError.Code.unknown](./code/unknown.md)
  An unknown error occurred.
- [CXErrorCodeCallDirectoryManagerError.Code.noExtensionFound](./code/noextensionfound.md)
  The call directory manager could not find a corresponding app extension.
- [CXErrorCodeCallDirectoryManagerError.Code.currentlyLoading](./code/currentlyloading.md)
  The call directory manager is loading the app extension.
- [CXErrorCodeCallDirectoryManagerError.Code.loadingInterrupted](./code/loadinginterrupted.md)
  The call directory manager was interrupted while loading the app extension.
- [CXErrorCodeCallDirectoryManagerError.Code.entriesOutOfOrder](./code/entriesoutoforder.md)
  The entries in the call directory are out of order.
- [CXErrorCodeCallDirectoryManagerError.Code.duplicateEntries](./code/duplicateentries.md)
  There are duplicate entries in the call directory.
- [CXErrorCodeCallDirectoryManagerError.Code.maximumEntriesExceeded](./code/maximumentriesexceeded.md)
  There are too many entries in the call directory.
- [CXErrorCodeCallDirectoryManagerError.Code.extensionDisabled](./code/extensiondisabled.md)
  The call directory extension isn’t enabled by the system.
- [CXErrorCodeCallDirectoryManagerError.Code.unexpectedIncrementalRemoval](./code/unexpectedincrementalremoval.md)
  A request occurred before confirming incremental loading.
### Initializers
- [init?(rawValue: Int)](./code/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Errors
- [CXCallDirectoryManager.EnabledStatus](../cxcalldirectorymanager/enabledstatus.md)
  The enabled status of a Call Directory app extension, as reported by the [`getEnabledStatusForExtension(withIdentifier:completionHandler:)`](../cxcalldirectorymanager/getenabledstatusforextension%28withidentifier,completionhandler%29.md) method.
- [struct CXErrorCodeCallDirectoryManagerError](../cxerrorcodecalldirectorymanagererror-swift.struct.md)
  Errors when interacting with a call directory manager.
- [let CXErrorDomainCallDirectoryManager: String](../cxerrordomaincalldirectorymanager.md)
  Domain for errors when interacting with a call directory manager.


---

*[View on Apple Developer](https://developer.apple.com/documentation/callkit/cxerrorcodecalldirectorymanagererror-swift.struct/code)*