# writeLock(completionHandler:)

**Framework**: Core NFC  
**Kind**: method  
**Required**: Yes

Changes the NDEF tag status to read-only, preventing future write operations.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+

## Declaration

```swift
func writeLock() async throws
```

#### Discussion

Calling this method updates the write access condition byte in the NDEF File Control of the tag’s file system, thus locking the tag. This is a permanent action that you cannot undo. After locking the tag, you can no longer write data to it.

## Parameters

- `completionHandler`: The handler invoked by the reader session after completing the lock request. The session calls `completionHandler` on the dispatch queue provided when creating the [`NFCNDEFReaderSession`](nfcndefreadersession.md). The handler has the following parameter: - **error**: An [`NSError`](https://developer.apple.com/documentation/Foundation/NSError) object if the write request fails. A value of `nil` indicates that the session locked the tag and future write requests aren’t possible.

## See Also

- [func writeNDEF(NFCNDEFMessage, completionHandler: ((any Error)?) -> Void)](nfcndeftag/writendef(_:completionhandler:).md)
  Saves an NDEF message to a writable tag.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfcndeftag/writelock(completionhandler:))*