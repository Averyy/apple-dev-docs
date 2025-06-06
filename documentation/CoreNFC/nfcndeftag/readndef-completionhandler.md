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

- `completionHandler`: The session calls   on the dispatch queue provided when creating the  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfcndeftag/readndef(completionhandler:))*