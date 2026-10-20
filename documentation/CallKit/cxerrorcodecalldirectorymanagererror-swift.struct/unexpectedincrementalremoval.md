# unexpectedIncrementalRemoval

**Framework**: CallKit  
**Kind**: property  
**Role**: Type Property

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

### Constants
- [static var unknown: CXErrorCodeCallDirectoryManagerError.Code](./unknown.md)
  An unknown error occurred.
- [static var noExtensionFound: CXErrorCodeCallDirectoryManagerError.Code](./noextensionfound.md)
  The call directory manager can’t find a corresponding app extension.
- [static var currentlyLoading: CXErrorCodeCallDirectoryManagerError.Code](./currentlyloading.md)
  The call directory manager is loading the app extension.
- [static var loadingInterrupted: CXErrorCodeCallDirectoryManagerError.Code](./loadinginterrupted.md)
  The system interrupted the call directory manager while loading the app extension.
- [static var entriesOutOfOrder: CXErrorCodeCallDirectoryManagerError.Code](./entriesoutoforder.md)
  The entries in the call directory are out of order.
- [static var duplicateEntries: CXErrorCodeCallDirectoryManagerError.Code](./duplicateentries.md)
  There are duplicate entries in the call directory.
- [static var maximumEntriesExceeded: CXErrorCodeCallDirectoryManagerError.Code](./maximumentriesexceeded.md)
  There are too many entries in the call directory.
- [static var extensionDisabled: CXErrorCodeCallDirectoryManagerError.Code](./extensiondisabled.md)
  The call directory extension isn’t in an enabled state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/callkit/cxerrorcodecalldirectorymanagererror-swift.struct/unexpectedincrementalremoval)*