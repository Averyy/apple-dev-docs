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

- `completionHandler`: The handler has the following parameter:

## See Also

- [func writeNDEF(NFCNDEFMessage, completionHandler: ((any Error)?) -> Void)](nfcndeftag/writendef(_:completionhandler:).md)
  Saves an NDEF message to a writable tag.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfcndeftag/writelock(completionhandler:))*