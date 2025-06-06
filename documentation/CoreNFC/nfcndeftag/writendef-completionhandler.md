# writeNDEF(_:completionHandler:)

**Framework**: Core NFC  
**Kind**: method  
**Required**: Yes

Saves an NDEF message to a writable tag.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+

## Declaration

```swift
func writeNDEF(_ ndefMessage: NFCNDEFMessage) async throws
```

#### Discussion

To determine whether the tag is writable, call [`queryNDEFStatus(completionHandler:)`](nfcndeftag/queryndefstatus(completionhandler:).md) and check that the `status` is [`NFCNDEFStatus.readWrite`](nfcndefstatus/readwrite.md).

## Parameters

- `ndefMessage`: The NDEF message to write to the tag.
- `completionHandler`: The handler has the following parameter:

## See Also

- [func writeLock(completionHandler: ((any Error)?) -> Void)](nfcndeftag/writelock(completionhandler:).md)
  Changes the NDEF tag status to read-only, preventing future write operations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfcndeftag/writendef(_:completionhandler:))*