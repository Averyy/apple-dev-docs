# EncryptionId

**Framework**: Core NFC  
**Kind**: typealias

Encryption identifiers indicating the type of encryption algorithm used in the response of a Request Service V2 command.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+

## Declaration

```swift
typealias EncryptionId = NFCFeliCaEncryptionId
```

## Topics

### Identifiers
- [static var aes: NFCFeliCaEncryptionId](nfcfelicaencryptionid/aes-swift.type.property.md)
  An identifier that indicates the Advanced Encryption Standard (AES) encryption algorithm.
- [static var aes_des: NFCFeliCaEncryptionId](nfcfelicaencryptionid/aes_des-swift.type.property.md)
  An identifier that indicates the Data Encryption Standard (DES) encryption algorithm.

## See Also

- [func requestService(nodeCodeList: [Data], completionHandler: ([Data], (any Error)?) -> Void)](nfcfelicatag/requestservice(nodecodelist:completionhandler:).md)
  Sends the Request Service command, as defined by the FeliCa card specification, to the tag.
- [func requestServiceV2(nodeCodeList: [Data], completionHandler: (Int, Int, NFCFeliCaEncryptionId, [Data], [Data], (any Error)?) -> Void)](nfcfelicatag/requestservicev2(nodecodelist:completionhandler:).md)
  Sends the Request Service V2 command, as defined by the FeliCa card specification, to the tag.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/encryptionid)*