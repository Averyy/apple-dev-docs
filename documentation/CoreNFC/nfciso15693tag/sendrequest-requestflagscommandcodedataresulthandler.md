# sendRequest(requestFlags:commandCode:data:resultHandler:)

**Framework**: Core NFC  
**Kind**: method

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst ?+

## Declaration

```swift
func sendRequest(requestFlags flags: Int, commandCode: Int, data: Data?, resultHandler: @escaping (Result<(NFCISO15693ResponseFlag, Data?), any Error>) -> Void)
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfciso15693tag/sendrequest(requestflags:commandcode:data:resulthandler:))*