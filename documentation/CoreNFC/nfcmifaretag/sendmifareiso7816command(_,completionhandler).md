# sendMiFareISO7816Command(_:completionHandler:)

**Framework**: Core NFC  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Sends an ISO 7816 command APDU to the tag and receives a response APDU.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+

## Declaration

```swift
func sendMiFareISO7816Command(_ apdu: NFCISO7816APDU, completionHandler: @escaping @Sendable (Data, UInt8, UInt8, (any Error)?) -> Void)
```

```swift
func sendMiFareISO7816Command(_ apdu: NFCISO7816APDU) async throws -> (Data, UInt8, UInt8)
```

```objc
- (void) sendMiFareISO7816Command:(NFCISO7816APDU *) apdu completionHandler:(void (^)(NSData *responseData, uint8_t sw1, uint8_t sw2, NSError *error)) completionHandler;
```

## Discussion

Use this method to send commands to tags that have a [`mifareFamily`](./mifarefamily.md) value of either [`NFCMiFareFamily.plus`](../nfcmifarefamily/plus.md) or [`NFCMiFareFamily.desfire`](../nfcmifarefamily/desfire.md).

## Parameters

- `apdu`: An ISO 7816-4 command APDU object.
- `completionHandler`: A handler that the reader session invokes after the operation completes. The session calls `completionHandler` on the dispatch queue that you provided when creating the [`NFCTagReaderSession`](../nfctagreadersession.md) object.

  The handler has the following parameters:

  - **responseData**: An [`NSData`](../../Foundation/nsdata.md) object containing the APDU response.
  - **sw1**: The SW1 command-processing status byte.
  - **sw2**: The SW2 command-processing status byte.
  - **error**: `nil` when the operation is successful; otherwise, an [`NSError`](../../Foundation/nserror.md) object indicating that a problem occurred while communicating with the tag, or that the tag doesn’t support ISO 7816-4 commands.

## Default Implementations

### NFCMiFareTag Implementations
- [func sendMiFareISO7816Command(NFCISO7816APDU) async throws -> NFCISO7816ResponseAPDU](./sendmifareiso7816command%28_%29.md)

## See Also

### Sending Commands
- [func sendMiFareCommand(commandPacket: Data, completionHandler: (Data, (any Error)?) -> Void)](./sendmifarecommand%28commandpacket,completionhandler%29.md)
  Sends a native MIFARE command to the tag.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfcmifaretag/sendmifareiso7816command(_:completionhandler:))*