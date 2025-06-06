# CXErrorCodeCallDirectoryManagerError.Code

**Framework**: CallKit  
**Kind**: enum

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

## Topics

### Constants
- [CXErrorCodeCallDirectoryManagerError.Code.unknown](cxerrorcodecalldirectorymanagererror-swift.struct/code/unknown.md)
  An unknown error occurred.
- [CXErrorCodeCallDirectoryManagerError.Code.noExtensionFound](cxerrorcodecalldirectorymanagererror-swift.struct/code/noextensionfound.md)
  The call directory manager could not find a corresponding app extension.
- [CXErrorCodeCallDirectoryManagerError.Code.currentlyLoading](cxerrorcodecalldirectorymanagererror-swift.struct/code/currentlyloading.md)
  The call directory manager is loading the app extension.
- [CXErrorCodeCallDirectoryManagerError.Code.loadingInterrupted](cxerrorcodecalldirectorymanagererror-swift.struct/code/loadinginterrupted.md)
  The call directory manager was interrupted while loading the app extension.
- [CXErrorCodeCallDirectoryManagerError.Code.entriesOutOfOrder](cxerrorcodecalldirectorymanagererror-swift.struct/code/entriesoutoforder.md)
  The entries in the call directory are out of order.
- [CXErrorCodeCallDirectoryManagerError.Code.duplicateEntries](cxerrorcodecalldirectorymanagererror-swift.struct/code/duplicateentries.md)
  There are duplicate entries in the call directory.
- [CXErrorCodeCallDirectoryManagerError.Code.maximumEntriesExceeded](cxerrorcodecalldirectorymanagererror-swift.struct/code/maximumentriesexceeded.md)
  There are too many entries in the call directory.
- [CXErrorCodeCallDirectoryManagerError.Code.extensionDisabled](cxerrorcodecalldirectorymanagererror-swift.struct/code/extensiondisabled.md)
  The call directory extension isn’t enabled by the system.
- [CXErrorCodeCallDirectoryManagerError.Code.unexpectedIncrementalRemoval](cxerrorcodecalldirectorymanagererror-swift.struct/code/unexpectedincrementalremoval.md)
  A request occurred before confirming incremental loading.
### Initializers
- [init?(rawValue: Int)](cxerrorcodecalldirectorymanagererror-swift.struct/code/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [CXCallDirectoryManager.EnabledStatus](cxcalldirectorymanager/enabledstatus.md)
  The enabled status of a Call Directory app extension, as reported by the [`getEnabledStatusForExtension(withIdentifier:completionHandler:)`](cxcalldirectorymanager/getenabledstatusforextension(withidentifier:completionhandler:).md) method.
- [struct CXErrorCodeCallDirectoryManagerError](cxerrorcodecalldirectorymanagererror-swift.struct.md)
  Errors when interacting with a call directory manager.
- [let CXErrorDomainCallDirectoryManager: String](cxerrordomaincalldirectorymanager.md)
  Domain for errors when interacting with a call directory manager.


---

*[View on Apple Developer](https://developer.apple.com/documentation/callkit/cxerrorcodecalldirectorymanagererror-swift.struct/code)*