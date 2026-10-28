# sendMiFareCommand(commandPacket:completionHandler:)

**Framework**: Core NFC  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Sends a native MIFARE command to the tag.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+

## Declaration

```swift
func sendMiFareCommand(commandPacket command: Data, completionHandler: @escaping @Sendable (Data, (any Error)?) -> Void)
```

```swift
func sendMiFareCommand(commandPacket command: Data) async throws -> Data
```

```objc
- (void) sendMiFareCommand:(NSData *) command completionHandler:(void (^)(NSData *response, NSError *error)) completionHandler;
```

## Discussion

Use this method to send commands to tags that are from the [`NFCMiFareFamily.ultralight`](../nfcmifarefamily/ultralight.md), [`NFCMiFareFamily.plus`](../nfcmifarefamily/plus.md), and [`NFCMiFareFamily.desfire`](../nfcmifarefamily/desfire.md) product families.

This method supports command chaining, passing the full response composed of the individual fragments to the `completionHandler`.

> **Note**:  This method doesn’t support the Crypto1 protocol.

## Parameters

- `command`: A MIFARE command. For [`NFCMiFareFamily.ultralight`](../nfcmifarefamily/ultralight.md) commands, you must calculate a 2-byte CRC value and append it to the end of the `command` data.
- `completionHandler`: A handler that the reader session invokes after the operation completes. The session calls `completionHandler` on the dispatch queue that you provided when creating the [`NFCTagReaderSession`](../nfctagreadersession.md) object.

  The handler has the following parameters:

  - **response**: An [`NSData`](../../Foundation/nsdata.md) object containing the tag’s response data for the command.
  - **error**: `nil` when the operation is successful; otherwise, an [`NSError`](../../Foundation/nserror.md) object indicating that a problem occurred while communicating with the tag.

## See Also

### Sending Commands
- [func sendMiFareISO7816Command(NFCISO7816APDU, completionHandler: (Data, UInt8, UInt8, (any Error)?) -> Void)](./sendmifareiso7816command%28_,completionhandler%29.md)
  Sends an ISO 7816 command APDU to the tag and receives a response APDU.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfcmifaretag/sendmifarecommand(commandpacket:completionhandler:))*