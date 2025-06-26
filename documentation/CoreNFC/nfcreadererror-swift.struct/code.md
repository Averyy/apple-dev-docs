# NFCReaderError.Code

**Framework**: Core NFC  
**Kind**: enum

Reader session and tag error codes.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+

## Declaration

```swift
enum Code
```

## Topics

### Session Errors
- [NFCReaderError.Code.readerSessionInvalidationErrorFirstNDEFTagRead](nfcreadererror-swift.struct/code/readersessioninvalidationerrorfirstndeftagread.md)
  The first NDEF tag read by this session is invalid.
- [NFCReaderError.Code.readerSessionInvalidationErrorSessionTerminatedUnexpectedly](nfcreadererror-swift.struct/code/readersessioninvalidationerrorsessionterminatedunexpectedly.md)
  The reader session terminated unexpectedly.
- [NFCReaderError.Code.readerSessionInvalidationErrorSessionTimeout](nfcreadererror-swift.struct/code/readersessioninvalidationerrorsessiontimeout.md)
  The reader session timed out.
- [NFCReaderError.Code.readerSessionInvalidationErrorSystemIsBusy](nfcreadererror-swift.struct/code/readersessioninvalidationerrorsystemisbusy.md)
  The reader session failed because the system is busy.
- [NFCReaderError.Code.readerSessionInvalidationErrorUserCanceled](nfcreadererror-swift.struct/code/readersessioninvalidationerrorusercanceled.md)
  The user canceled the reader session.
- [NFCReaderError.Code.readerSessionInvalidationErrorFirstNDEFTagRead](nfcreadererror-swift.struct/code/readersessioninvalidationerrorfirstndeftagread.md)
  The first NDEF tag read by this session is invalid.
- [NFCReaderError.Code.readerSessionInvalidationErrorSessionTerminatedUnexpectedly](nfcreadererror-swift.struct/code/readersessioninvalidationerrorsessionterminatedunexpectedly.md)
  The reader session terminated unexpectedly.
- [NFCReaderError.Code.readerSessionInvalidationErrorSessionTimeout](nfcreadererror-swift.struct/code/readersessioninvalidationerrorsessiontimeout.md)
  The reader session timed out.
- [NFCReaderError.Code.readerSessionInvalidationErrorSystemIsBusy](nfcreadererror-swift.struct/code/readersessioninvalidationerrorsystemisbusy.md)
  The reader session failed because the system is busy.
- [NFCReaderError.Code.readerSessionInvalidationErrorUserCanceled](nfcreadererror-swift.struct/code/readersessioninvalidationerrorusercanceled.md)
  The user canceled the reader session.
### NDEF Tag Errors
- [NFCReaderError.Code.ndefReaderSessionErrorTagNotWritable](nfcreadererror-swift.struct/code/ndefreadersessionerrortagnotwritable.md)
  The NDEF tag isn’t writable.
- [NFCReaderError.Code.ndefReaderSessionErrorTagSizeTooSmall](nfcreadererror-swift.struct/code/ndefreadersessionerrortagsizetoosmall.md)
  The NDEF tag memory size is too small to store the data.
- [NFCReaderError.Code.ndefReaderSessionErrorTagUpdateFailure](nfcreadererror-swift.struct/code/ndefreadersessionerrortagupdatefailure.md)
  The reader session failed to update the NDEF tag.
- [NFCReaderError.Code.ndefReaderSessionErrorZeroLengthMessage](nfcreadererror-swift.struct/code/ndefreadersessionerrorzerolengthmessage.md)
  The NDEF tag doesn’t contain an NDEF message.
- [NFCReaderError.Code.ndefReaderSessionErrorTagNotWritable](nfcreadererror-swift.struct/code/ndefreadersessionerrortagnotwritable.md)
  The NDEF tag isn’t writable.
- [NFCReaderError.Code.ndefReaderSessionErrorTagSizeTooSmall](nfcreadererror-swift.struct/code/ndefreadersessionerrortagsizetoosmall.md)
  The NDEF tag memory size is too small to store the data.
- [NFCReaderError.Code.ndefReaderSessionErrorTagUpdateFailure](nfcreadererror-swift.struct/code/ndefreadersessionerrortagupdatefailure.md)
  The reader session failed to update the NDEF tag.
- [NFCReaderError.Code.ndefReaderSessionErrorZeroLengthMessage](nfcreadererror-swift.struct/code/ndefreadersessionerrorzerolengthmessage.md)
  The NDEF tag doesn’t contain an NDEF message.
### Transceive Errors
- [NFCReaderError.Code.readerTransceiveErrorRetryExceeded](nfcreadererror-swift.struct/code/readertransceiveerrorretryexceeded.md)
  Too many retries have occurred.
- [NFCReaderError.Code.readerTransceiveErrorTagConnectionLost](nfcreadererror-swift.struct/code/readertransceiveerrortagconnectionlost.md)
  The reader lost the connection to the tag.
- [NFCReaderError.Code.readerTransceiveErrorTagNotConnected](nfcreadererror-swift.struct/code/readertransceiveerrortagnotconnected.md)
  The tag isn’t in the connected state.
- [NFCReaderError.Code.readerTransceiveErrorTagResponseError](nfcreadererror-swift.struct/code/readertransceiveerrortagresponseerror.md)
  The tag has responded with an error.
- [NFCReaderError.Code.readerTransceiveErrorSessionInvalidated](nfcreadererror-swift.struct/code/readertransceiveerrorsessioninvalidated.md)
  The reader session is invalid.
- [NFCReaderError.Code.readerTransceiveErrorPacketTooLong](nfcreadererror-swift.struct/code/readertransceiveerrorpackettoolong.md)
  The packet length exceeds the limit supported by the tag.
- [NFCReaderError.Code.readerTransceiveErrorRetryExceeded](nfcreadererror-swift.struct/code/readertransceiveerrorretryexceeded.md)
  Too many retries have occurred.
- [NFCReaderError.Code.readerTransceiveErrorTagConnectionLost](nfcreadererror-swift.struct/code/readertransceiveerrortagconnectionlost.md)
  The reader lost the connection to the tag.
- [NFCReaderError.Code.readerTransceiveErrorTagNotConnected](nfcreadererror-swift.struct/code/readertransceiveerrortagnotconnected.md)
  The tag isn’t in the connected state.
- [NFCReaderError.Code.readerTransceiveErrorTagResponseError](nfcreadererror-swift.struct/code/readertransceiveerrortagresponseerror.md)
  The tag has responded with an error.
- [NFCReaderError.Code.readerTransceiveErrorSessionInvalidated](nfcreadererror-swift.struct/code/readertransceiveerrorsessioninvalidated.md)
  The reader session is invalid.
- [NFCReaderError.Code.readerTransceiveErrorPacketTooLong](nfcreadererror-swift.struct/code/readertransceiveerrorpackettoolong.md)
  The packet length exceeds the limit supported by the tag.
### Tag Command Configuration Error
- [NFCReaderError.Code.tagCommandConfigurationErrorInvalidParameters](nfcreadererror-swift.struct/code/tagcommandconfigurationerrorinvalidparameters.md)
  The tag has been configured with invalid parameters.
- [NFCReaderError.Code.tagCommandConfigurationErrorInvalidParameters](nfcreadererror-swift.struct/code/tagcommandconfigurationerrorinvalidparameters.md)
  The tag has been configured with invalid parameters.
### Other Errors
- [NFCReaderError.Code.readerErrorUnsupportedFeature](nfcreadererror-swift.struct/code/readererrorunsupportedfeature.md)
  The reader session does not support this feature.
- [NFCReaderError.Code.readerErrorInvalidParameter](nfcreadererror-swift.struct/code/readererrorinvalidparameter.md)
  An input parameter is invalid.
- [NFCReaderError.Code.readerErrorInvalidParameterLength](nfcreadererror-swift.struct/code/readererrorinvalidparameterlength.md)
  The length of an input parameter is invalid.
- [NFCReaderError.Code.readerErrorParameterOutOfBound](nfcreadererror-swift.struct/code/readererrorparameteroutofbound.md)
  A parameter value is outside of the acceptable boundary.
- [NFCReaderError.Code.readerErrorRadioDisabled](nfcreadererror-swift.struct/code/readererrorradiodisabled.md)
  The NFC wireless radio on the device is disabled.
- [NFCReaderError.Code.readerErrorSecurityViolation](nfcreadererror-swift.struct/code/readererrorsecurityviolation.md)
  A security violation associated with the reader session has occurred.
- [NFCReaderError.Code.readerErrorUnsupportedFeature](nfcreadererror-swift.struct/code/readererrorunsupportedfeature.md)
  The reader session does not support this feature.
- [NFCReaderError.Code.readerErrorInvalidParameter](nfcreadererror-swift.struct/code/readererrorinvalidparameter.md)
  An input parameter is invalid.
- [NFCReaderError.Code.readerErrorInvalidParameterLength](nfcreadererror-swift.struct/code/readererrorinvalidparameterlength.md)
  The length of an input parameter is invalid.
- [NFCReaderError.Code.readerErrorParameterOutOfBound](nfcreadererror-swift.struct/code/readererrorparameteroutofbound.md)
  A parameter value is outside of the acceptable boundary.
- [NFCReaderError.Code.readerErrorRadioDisabled](nfcreadererror-swift.struct/code/readererrorradiodisabled.md)
  The NFC wireless radio on the device is disabled.
- [NFCReaderError.Code.readerErrorSecurityViolation](nfcreadererror-swift.struct/code/readererrorsecurityviolation.md)
  A security violation associated with the reader session has occurred.
### Enumeration Cases
- [NFCReaderError.Code.readerErrorAccessNotAccepted](nfcreadererror-swift.struct/code/readererroraccessnotaccepted.md)
- [NFCReaderError.Code.readerErrorIneligible](nfcreadererror-swift.struct/code/readererrorineligible.md)
### Initializers
- [init?(rawValue: Int)](nfcreadererror-swift.struct/code/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct NFCReaderError](nfcreadererror-swift.struct.md)
  An error type that indicates problems with reader sessions or tags.
- [let NFCErrorDomain: String](nfcerrordomain.md)
  The domain for errors associated with Core NFC APIs.
- [let NFCTagResponseUnexpectedLengthErrorKey: String](nfctagresponseunexpectedlengtherrorkey.md)
  A user-information dictionary key that indicates an invalid received response packet length.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfcreadererror-swift.struct/code)*