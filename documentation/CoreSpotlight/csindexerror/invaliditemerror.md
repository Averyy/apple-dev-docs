# invalidItemError

**Framework**: Core Spotlight  
**Kind**: property  
**Role**: Type Property

The searchable item object is invalid.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+

## Declaration

```swift
static var invalidItemError: CSIndexError.Code { get }
```

#### Discussion

Verify the information in your [`CSSearchableItem`](../cssearchableitem.md) object is correct.

## See Also

### Getting the error codes
- [static var indexUnavailableError: CSIndexError.Code](./indexunavailableerror.md)
  The indexer is unavailable.
- [static var indexingUnsupported: CSIndexError.Code](./indexingunsupported.md)
  Indexing isn’t supported on the device.
- [static var invalidClientStateError: CSIndexError.Code](./invalidclientstateerror.md)
  The provided client state data is invalid.
- [static var mismatchedClientState: CSIndexError.Code](./mismatchedclientstate.md)
  The provided client state did not match the information in the index.
- [static var quotaExceeded: CSIndexError.Code](./quotaexceeded.md)
  The quota for the bundle has been exceeded.
- [static var remoteConnectionError: CSIndexError.Code](./remoteconnectionerror.md)
  An error occurred while communicating with the remote process.
- [static var unknownError: CSIndexError.Code](./unknownerror.md)
  An unknown error occurred.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/csindexerror/invaliditemerror)*