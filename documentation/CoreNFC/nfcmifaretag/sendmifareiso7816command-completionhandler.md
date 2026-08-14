# sendMiFareISO7816Command(_:completionHandler:)

**Framework**: Core NFC  
**Kind**: method  
**Required**: Yes

Sends an ISO 7816 command APDU to the tag and receives a response APDU.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+

## Declaration

```swift
func sendMiFareISO7816Command(_ apdu: NFCISO7816APDU) async throws -> (Data, UInt8, UInt8)
```

#### Discussion

Use this method to send commands to tags that have a [`mifareFamily`](nfcmifaretag/mifarefamily.md) value of either [`NFCMiFareFamily.plus`](nfcmifarefamily/plus.md) or [`NFCMiFareFamily.desfire`](nfcmifarefamily/desfire.md).

## Parameters

- `apdu`: An ISO 7816-4 command APDU object.
- `completionHandler`: A handler that the reader session invokes after the operation completes. The session calls `completionHandler` on the dispatch queue that you provided when creating the [`NFCTagReaderSession`](nfctagreadersession.md) object. The handler has the following parameters: - **responseData**: An [`NSData`](https://developer.apple.com/documentation/foundation/nsdata) object containing the APDU response.
- **sw1**: The SW1 command-processing status byte.
- **sw2**: The SW2 command-processing status byte.
- **error**: `nil` when the operation is successful; otherwise, an [`NSError`](https://developer.apple.com/documentation/foundation/nserror) object indicating that a problem occurred while communicating with the tag, or that the tag doesn’t support ISO 7816-4 commands.

## See Also

- [func sendMiFareCommand(commandPacket: Data, completionHandler: (Data, (any Error)?) -> Void)](nfcmifaretag/sendmifarecommand(commandpacket:completionhandler:).md)
  Sends a native MIFARE command to the tag.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfcmifaretag/sendmifareiso7816command(_:completionhandler:))*