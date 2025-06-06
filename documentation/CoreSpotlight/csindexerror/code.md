# CSIndexError.Code

**Framework**: Core Spotlight  
**Kind**: enum

Error codes that describe indexing-specific errors.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+

## Declaration

```swift
enum Code
```

## Topics

### Getting the indexing error codes
- [CSIndexError.Code.indexUnavailableError](csindexerror/code/indexunavailableerror.md)
  The indexer is unavailable.
- [CSIndexError.Code.indexingUnsupported](csindexerror/code/indexingunsupported.md)
  Indexing isn’t supported on the device.
- [CSIndexError.Code.invalidClientStateError](csindexerror/code/invalidclientstateerror.md)
  The provided client state data is invalid.
- [CSIndexError.Code.invalidItemError](csindexerror/code/invaliditemerror.md)
  The searchable item object is invalid.
- [CSIndexError.Code.mismatchedClientState](csindexerror/code/mismatchedclientstate.md)
  The provided client state did not match the information in the index.
- [CSIndexError.Code.quotaExceeded](csindexerror/code/quotaexceeded.md)
  The quota for the bundle has been exceeded.
- [CSIndexError.Code.remoteConnectionError](csindexerror/code/remoteconnectionerror.md)
  An error occurred while communicating with the remote process.
- [CSIndexError.Code.unknownError](csindexerror/code/unknownerror.md)
  An unknown error occurred.
### Initializers
- [init?(rawValue: Int)](csindexerror/code/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/csindexerror/code)*