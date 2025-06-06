# readWithoutEncryption(serviceCodeList:blockList:resultHandler:)

**Framework**: Core NFC  
**Kind**: method

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst ?+

## Declaration

```swift
func readWithoutEncryption(serviceCodeList: [Data], blockList: [Data], resultHandler: @escaping (Result<(NFCFeliCaStatusFlag, [Data]), any Error>) -> Void)
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfcfelicatag/readwithoutencryption(servicecodelist:blocklist:resulthandler:))*