# NFCReaderError

**Framework**: Core NFC  
**Kind**: struct

An error type that indicates problems with reader sessions or tags.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+

## Declaration

```swift
struct NFCReaderError
```

## Topics

### Session Errors
- [static var readerSessionInvalidationErrorFirstNDEFTagRead: NFCReaderError.Code](nfcreadererror-swift.struct/readersessioninvalidationerrorfirstndeftagread.md)
  The first NDEF tag read by this session is invalid.
- [static var readerSessionInvalidationErrorSessionTerminatedUnexpectedly: NFCReaderError.Code](nfcreadererror-swift.struct/readersessioninvalidationerrorsessionterminatedunexpectedly.md)
  The reader session terminated unexpectedly.
- [static var readerSessionInvalidationErrorSessionTimeout: NFCReaderError.Code](nfcreadererror-swift.struct/readersessioninvalidationerrorsessiontimeout.md)
  The reader session timed out.
- [static var readerSessionInvalidationErrorSystemIsBusy: NFCReaderError.Code](nfcreadererror-swift.struct/readersessioninvalidationerrorsystemisbusy.md)
  The reader session failed because the system is busy.
- [static var readerSessionInvalidationErrorUserCanceled: NFCReaderError.Code](nfcreadererror-swift.struct/readersessioninvalidationerrorusercanceled.md)
  The user canceled the reader session.
### NDEF Tag Errors
- [static var ndefReaderSessionErrorTagNotWritable: NFCReaderError.Code](nfcreadererror-swift.struct/ndefreadersessionerrortagnotwritable.md)
  The NDEF tag isn’t writable.
- [static var ndefReaderSessionErrorTagSizeTooSmall: NFCReaderError.Code](nfcreadererror-swift.struct/ndefreadersessionerrortagsizetoosmall.md)
  The NDEF tag memory size is too small to store the data.
- [static var ndefReaderSessionErrorTagUpdateFailure: NFCReaderError.Code](nfcreadererror-swift.struct/ndefreadersessionerrortagupdatefailure.md)
  The reader session failed to update the NDEF tag.
- [static var ndefReaderSessionErrorZeroLengthMessage: NFCReaderError.Code](nfcreadererror-swift.struct/ndefreadersessionerrorzerolengthmessage.md)
  The NDEF tag doesn’t contain an NDEF message.
### Transceive Errors
- [static var readerTransceiveErrorRetryExceeded: NFCReaderError.Code](nfcreadererror-swift.struct/readertransceiveerrorretryexceeded.md)
  Too many retries have occurred.
- [static var readerTransceiveErrorTagConnectionLost: NFCReaderError.Code](nfcreadererror-swift.struct/readertransceiveerrortagconnectionlost.md)
  The reader lost the connection to the tag.
- [static var readerTransceiveErrorTagNotConnected: NFCReaderError.Code](nfcreadererror-swift.struct/readertransceiveerrortagnotconnected.md)
  The tag isn’t in the connected state.
- [static var readerTransceiveErrorTagResponseError: NFCReaderError.Code](nfcreadererror-swift.struct/readertransceiveerrortagresponseerror.md)
  The tag has responded with an error.
- [static var readerTransceiveErrorSessionInvalidated: NFCReaderError.Code](nfcreadererror-swift.struct/readertransceiveerrorsessioninvalidated.md)
  The reader session is invalid.
- [static var readerTransceiveErrorPacketTooLong: NFCReaderError.Code](nfcreadererror-swift.struct/readertransceiveerrorpackettoolong.md)
  The packet length exceeds the limit supported by the tag.
### Tag Command Configuration Error
- [static var tagCommandConfigurationErrorInvalidParameters: NFCReaderError.Code](nfcreadererror-swift.struct/tagcommandconfigurationerrorinvalidparameters.md)
  The tag has been configured with invalid parameters.
### Other Errors
- [static var readerErrorUnsupportedFeature: NFCReaderError.Code](nfcreadererror-swift.struct/readererrorunsupportedfeature.md)
  The reader session does not support this feature.
- [static var readerErrorInvalidParameter: NFCReaderError.Code](nfcreadererror-swift.struct/readererrorinvalidparameter.md)
  An input parameter is invalid.
- [static var readerErrorInvalidParameterLength: NFCReaderError.Code](nfcreadererror-swift.struct/readererrorinvalidparameterlength.md)
  The length of an input parameter is invalid.
- [static var readerErrorParameterOutOfBound: NFCReaderError.Code](nfcreadererror-swift.struct/readererrorparameteroutofbound.md)
  A parameter value is outside of the acceptable boundary.
- [static var readerErrorRadioDisabled: NFCReaderError.Code](nfcreadererror-swift.struct/readererrorradiodisabled.md)
  The NFC wireless radio on the device is disabled.
- [static var readerErrorSecurityViolation: NFCReaderError.Code](nfcreadererror-swift.struct/readererrorsecurityviolation.md)
  A security violation associated with the reader session has occurred.
### Error Domain
- [let NFCErrorDomain: String](nfcerrordomain.md)
  The domain for errors associated with Core NFC APIs.
### Type Properties
- [static var errorDomain: String](nfcreadererror-swift.struct/errordomain.md)
- [static var readerErrorAccessNotAccepted: NFCReaderError.Code](nfcreadererror-swift.struct/readererroraccessnotaccepted.md)
- [static var readerErrorIneligible: NFCReaderError.Code](nfcreadererror-swift.struct/readererrorineligible.md)

## Relationships

### Conforms To
- [CustomNSError](../Foundation/CustomNSError.md)
- [Equatable](../Swift/Equatable.md)
- [Error](../Swift/Error.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [NFCReaderError.Code](nfcreadererror-swift.struct/code.md)
  Reader session and tag error codes.
- [let NFCErrorDomain: String](nfcerrordomain.md)
  The domain for errors associated with Core NFC APIs.
- [let NFCTagResponseUnexpectedLengthErrorKey: String](nfctagresponseunexpectedlengtherrorkey.md)
  A user-information dictionary key that indicates an invalid received response packet length.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfcreadererror-swift.struct)*