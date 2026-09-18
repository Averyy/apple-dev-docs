# writeWithoutEncryption(serviceCodeList:blockList:blockData:resultHandler:)

**Framework**: Core NFC  
**Kind**: method

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
@preconcurrency
func writeWithoutEncryption(serviceCodeList: [Data], blockList: [Data], blockData: [Data], resultHandler: @escaping @Sendable (Result<NFCFeliCaStatusFlag, any Error>) -> Void)
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfcfelicatag/writewithoutencryption(servicecodelist:blocklist:blockdata:resulthandler:))*