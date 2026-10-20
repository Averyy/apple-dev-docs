# NFCReaderError.Code

**Framework**: Core NFC  
**Kind**: enum  
**Role**: Enumeration

Reader session and tag error codes.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+

## Declaration

```swift
enum Code
```

```c
enum NFCReaderError : NSInteger;
```

## Topics

### Session Errors
- [NFCReaderError.Code.readerSessionInvalidationErrorFirstNDEFTagRead](./code/readersessioninvalidationerrorfirstndeftagread.md)
  The first NDEF tag read by this session is invalid.
- [NFCReaderError.Code.readerSessionInvalidationErrorSessionTerminatedUnexpectedly](./code/readersessioninvalidationerrorsessionterminatedunexpectedly.md)
  The reader session terminated unexpectedly.
- [NFCReaderError.Code.readerSessionInvalidationErrorSessionTimeout](./code/readersessioninvalidationerrorsessiontimeout.md)
  The reader session timed out.
- [NFCReaderError.Code.readerSessionInvalidationErrorSystemIsBusy](./code/readersessioninvalidationerrorsystemisbusy.md)
  The reader session failed because the system is busy.
- [NFCReaderError.Code.readerSessionInvalidationErrorUserCanceled](./code/readersessioninvalidationerrorusercanceled.md)
  The user canceled the reader session.
- [NFCReaderError.Code.readerSessionInvalidationErrorFirstNDEFTagRead](./code/readersessioninvalidationerrorfirstndeftagread.md)
  The first NDEF tag read by this session is invalid.
- [NFCReaderError.Code.readerSessionInvalidationErrorSessionTerminatedUnexpectedly](./code/readersessioninvalidationerrorsessionterminatedunexpectedly.md)
  The reader session terminated unexpectedly.
- [NFCReaderError.Code.readerSessionInvalidationErrorSessionTimeout](./code/readersessioninvalidationerrorsessiontimeout.md)
  The reader session timed out.
- [NFCReaderError.Code.readerSessionInvalidationErrorSystemIsBusy](./code/readersessioninvalidationerrorsystemisbusy.md)
  The reader session failed because the system is busy.
- [NFCReaderError.Code.readerSessionInvalidationErrorUserCanceled](./code/readersessioninvalidationerrorusercanceled.md)
  The user canceled the reader session.
### NDEF Tag Errors
- [NFCReaderError.Code.ndefReaderSessionErrorTagNotWritable](./code/ndefreadersessionerrortagnotwritable.md)
  The NDEF tag isn’t writable.
- [NFCReaderError.Code.ndefReaderSessionErrorTagSizeTooSmall](./code/ndefreadersessionerrortagsizetoosmall.md)
  The NDEF tag memory size is too small to store the data.
- [NFCReaderError.Code.ndefReaderSessionErrorTagUpdateFailure](./code/ndefreadersessionerrortagupdatefailure.md)
  The reader session failed to update the NDEF tag.
- [NFCReaderError.Code.ndefReaderSessionErrorZeroLengthMessage](./code/ndefreadersessionerrorzerolengthmessage.md)
  The NDEF tag doesn’t contain an NDEF message.
- [NFCReaderError.Code.ndefReaderSessionErrorTagNotWritable](./code/ndefreadersessionerrortagnotwritable.md)
  The NDEF tag isn’t writable.
- [NFCReaderError.Code.ndefReaderSessionErrorTagSizeTooSmall](./code/ndefreadersessionerrortagsizetoosmall.md)
  The NDEF tag memory size is too small to store the data.
- [NFCReaderError.Code.ndefReaderSessionErrorTagUpdateFailure](./code/ndefreadersessionerrortagupdatefailure.md)
  The reader session failed to update the NDEF tag.
- [NFCReaderError.Code.ndefReaderSessionErrorZeroLengthMessage](./code/ndefreadersessionerrorzerolengthmessage.md)
  The NDEF tag doesn’t contain an NDEF message.
### Transceive Errors
- [NFCReaderError.Code.readerTransceiveErrorRetryExceeded](./code/readertransceiveerrorretryexceeded.md)
  Too many retries have occurred.
- [NFCReaderError.Code.readerTransceiveErrorTagConnectionLost](./code/readertransceiveerrortagconnectionlost.md)
  The reader lost the connection to the tag.
- [NFCReaderError.Code.readerTransceiveErrorTagNotConnected](./code/readertransceiveerrortagnotconnected.md)
  The tag isn’t in the connected state.
- [NFCReaderError.Code.readerTransceiveErrorTagResponseError](./code/readertransceiveerrortagresponseerror.md)
  The tag has responded with an error.
- [NFCReaderError.Code.readerTransceiveErrorSessionInvalidated](./code/readertransceiveerrorsessioninvalidated.md)
  The reader session is invalid.
- [NFCReaderError.Code.readerTransceiveErrorPacketTooLong](./code/readertransceiveerrorpackettoolong.md)
  The packet length exceeds the limit supported by the tag.
- [NFCReaderError.Code.readerTransceiveErrorRetryExceeded](./code/readertransceiveerrorretryexceeded.md)
  Too many retries have occurred.
- [NFCReaderError.Code.readerTransceiveErrorTagConnectionLost](./code/readertransceiveerrortagconnectionlost.md)
  The reader lost the connection to the tag.
- [NFCReaderError.Code.readerTransceiveErrorTagNotConnected](./code/readertransceiveerrortagnotconnected.md)
  The tag isn’t in the connected state.
- [NFCReaderError.Code.readerTransceiveErrorTagResponseError](./code/readertransceiveerrortagresponseerror.md)
  The tag has responded with an error.
- [NFCReaderError.Code.readerTransceiveErrorSessionInvalidated](./code/readertransceiveerrorsessioninvalidated.md)
  The reader session is invalid.
- [NFCReaderError.Code.readerTransceiveErrorPacketTooLong](./code/readertransceiveerrorpackettoolong.md)
  The packet length exceeds the limit supported by the tag.
### Tag Command Configuration Error
- [NFCReaderError.Code.tagCommandConfigurationErrorInvalidParameters](./code/tagcommandconfigurationerrorinvalidparameters.md)
  The tag has been configured with invalid parameters.
- [NFCReaderError.Code.tagCommandConfigurationErrorInvalidParameters](./code/tagcommandconfigurationerrorinvalidparameters.md)
  The tag has been configured with invalid parameters.
### Other Errors
- [NFCReaderError.Code.readerErrorUnsupportedFeature](./code/readererrorunsupportedfeature.md)
  The reader session does not support this feature.
- [NFCReaderError.Code.readerErrorInvalidParameter](./code/readererrorinvalidparameter.md)
  An input parameter is invalid.
- [NFCReaderError.Code.readerErrorInvalidParameterLength](./code/readererrorinvalidparameterlength.md)
  The length of an input parameter is invalid.
- [NFCReaderError.Code.readerErrorParameterOutOfBound](./code/readererrorparameteroutofbound.md)
  A parameter value is outside of the acceptable boundary.
- [NFCReaderError.Code.readerErrorRadioDisabled](./code/readererrorradiodisabled.md)
  The NFC wireless radio on the device is disabled.
- [NFCReaderError.Code.readerErrorSecurityViolation](./code/readererrorsecurityviolation.md)
  A security violation associated with the reader session has occurred.
- [NFCReaderError.Code.readerErrorUnsupportedFeature](./code/readererrorunsupportedfeature.md)
  The reader session does not support this feature.
- [NFCReaderError.Code.readerErrorInvalidParameter](./code/readererrorinvalidparameter.md)
  An input parameter is invalid.
- [NFCReaderError.Code.readerErrorInvalidParameterLength](./code/readererrorinvalidparameterlength.md)
  The length of an input parameter is invalid.
- [NFCReaderError.Code.readerErrorParameterOutOfBound](./code/readererrorparameteroutofbound.md)
  A parameter value is outside of the acceptable boundary.
- [NFCReaderError.Code.readerErrorRadioDisabled](./code/readererrorradiodisabled.md)
  The NFC wireless radio on the device is disabled.
- [NFCReaderError.Code.readerErrorSecurityViolation](./code/readererrorsecurityviolation.md)
  A security violation associated with the reader session has occurred.
### Enumeration Cases
- [NFCReaderError.Code.paymentTagReaderSessionErrorLocationAuthorizationDenied](./code/paymenttagreadersessionerrorlocationauthorizationdenied.md)
- [NFCReaderError.Code.paymentTagReaderSessionErrorLocationServiceRestricted](./code/paymenttagreadersessionerrorlocationservicerestricted.md)
- [NFCReaderError.Code.paymentTagReaderSessionErrorOnDeviceLocationUnavailable](./code/paymenttagreadersessionerrorondevicelocationunavailable.md)
- [NFCReaderError.Code.readerErrorAccessNotAccepted](./code/readererroraccessnotaccepted.md)
- [NFCReaderError.Code.readerErrorIneligible](./code/readererrorineligible.md)
### Initializers
- [init?(rawValue: Int)](./code/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Errors
- [struct NFCReaderError](../nfcreadererror-swift.struct.md)
  An error type that indicates problems with reader sessions or tags.
- [let NFCErrorDomain: String](../nfcerrordomain.md)
  The domain for errors associated with Core NFC APIs.
- [let NFCTagResponseUnexpectedLengthErrorKey: String](../nfctagresponseunexpectedlengtherrorkey.md)
  A user-information dictionary key that indicates an invalid received response packet length.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfcreadererror-swift.struct/code)*