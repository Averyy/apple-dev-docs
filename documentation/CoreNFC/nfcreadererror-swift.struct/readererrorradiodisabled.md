# readerErrorRadioDisabled

**Framework**: Core NFC  
**Kind**: property

The NFC wireless radio on the device is disabled.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
static var readerErrorRadioDisabled: NFCReaderError.Code { get }
```

#### Discussion

This condition happens, for example, when a person enables airplane mode on their device.

## See Also

- [static var readerErrorUnsupportedFeature: NFCReaderError.Code](nfcreadererror-swift.struct/readererrorunsupportedfeature.md)
  The reader session does not support this feature.
- [static var readerErrorInvalidParameter: NFCReaderError.Code](nfcreadererror-swift.struct/readererrorinvalidparameter.md)
  An input parameter is invalid.
- [static var readerErrorInvalidParameterLength: NFCReaderError.Code](nfcreadererror-swift.struct/readererrorinvalidparameterlength.md)
  The length of an input parameter is invalid.
- [static var readerErrorParameterOutOfBound: NFCReaderError.Code](nfcreadererror-swift.struct/readererrorparameteroutofbound.md)
  A parameter value is outside of the acceptable boundary.
- [static var readerErrorSecurityViolation: NFCReaderError.Code](nfcreadererror-swift.struct/readererrorsecurityviolation.md)
  A security violation associated with the reader session has occurred.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfcreadererror-swift.struct/readererrorradiodisabled)*