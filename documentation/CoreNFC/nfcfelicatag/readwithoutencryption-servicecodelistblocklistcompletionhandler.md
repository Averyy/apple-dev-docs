# readWithoutEncryption(serviceCodeList:blockList:completionHandler:)

**Framework**: Core NFC  
**Kind**: method  
**Required**: Yes

Sends the Read Without Encryption command, as defined by the FeliCa card specification, to the tag.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+

## Declaration

```swift
func readWithoutEncryption(serviceCodeList: [Data], blockList: [Data]) async throws -> (Int, Int, [Data])
```

## See Also

- [func writeWithoutEncryption(serviceCodeList: [Data], blockList: [Data], blockData: [Data], completionHandler: (Int, Int, (any Error)?) -> Void)](nfcfelicatag/writewithoutencryption(servicecodelist:blocklist:blockdata:completionhandler:).md)
  Sends the Write Without Encryption command, as defined by the FeliCa card specification, to the tag.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfcfelicatag/readwithoutencryption(servicecodelist:blocklist:completionhandler:))*