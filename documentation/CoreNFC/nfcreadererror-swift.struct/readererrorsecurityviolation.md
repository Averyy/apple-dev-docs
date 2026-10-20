# readerErrorSecurityViolation

**Framework**: Core NFC  
**Kind**: property  
**Role**: Type Property

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

### Other Errors
- [static var readerErrorUnsupportedFeature: NFCReaderError.Code](./readererrorunsupportedfeature.md)
  The reader session does not support this feature.
- [static var readerErrorInvalidParameter: NFCReaderError.Code](./readererrorinvalidparameter.md)
  An input parameter is invalid.
- [static var readerErrorInvalidParameterLength: NFCReaderError.Code](./readererrorinvalidparameterlength.md)
  The length of an input parameter is invalid.
- [static var readerErrorParameterOutOfBound: NFCReaderError.Code](./readererrorparameteroutofbound.md)
  A parameter value is outside of the acceptable boundary.
- [static var readerErrorRadioDisabled: NFCReaderError.Code](./readererrorradiodisabled.md)
  The NFC wireless radio on the device is disabled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfcreadererror-swift.struct/readererrorsecurityviolation)*