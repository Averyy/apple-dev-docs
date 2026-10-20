# NFCFeliCaEncryptionId

**Framework**: Core NFC  
**Kind**: enum  
**Role**: Enumeration

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+

## Declaration

```swift
enum NFCFeliCaEncryptionId
```

```c
enum NFCFeliCaEncryptionId : NSInteger;
```

## Topics

### Enumeration Cases
- [NFCFeliCaEncryptionId.AES](./nfcfelicaencryptionid/aes-swift.enum.case.md)
- [NFCFeliCaEncryptionId.AES_DES](./nfcfelicaencryptionid/aes_des-swift.enum.case.md)
### Initializers
- [init?(rawValue: Int)](./nfcfelicaencryptionid/init%28rawvalue%29.md)
### Type Properties
- [static var aes: NFCFeliCaEncryptionId](./nfcfelicaencryptionid/aes-swift.type.property.md)
  An identifier that indicates the Advanced Encryption Standard (AES) encryption algorithm.
- [static var aes_des: NFCFeliCaEncryptionId](./nfcfelicaencryptionid/aes_des-swift.type.property.md)
  An identifier that indicates the Data Encryption Standard (DES) encryption algorithm.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Enumerations
- [enum NFCFeliCaPollingRequestCode](./nfcfelicapollingrequestcode.md)
- [enum NFCFeliCaPollingTimeSlot](./nfcfelicapollingtimeslot.md)
- [struct NFCISO15693RequestFlag](./nfciso15693requestflag.md)
- [struct NFCISO15693ResponseFlag](./nfciso15693responseflag.md)
- [NFCVASResponse.ErrorCode](./nfcvasresponse/errorcode.md)
- [NFCVASCommandConfiguration.Mode](./nfcvascommandconfiguration/mode-swift.enum.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfcfelicaencryptionid)*