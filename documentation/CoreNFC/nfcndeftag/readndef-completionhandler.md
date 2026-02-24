# readNDEF(completionHandler:)

**Framework**: Core NFC  
**Kind**: method  
**Required**: Yes

Retrieves an NDEF message from the tag.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+

## Declaration

```swift
func readNDEF() async throws -> NFCNDEFMessage
```

## Parameters

- `completionHandler`: The handler invoked by the reader session that provides the NDEF message. The handler has the following parameters: - **message**: An [`NFCNDEFMessage`](nfcndefmessage.md) object, or `nil` if an error occurs while retrieving the message.
- **error**: An [`NSError`](https://developer.apple.com/documentation/Foundation/NSError) object if the read request fails; otherwise, `nil`. The session calls `completionHandler` on the dispatch queue provided when creating the [`NFCNDEFReaderSession`](nfcndefreadersession.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfcndeftag/readndef(completionhandler:))*