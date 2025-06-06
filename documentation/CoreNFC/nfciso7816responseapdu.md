# NFCISO7816ResponseAPDU

**Framework**: Core NFC  
**Kind**: struct

An object containing the response from the tag.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst ?+

## Declaration

```swift
struct NFCISO7816ResponseAPDU
```

## Topics

### Response Data
- [var payload: Data?](nfciso7816responseapdu/payload.md)
  A data object that contains the response data.
- [var statusWord1: UInt8](nfciso7816responseapdu/statusword1.md)
  The SW1 command-processing status byte.
- [var statusWord2: UInt8](nfciso7816responseapdu/statusword2.md)
  The SW2 command-processing status byte.

## See Also

- [func sendCommand(apdu: NFCISO7816APDU, resultHandler: (Result<NFCISO7816ResponseAPDU, any Error>) -> Void)](nfciso7816tag/sendcommand(apdu:resulthandler:).md)
  Sends an application protocol data unit (APDU) to the tag and receives a response APDU.
- [func sendCommand(apdu: NFCISO7816APDU, completionHandler: (Data, UInt8, UInt8, (any Error)?) -> Void)](nfciso7816tag/sendcommand(apdu:completionhandler:).md)
  Sends an application protocol data unit (APDU) to the tag and receives a response APDU.
- [class NFCISO7816APDU](nfciso7816apdu.md)
  An object representing an ISO 7816 application protocol data unit (APDU).


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfciso7816responseapdu)*