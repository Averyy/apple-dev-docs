# CSIndexError.Code

**Framework**: Core Spotlight  
**Kind**: enum  
**Role**: Enumeration

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

```c
enum CSIndexErrorCode : NSInteger;
```

## Topics

### Getting the indexing error codes
- [CSIndexError.Code.indexUnavailableError](./code/indexunavailableerror.md)
  The indexer is unavailable.
- [CSIndexError.Code.indexingUnsupported](./code/indexingunsupported.md)
  Indexing isn’t supported on the device.
- [CSIndexError.Code.invalidClientStateError](./code/invalidclientstateerror.md)
  The provided client state data is invalid.
- [CSIndexError.Code.invalidItemError](./code/invaliditemerror.md)
  The searchable item object is invalid.
- [CSIndexError.Code.mismatchedClientState](./code/mismatchedclientstate.md)
  The provided client state did not match the information in the index.
- [CSIndexError.Code.quotaExceeded](./code/quotaexceeded.md)
  The quota for the bundle has been exceeded.
- [CSIndexError.Code.remoteConnectionError](./code/remoteconnectionerror.md)
  An error occurred while communicating with the remote process.
- [CSIndexError.Code.unknownError](./code/unknownerror.md)
  An unknown error occurred.
### Initializers
- [init?(rawValue: Int)](./code/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/csindexerror/code)*