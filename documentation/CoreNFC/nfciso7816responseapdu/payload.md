# payload

**Framework**: Core NFC  
**Kind**: property

A data object that contains the response data.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst ?+

## Declaration

```swift
var payload: Data?
```

#### Discussion

The data may be empty even if [`sendCommand(apdu:resultHandler:)`](nfciso7816tag/sendcommand(apdu:resulthandler:).md) completes successfully.

## See Also

- [var statusWord1: UInt8](nfciso7816responseapdu/statusword1.md)
  The SW1 command-processing status byte.
- [var statusWord2: UInt8](nfciso7816responseapdu/statusword2.md)
  The SW2 command-processing status byte.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfciso7816responseapdu/payload)*