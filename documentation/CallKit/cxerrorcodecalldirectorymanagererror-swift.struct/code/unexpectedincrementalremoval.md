# CXErrorCodeCallDirectoryManagerError.Code.unexpectedIncrementalRemoval

**Framework**: CallKit  
**Kind**: case  
**Role**: Case

A request occurred before confirming incremental loading.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
case unexpectedIncrementalRemoval
```

```c
CXErrorCodeCallDirectoryManagerErrorUnexpectedIncrementalRemoval
```

## See Also

### Constants
- [CXErrorCodeCallDirectoryManagerError.Code.unknown](./unknown.md)
  An unknown error occurred.
- [CXErrorCodeCallDirectoryManagerError.Code.noExtensionFound](./noextensionfound.md)
  The call directory manager could not find a corresponding app extension.
- [CXErrorCodeCallDirectoryManagerError.Code.currentlyLoading](./currentlyloading.md)
  The call directory manager is loading the app extension.
- [CXErrorCodeCallDirectoryManagerError.Code.loadingInterrupted](./loadinginterrupted.md)
  The call directory manager was interrupted while loading the app extension.
- [CXErrorCodeCallDirectoryManagerError.Code.entriesOutOfOrder](./entriesoutoforder.md)
  The entries in the call directory are out of order.
- [CXErrorCodeCallDirectoryManagerError.Code.duplicateEntries](./duplicateentries.md)
  There are duplicate entries in the call directory.
- [CXErrorCodeCallDirectoryManagerError.Code.maximumEntriesExceeded](./maximumentriesexceeded.md)
  There are too many entries in the call directory.
- [CXErrorCodeCallDirectoryManagerError.Code.extensionDisabled](./extensiondisabled.md)
  The call directory extension isn’t enabled by the system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/callkit/cxerrorcodecalldirectorymanagererror-swift.struct/code/unexpectedincrementalremoval)*