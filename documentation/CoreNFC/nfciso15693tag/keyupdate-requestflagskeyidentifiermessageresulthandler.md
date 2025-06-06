# keyUpdate(requestFlags:keyIdentifier:message:resultHandler:)

**Framework**: Core NFC  
**Kind**: method

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst ?+

## Declaration

```swift
func keyUpdate(requestFlags flags: NFCISO15693RequestFlag, keyIdentifier: Int, message: Data, resultHandler: @escaping (Result<(NFCISO15693ResponseFlag, Data), any Error>) -> Void)
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfciso15693tag/keyupdate(requestflags:keyidentifier:message:resulthandler:))*