# select(requestFlags:completionHandler:)

**Framework**: Core NFC  
**Kind**: method  
**Required**: Yes

Sends the Select command (0x25 command code), as defined in the ISO 15693-3 specification, to the tag.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+

## Declaration

```swift
func select(requestFlags flags: NFCISO15693RequestFlag) async throws
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfciso15693tag/select(requestflags:completionhandler:))*