# NFCVASCommandConfiguration.Mode

**Framework**: Core NFC  
**Kind**: enum  
**Role**: Enumeration

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+

## Declaration

```swift
enum Mode
```

```c
enum NFCVASMode : NSInteger;
```

## Topics

### Enumeration Cases
- [NFCVASCommandConfiguration.Mode.normal](./mode-swift.enum/normal.md)
- [NFCVASCommandConfiguration.Mode.urlOnly](./mode-swift.enum/urlonly.md)
### Initializers
- [init?(rawValue: Int)](./mode-swift.enum/init%28rawvalue%29.md)
### Type Properties
- [static var VASModeNormal: NFCVASCommandConfiguration.Mode](./mode-swift.enum/vasmodenormal.md)
  A constant that indicates the Full VAS Protocol mode.
- [static var VASModeURLOnly: NFCVASCommandConfiguration.Mode](./mode-swift.enum/vasmodeurlonly.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Enumerations
- [enum NFCFeliCaEncryptionId](../nfcfelicaencryptionid.md)
- [enum NFCFeliCaPollingRequestCode](../nfcfelicapollingrequestcode.md)
- [enum NFCFeliCaPollingTimeSlot](../nfcfelicapollingtimeslot.md)
- [struct NFCISO15693RequestFlag](../nfciso15693requestflag.md)
- [struct NFCISO15693ResponseFlag](../nfciso15693responseflag.md)
- [NFCVASResponse.ErrorCode](../nfcvasresponse/errorcode.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfcvascommandconfiguration/mode-swift.enum)*