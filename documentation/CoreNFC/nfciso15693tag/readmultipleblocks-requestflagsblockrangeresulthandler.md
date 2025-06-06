# readMultipleBlocks(requestFlags:blockRange:resultHandler:)

**Framework**: Core NFC  
**Kind**: method

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst ?+

## Declaration

```swift
func readMultipleBlocks(requestFlags flags: NFCISO15693RequestFlag, blockRange: NSRange, resultHandler: @escaping (Result<[Data], any Error>) -> Void)
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfciso15693tag/readmultipleblocks(requestflags:blockrange:resulthandler:))*