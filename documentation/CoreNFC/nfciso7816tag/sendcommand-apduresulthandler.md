# sendCommand(apdu:resultHandler:)

**Framework**: Core NFC  
**Kind**: method

Sends an application protocol data unit (APDU) to the tag and receives a response APDU.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst ?+

## Declaration

```swift
func sendCommand(apdu: NFCISO7816APDU, resultHandler: @escaping (Result<NFCISO7816ResponseAPDU, any Error>) -> Void)
```

#### Discussion

When you send a `SELECT` command with a [`p1Parameter`](nfciso7816apdu/p1parameter.md) value of `0x04`, your app must support one of the applications listed in the [`ISO7816 application identifiers for NFC Tag Reader Session`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.nfc.readersession.iso7816.select-identifiers) property list key. Otherwise, the `resultHandler` receives an [`NFCReaderError.Code.readerErrorSecurityViolation`](nfcreadererror-swift.struct/code/readererrorsecurityviolation.md) error.

The session calls `resultHandler` on the dispatch queue that you provided when creating the [`NFCTagReaderSession`](nfctagreadersession.md) object.

## Parameters

- `apdu`: An application protocol data unit to send to the tag.
- `resultHandler`: A handler that the reader session invokes after the operation completes. The handler receives a   with the cases:

## See Also

- [func sendCommand(apdu: NFCISO7816APDU, completionHandler: (Data, UInt8, UInt8, (any Error)?) -> Void)](nfciso7816tag/sendcommand(apdu:completionhandler:).md)
  Sends an application protocol data unit (APDU) to the tag and receives a response APDU.
- [class NFCISO7816APDU](nfciso7816apdu.md)
  An object representing an ISO 7816 application protocol data unit (APDU).
- [struct NFCISO7816ResponseAPDU](nfciso7816responseapdu.md)
  An object containing the response from the tag.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfciso7816tag/sendcommand(apdu:resulthandler:))*