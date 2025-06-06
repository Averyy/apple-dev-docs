# requestServiceV2(nodeCodeList:completionHandler:)

**Framework**: Core NFC  
**Kind**: method  
**Required**: Yes

Sends the Request Service V2 command, as defined by the FeliCa card specification, to the tag.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+

## Declaration

```swift
func requestServiceV2(nodeCodeList: [Data]) async throws -> (Int, Int, NFCFeliCaEncryptionId, [Data], [Data])
```

## See Also

- [func requestService(nodeCodeList: [Data], completionHandler: ([Data], (any Error)?) -> Void)](nfcfelicatag/requestservice(nodecodelist:completionhandler:).md)
  Sends the Request Service command, as defined by the FeliCa card specification, to the tag.
- [typealias EncryptionId](encryptionid.md)
  Encryption identifiers indicating the type of encryption algorithm used in the response of a Request Service V2 command.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfcfelicatag/requestservicev2(nodecodelist:completionhandler:))*