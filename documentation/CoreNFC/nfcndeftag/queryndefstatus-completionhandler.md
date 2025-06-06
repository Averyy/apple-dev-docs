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

- `completionHandler`: The session calls   on the dispatch queue provided when creating the  .

## See Also

- [var isAvailable: Bool](nfcndeftag/isavailable.md)
  A Boolean value that determines whether the NDEF tag is available in the current reader session.
- [enum NFCNDEFStatus](nfcndefstatus.md)
  Constants that indicate status for an NDEF tag.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfcndeftag/queryndefstatus(completionhandler:))*