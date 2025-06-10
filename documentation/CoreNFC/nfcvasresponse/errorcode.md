# NFCVASResponse.ErrorCode

**Framework**: Core NFC  
**Kind**: enum

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+

## Declaration

```swift
enum ErrorCode
```

## Topics

### Enumeration Cases
- [NFCVASResponse.ErrorCode.dataNotActivated](nfcvasresponse/errorcode/datanotactivated.md)
- [NFCVASResponse.ErrorCode.dataNotFound](nfcvasresponse/errorcode/datanotfound.md)
- [NFCVASResponse.ErrorCode.incorrectData](nfcvasresponse/errorcode/incorrectdata.md)
- [NFCVASResponse.ErrorCode.success](nfcvasresponse/errorcode/success.md)
- [NFCVASResponse.ErrorCode.unsupportedApplicationVersion](nfcvasresponse/errorcode/unsupportedapplicationversion.md)
- [NFCVASResponse.ErrorCode.userIntervention](nfcvasresponse/errorcode/userintervention.md)
- [NFCVASResponse.ErrorCode.wrongLCField](nfcvasresponse/errorcode/wronglcfield.md)
- [NFCVASResponse.ErrorCode.wrongParameters](nfcvasresponse/errorcode/wrongparameters.md)
### Initializers
- [init?(rawValue: Int)](nfcvasresponse/errorcode/init(rawvalue:).md)
### Type Properties
- [static var VASErrorCodeDataNotActivated: NFCVASResponse.ErrorCode](nfcvasresponse/errorcode/vaserrorcodedatanotactivated.md)
  A constant indicating that the data isn’t activated.
- [static var VASErrorCodeDataNotFound: NFCVASResponse.ErrorCode](nfcvasresponse/errorcode/vaserrorcodedatanotfound.md)
  A constant indicating that data wasn’t found.
- [static var VASErrorCodeIncorrectData: NFCVASResponse.ErrorCode](nfcvasresponse/errorcode/vaserrorcodeincorrectdata.md)
  A constant indicating that the data is incorrect.
- [static var VASErrorCodeSuccess: NFCVASResponse.ErrorCode](nfcvasresponse/errorcode/vaserrorcodesuccess.md)
  A constant indicating that the `GET VAS DATA` command was successful.
- [static var VASErrorCodeUnsupportedApplicationVersion: NFCVASResponse.ErrorCode](nfcvasresponse/errorcode/vaserrorcodeunsupportedapplicationversion.md)
  A constant indicating an unsupported application version.
- [static var VASErrorCodeUserIntervention: NFCVASResponse.ErrorCode](nfcvasresponse/errorcode/vaserrorcodeuserintervention.md)
  A constant indicating that the tag requires user intervention.
- [static var VASErrorCodeWrongLCField: NFCVASResponse.ErrorCode](nfcvasresponse/errorcode/vaserrorcodewronglcfield.md)
  A constant indicating that the value in the Length Count field is wrong.
- [static var VASErrorCodeWrongParameters: NFCVASResponse.ErrorCode](nfcvasresponse/errorcode/vaserrorcodewrongparameters.md)
  A constant indicating that VAS command parameters are wrong.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [enum NFCFeliCaEncryptionId](nfcfelicaencryptionid.md)
- [enum NFCFeliCaPollingRequestCode](nfcfelicapollingrequestcode.md)
- [enum NFCFeliCaPollingTimeSlot](nfcfelicapollingtimeslot.md)
- [struct NFCISO15693RequestFlag](nfciso15693requestflag.md)
- [struct NFCISO15693ResponseFlag](nfciso15693responseflag.md)
- [NFCVASCommandConfiguration.Mode](nfcvascommandconfiguration/mode-swift.enum.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfcvasresponse/errorcode)*