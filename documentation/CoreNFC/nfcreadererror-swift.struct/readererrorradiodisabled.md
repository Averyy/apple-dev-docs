# readerErrorRadioDisabled

**Framework**: Core NFC  
**Kind**: property  
**Role**: Type Property

The NFC wireless radio on the device is disabled.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
static var readerErrorRadioDisabled: NFCReaderError.Code { get }
```

## Discussion

This condition happens, for example, when a person enables airplane mode on their device.

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
- [static var readerErrorSecurityViolation: NFCReaderError.Code](./readererrorsecurityviolation.md)
  A security violation associated with the reader session has occurred.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfcreadererror-swift.struct/readererrorradiodisabled)*