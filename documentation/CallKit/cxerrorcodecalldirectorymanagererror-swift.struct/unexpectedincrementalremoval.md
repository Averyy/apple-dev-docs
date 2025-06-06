# unexpectedIncrementalRemoval

**Framework**: CallKit  
**Kind**: property

A request occurred before confirming incremental loading.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
static var unexpectedIncrementalRemoval: CXErrorCodeCallDirectoryManagerError.Code { get }
```

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/callkit/cxerrorcodecalldirectorymanagererror-swift.struct/unexpectedincrementalremoval)*