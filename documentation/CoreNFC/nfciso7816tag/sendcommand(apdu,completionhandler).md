# sendCommand(apdu:completionHandler:)

**Framework**: Core NFC  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Sends an application protocol data unit (APDU) to the tag and receives a response APDU.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+

## Declaration

```swift
func sendCommand(apdu: NFCISO7816APDU, completionHandler: @escaping @Sendable (Data, UInt8, UInt8, (any Error)?) -> Void)
```

```swift
func sendCommand(apdu: NFCISO7816APDU) async throws -> (Data, UInt8, UInt8)
```

```objc
- (void) sendCommandAPDU:(NFCISO7816APDU *) apdu completionHandler:(void (^)(NSData *responseData, uint8_t sw1, uint8_t sw2, NSError *error)) completionHandler;
```

#### Discussion

When you send a `SELECT` command with a [`p1Parameter`](../nfciso7816apdu/p1parameter.md) value of `0x04`, your app must support one of the applications listed in the [`ISO7816 application identifiers for NFC Tag Reader Session`](../../BundleResources/entitlements/com.apple.developer.nfc.readersession.iso7816.select-identifiers.md) property list key. Otherwise, the `completionHandler` receives an [`NFCReaderError.Code.readerErrorSecurityViolation`](../nfcreadererror-swift.struct/code/readererrorsecurityviolation.md) error.

The session calls `completionHandler` on the dispatch queue that you provided when creating the [`NFCTagReaderSession`](../nfctagreadersession.md) object.

## Parameters

- `apdu`: An application protocol data unit to send to the tag.
- `completionHandler`: A handler that the reader session invokes after the operation completes. The handler has the following parameters:

  - **responseData**: The response data, which may be empty even if the operation completes successfully.
  - **sw1**: The SW1 command-processing status byte. This value is always valid.
  - **sw2**: The SW2 command-processing status byte. This value is always valid.
  - **error**: `nil` when the operation completes successfully; otherwise, an [`NSError`](../../Foundation/nserror.md) object when there’s a communication issue with the tag.

## Default Implementations

### NFCISO7816Tag Implementations
- [func sendCommand(apdu: NFCISO7816APDU) async throws -> NFCISO7816ResponseAPDU](./sendcommand%28apdu%29.md)

## See Also

### Sending a Command
- [func sendCommand(apdu: NFCISO7816APDU, resultHandler: (Result<NFCISO7816ResponseAPDU, any Error>) -> Void)](./sendcommand%28apdu,resulthandler%29.md)
  Sends an application protocol data unit (APDU) to the tag and receives a response APDU.
- [class NFCISO7816APDU](../nfciso7816apdu.md)
  An object representing an ISO 7816 application protocol data unit (APDU).
- [struct NFCISO7816ResponseAPDU](../nfciso7816responseapdu.md)
  An object containing the response from the tag.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfciso7816tag/sendcommand(apdu:completionhandler:))*