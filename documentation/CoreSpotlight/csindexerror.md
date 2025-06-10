# CSIndexError

**Framework**: Core Spotlight  
**Kind**: struct

Index errors returned by Core Spotlight.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+

## Declaration

```swift
struct CSIndexError
```

## Topics

### Getting the error codes
- [static var indexUnavailableError: CSIndexError.Code](csindexerror/indexunavailableerror.md)
  The indexer is unavailable.
- [static var indexingUnsupported: CSIndexError.Code](csindexerror/indexingunsupported.md)
  Indexing isn’t supported on the device.
- [static var invalidClientStateError: CSIndexError.Code](csindexerror/invalidclientstateerror.md)
  The provided client state data is invalid.
- [static var invalidItemError: CSIndexError.Code](csindexerror/invaliditemerror.md)
  The searchable item object is invalid.
- [static var mismatchedClientState: CSIndexError.Code](csindexerror/mismatchedclientstate.md)
  The provided client state did not match the information in the index.
- [static var quotaExceeded: CSIndexError.Code](csindexerror/quotaexceeded.md)
  The quota for the bundle has been exceeded.
- [static var remoteConnectionError: CSIndexError.Code](csindexerror/remoteconnectionerror.md)
  An error occurred while communicating with the remote process.
- [static var unknownError: CSIndexError.Code](csindexerror/unknownerror.md)
  An unknown error occurred.
### Getting codes for indexing errors
- [CSIndexError.Code](csindexerror/code.md)
  Error codes that describe indexing-specific errors.
### Getting the error description
- [static var errorDomain: String](csindexerror/errordomain.md)

## Relationships

### Conforms To
- [CustomNSError](../Foundation/CustomNSError.md)
- [Equatable](../Swift/Equatable.md)
- [Error](../Swift/Error.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct CSSearchQueryError](cssearchqueryerror.md)
  Search query errors returned by Core Spotlight.
- [CSIndex Errors](csindex-errors.md)
  Index error codes and error domain.
- [CSSearchQuery Errors](cssearchquery-errors.md)
  Search query error codes and error domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/csindexerror)*