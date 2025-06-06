# readerErrorSecurityViolation

**Framework**: Core NFC  
**Kind**: property

A security violation associated with the reader session has occurred.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+

## Declaration

```swift
static var readerErrorSecurityViolation: NFCReaderError.Code { get }
```

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfcreadererror-swift.struct/readererrorsecurityviolation)*