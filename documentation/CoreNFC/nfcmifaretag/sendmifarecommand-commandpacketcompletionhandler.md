# sendMiFareCommand(commandPacket:completionHandler:)

**Framework**: Core NFC  
**Kind**: method  
**Required**: Yes

Sends a native MIFARE command to the tag.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+

## Declaration

```swift
func sendMiFareCommand(commandPacket command: Data) async throws -> Data
```

#### Discussion

Use this method to send commands to tags that are from the [`NFCMiFareFamily.ultralight`](nfcmifarefamily/ultralight.md), [`NFCMiFareFamily.plus`](nfcmifarefamily/plus.md), and [`NFCMiFareFamily.desfire`](nfcmifarefamily/desfire.md) product families.

This method supports command chaining, passing the full response composed of the individual fragments to the `completionHandler`.

> **Note**:  This method doesn’t support the Crypto1 protocol.

 This method doesn’t support the Crypto1 protocol.

## Parameters

- `command`: A MIFARE command. For   commands, you must calculate a 2-byte CRC value and append it to the end of the   data.
- `completionHandler`: The handler has the following parameters:

## See Also

- [func sendMiFareISO7816Command(NFCISO7816APDU, completionHandler: (Data, UInt8, UInt8, (any Error)?) -> Void)](nfcmifaretag/sendmifareiso7816command(_:completionhandler:).md)
  Sends an ISO 7816 command APDU to the tag and receives a response APDU.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfcmifaretag/sendmifarecommand(commandpacket:completionhandler:))*