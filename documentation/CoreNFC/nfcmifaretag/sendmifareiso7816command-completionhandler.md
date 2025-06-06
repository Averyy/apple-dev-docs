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
- `completionHandler`: The handler has the following parameters:

## See Also

- [func sendMiFareCommand(commandPacket: Data, completionHandler: (Data, (any Error)?) -> Void)](nfcmifaretag/sendmifarecommand(commandpacket:completionhandler:).md)
  Sends a native MIFARE command to the tag.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfcmifaretag/sendmifareiso7816command(_:completionhandler:))*