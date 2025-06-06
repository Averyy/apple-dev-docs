# sendRequest(requestFlags:commandCode:data:)

**Framework**: Core NFC  
**Kind**: method

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst ?+

## Declaration

```swift
func sendRequest(requestFlags flags: Int, commandCode: Int, data: Data?) async throws -> (NFCISO15693ResponseFlag, Data?)
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfciso15693tag/sendrequest(requestflags:commandcode:data:))*