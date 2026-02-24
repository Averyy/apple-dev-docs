# queryNDEFStatus(completionHandler:)

**Framework**: Core NFC  
**Kind**: method  
**Required**: Yes

Asks the reader session for the NDEF support status of the tag.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+

## Declaration

```swift
func queryNDEFStatus() async throws -> (NFCNDEFStatus, Int)
```

## Parameters

- `completionHandler`: The handler invoked by the reader session that provides the NDEF support status. The handler has the following parameters: - **status**: The [`NFCNDEFStatus`](nfcndefstatus.md) of the tag.
- **capacity**: Indicates the maximum NDEF message size, in bytes, that you can store on the tag.
- **error**: An [`NSError`](https://developer.apple.com/documentation/Foundation/NSError) object if the query fails; otherwise, `nil`. The session calls `completionHandler` on the dispatch queue provided when creating the [`NFCNDEFReaderSession`](nfcndefreadersession.md).

## See Also

- [var isAvailable: Bool](nfcndeftag/isavailable.md)
  A Boolean value that determines whether the NDEF tag is available in the current reader session.
- [enum NFCNDEFStatus](nfcndefstatus.md)
  Constants that indicate status for an NDEF tag.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfcndeftag/queryndefstatus(completionhandler:))*