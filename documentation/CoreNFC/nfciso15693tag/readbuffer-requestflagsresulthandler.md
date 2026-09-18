# readBuffer(requestFlags:resultHandler:)

**Framework**: Core NFC  
**Kind**: method

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
@preconcurrency
func readBuffer(requestFlags flags: NFCISO15693RequestFlag, resultHandler: @escaping @Sendable (Result<(NFCISO15693ResponseFlag, Data), any Error>) -> Void)
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfciso15693tag/readbuffer(requestflags:resulthandler:))*