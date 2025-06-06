# writeWithoutEncryption(serviceCodeList:blockList:blockData:completionHandler:)

**Framework**: Core NFC  
**Kind**: method  
**Required**: Yes

Sends the Write Without Encryption command, as defined by the FeliCa card specification, to the tag.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+

## Declaration

```swift
func writeWithoutEncryption(serviceCodeList: [Data], blockList: [Data], blockData: [Data]) async throws -> (Int, Int)
```

## See Also

- [func readWithoutEncryption(serviceCodeList: [Data], blockList: [Data], completionHandler: (Int, Int, [Data], (any Error)?) -> Void)](nfcfelicatag/readwithoutencryption(servicecodelist:blocklist:completionhandler:).md)
  Sends the Read Without Encryption command, as defined by the FeliCa card specification, to the tag.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfcfelicatag/writewithoutencryption(servicecodelist:blocklist:blockdata:completionhandler:))*