# VASErrorCode

**Framework**: Core NFC  
**Kind**: typealias

Constants representing APDU status codes for a VAS response.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+

## Declaration

```swift
typealias VASErrorCode = NFCVASResponse.ErrorCode
```

## Topics

### Status Codes
- [static var VASErrorCodeSuccess: NFCVASResponse.ErrorCode](nfcvasresponse/errorcode/vaserrorcodesuccess.md)
  A constant indicating that the `GET VAS DATA` command was successful.
- [static var VASErrorCodeUserIntervention: NFCVASResponse.ErrorCode](nfcvasresponse/errorcode/vaserrorcodeuserintervention.md)
  A constant indicating that the tag requires user intervention.
### Data Codes
- [static var VASErrorCodeDataNotActivated: NFCVASResponse.ErrorCode](nfcvasresponse/errorcode/vaserrorcodedatanotactivated.md)
  A constant indicating that the data isn’t activated.
- [static var VASErrorCodeDataNotFound: NFCVASResponse.ErrorCode](nfcvasresponse/errorcode/vaserrorcodedatanotfound.md)
  A constant indicating that data wasn’t found.
- [static var VASErrorCodeIncorrectData: NFCVASResponse.ErrorCode](nfcvasresponse/errorcode/vaserrorcodeincorrectdata.md)
  A constant indicating that the data is incorrect.
### Error Codes
- [static var VASErrorCodeUnsupportedApplicationVersion: NFCVASResponse.ErrorCode](nfcvasresponse/errorcode/vaserrorcodeunsupportedapplicationversion.md)
  A constant indicating an unsupported application version.
- [static var VASErrorCodeWrongLCField: NFCVASResponse.ErrorCode](nfcvasresponse/errorcode/vaserrorcodewronglcfield.md)
  A constant indicating that the value in the Length Count field is wrong.
- [static var VASErrorCodeWrongParameters: NFCVASResponse.ErrorCode](nfcvasresponse/errorcode/vaserrorcodewrongparameters.md)
  A constant indicating that VAS command parameters are wrong.

## See Also

- [var status: NFCVASResponse.ErrorCode](nfcvasresponse/status.md)
  A response APDU status code.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/vaserrorcode)*