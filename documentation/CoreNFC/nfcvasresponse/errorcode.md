# NFCVASResponse.ErrorCode

**Framework**: Core NFC  
**Kind**: enum  
**Role**: Enumeration

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+

## Declaration

```swift
enum ErrorCode
```

```c
enum NFCVASErrorCode : NSInteger;
```

## Topics

### Enumeration Cases
- [NFCVASResponse.ErrorCode.dataNotActivated](./errorcode/datanotactivated.md)
- [NFCVASResponse.ErrorCode.dataNotFound](./errorcode/datanotfound.md)
- [NFCVASResponse.ErrorCode.incorrectData](./errorcode/incorrectdata.md)
- [NFCVASResponse.ErrorCode.success](./errorcode/success.md)
- [NFCVASResponse.ErrorCode.unsupportedApplicationVersion](./errorcode/unsupportedapplicationversion.md)
- [NFCVASResponse.ErrorCode.userIntervention](./errorcode/userintervention.md)
- [NFCVASResponse.ErrorCode.wrongLCField](./errorcode/wronglcfield.md)
- [NFCVASResponse.ErrorCode.wrongParameters](./errorcode/wrongparameters.md)
### Initializers
- [init?(rawValue: Int)](./errorcode/init%28rawvalue%29.md)
### Type Properties
- [static var VASErrorCodeDataNotActivated: NFCVASResponse.ErrorCode](./errorcode/vaserrorcodedatanotactivated.md)
  A constant indicating that the data isn’t activated.
- [static var VASErrorCodeDataNotFound: NFCVASResponse.ErrorCode](./errorcode/vaserrorcodedatanotfound.md)
  A constant indicating that data wasn’t found.
- [static var VASErrorCodeIncorrectData: NFCVASResponse.ErrorCode](./errorcode/vaserrorcodeincorrectdata.md)
  A constant indicating that the data is incorrect.
- [static var VASErrorCodeSuccess: NFCVASResponse.ErrorCode](./errorcode/vaserrorcodesuccess.md)
  A constant indicating that the `GET VAS DATA` command was successful.
- [static var VASErrorCodeUnsupportedApplicationVersion: NFCVASResponse.ErrorCode](./errorcode/vaserrorcodeunsupportedapplicationversion.md)
  A constant indicating an unsupported application version.
- [static var VASErrorCodeUserIntervention: NFCVASResponse.ErrorCode](./errorcode/vaserrorcodeuserintervention.md)
  A constant indicating that the tag requires user intervention.
- [static var VASErrorCodeWrongLCField: NFCVASResponse.ErrorCode](./errorcode/vaserrorcodewronglcfield.md)
  A constant indicating that the value in the Length Count field is wrong.
- [static var VASErrorCodeWrongParameters: NFCVASResponse.ErrorCode](./errorcode/vaserrorcodewrongparameters.md)
  A constant indicating that VAS command parameters are wrong.

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
- [NFCVASCommandConfiguration.Mode](../nfcvascommandconfiguration/mode-swift.enum.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfcvasresponse/errorcode)*