# CXErrorCodeCallDirectoryManagerError

**Framework**: CallKit  
**Kind**: struct

Errors when interacting with a call directory manager.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 10.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
struct CXErrorCodeCallDirectoryManagerError
```

## Topics

### Constants
- [static var unknown: CXErrorCodeCallDirectoryManagerError.Code](cxerrorcodecalldirectorymanagererror-swift.struct/unknown.md)
  An unknown error occurred.
- [static var noExtensionFound: CXErrorCodeCallDirectoryManagerError.Code](cxerrorcodecalldirectorymanagererror-swift.struct/noextensionfound.md)
  The call directory manager can’t find a corresponding app extension.
- [static var currentlyLoading: CXErrorCodeCallDirectoryManagerError.Code](cxerrorcodecalldirectorymanagererror-swift.struct/currentlyloading.md)
  The call directory manager is loading the app extension.
- [static var loadingInterrupted: CXErrorCodeCallDirectoryManagerError.Code](cxerrorcodecalldirectorymanagererror-swift.struct/loadinginterrupted.md)
  The system interrupted the call directory manager while loading the app extension.
- [static var entriesOutOfOrder: CXErrorCodeCallDirectoryManagerError.Code](cxerrorcodecalldirectorymanagererror-swift.struct/entriesoutoforder.md)
  The entries in the call directory are out of order.
- [static var duplicateEntries: CXErrorCodeCallDirectoryManagerError.Code](cxerrorcodecalldirectorymanagererror-swift.struct/duplicateentries.md)
  There are duplicate entries in the call directory.
- [static var maximumEntriesExceeded: CXErrorCodeCallDirectoryManagerError.Code](cxerrorcodecalldirectorymanagererror-swift.struct/maximumentriesexceeded.md)
  There are too many entries in the call directory.
- [static var extensionDisabled: CXErrorCodeCallDirectoryManagerError.Code](cxerrorcodecalldirectorymanagererror-swift.struct/extensiondisabled.md)
  The call directory extension isn’t in an enabled state.
- [static var unexpectedIncrementalRemoval: CXErrorCodeCallDirectoryManagerError.Code](cxerrorcodecalldirectorymanagererror-swift.struct/unexpectedincrementalremoval.md)
  A request occurred before confirming incremental loading.
### Enumerations
- [CXErrorCodeCallDirectoryManagerError.Code](cxerrorcodecalldirectorymanagererror-swift.struct/code.md)
  Error codes the CallKit framework returns.
### Type Properties
- [static var errorDomain: String](cxerrorcodecalldirectorymanagererror-swift.struct/errordomain.md)

## Relationships

### Conforms To
- [CustomNSError](../Foundation/CustomNSError.md)
- [Equatable](../Swift/Equatable.md)
- [Error](../Swift/Error.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [CXCallDirectoryManager.EnabledStatus](cxcalldirectorymanager/enabledstatus.md)
  The enabled status of a Call Directory app extension, as reported by the [`getEnabledStatusForExtension(withIdentifier:completionHandler:)`](cxcalldirectorymanager/getenabledstatusforextension(withidentifier:completionhandler:).md) method.
- [CXErrorCodeCallDirectoryManagerError.Code](cxerrorcodecalldirectorymanagererror-swift.struct/code.md)
  Error codes the CallKit framework returns.
- [let CXErrorDomainCallDirectoryManager: String](cxerrordomaincalldirectorymanager.md)
  Domain for errors when interacting with a call directory manager.


---

*[View on Apple Developer](https://developer.apple.com/documentation/callkit/cxerrorcodecalldirectorymanagererror-swift.struct)*