# CXErrorCodeCallDirectoryManagerError.Code.noExtensionFound

**Framework**: CallKit  
**Kind**: case  
**Role**: Case

The call directory manager could not find a corresponding app extension.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 10.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
case noExtensionFound
```

```c
CXErrorCodeCallDirectoryManagerErrorNoExtensionFound
```

## See Also

### Constants
- [CXErrorCodeCallDirectoryManagerError.Code.unknown](./unknown.md)
  An unknown error occurred.
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
- [CXErrorCodeCallDirectoryManagerError.Code.unexpectedIncrementalRemoval](./unexpectedincrementalremoval.md)
  A request occurred before confirming incremental loading.


---

*[View on Apple Developer](https://developer.apple.com/documentation/callkit/cxerrorcodecalldirectorymanagererror-swift.struct/code/noextensionfound)*