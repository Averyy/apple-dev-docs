# mismatchedClientState

**Framework**: Core Spotlight  
**Kind**: property

The provided client state did not match the information in the index.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
static var mismatchedClientState: CSIndexError.Code { get }
```

## See Also

- [static var indexUnavailableError: CSIndexError.Code](csindexerror/indexunavailableerror.md)
  The indexer is unavailable.
- [static var indexingUnsupported: CSIndexError.Code](csindexerror/indexingunsupported.md)
  Indexing isn’t supported on the device.
- [static var invalidClientStateError: CSIndexError.Code](csindexerror/invalidclientstateerror.md)
  The provided client state data is invalid.
- [static var invalidItemError: CSIndexError.Code](csindexerror/invaliditemerror.md)
  The searchable item object is invalid.
- [static var quotaExceeded: CSIndexError.Code](csindexerror/quotaexceeded.md)
  The quota for the bundle has been exceeded.
- [static var remoteConnectionError: CSIndexError.Code](csindexerror/remoteconnectionerror.md)
  An error occurred while communicating with the remote process.
- [static var unknownError: CSIndexError.Code](csindexerror/unknownerror.md)
  An unknown error occurred.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/csindexerror/mismatchedclientstate)*