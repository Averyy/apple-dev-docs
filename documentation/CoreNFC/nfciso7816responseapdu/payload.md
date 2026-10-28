# payload

**Framework**: Core NFC  
**Kind**: property  
**Role**: Instance Property

A data object that contains the response data.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
var payload: Data?
```

## Discussion

The data may be empty even if [`sendCommand(apdu:resultHandler:)`](../nfciso7816tag/sendcommand%28apdu,resulthandler%29.md) completes successfully.

## See Also

### Response Data
- [var statusWord1: UInt8](./statusword1.md)
  The SW1 command-processing status byte.
- [var statusWord2: UInt8](./statusword2.md)
  The SW2 command-processing status byte.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfciso7816responseapdu/payload)*