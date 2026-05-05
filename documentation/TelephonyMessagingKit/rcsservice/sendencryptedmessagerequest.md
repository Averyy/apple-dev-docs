# RCSService.SendEncryptedMessageRequest

**Framework**: TelephonyMessagingKit  
**Kind**: struct

A structure that represents a request to send an encrypted message.

**Availability**:
- iOS 26.5+
- iPadOS 26.5+

## Declaration

```swift
struct SendEncryptedMessageRequest
```

## Topics

### Creating a request
- [init(content: RCSMessage.GeolocationPush, destination: RCSHandle, cellularServiceID: CellularServiceID, messageID: RCSMessageID)](rcsservice/sendencryptedmessagerequest/init(content:destination:cellularserviceid:messageid:)-3ox0y.md)
- [init(content: RCSMessage.Text, destination: RCSHandle, cellularServiceID: CellularServiceID, messageID: RCSMessageID)](rcsservice/sendencryptedmessagerequest/init(content:destination:cellularserviceid:messageid:)-6dm2z.md)
- [init(content: RCSMessage.FileTransfer, destination: RCSHandle, cellularServiceID: CellularServiceID, messageID: RCSMessageID)](rcsservice/sendencryptedmessagerequest/init(content:destination:cellularserviceid:messageid:)-jqfv.md)
### Inspecting receipts
- [var secureSendReceipt: RCSMessage.SecureSendReceipt?](rcsservice/sendencryptedmessagerequest/securesendreceipt.md)
  The send receipt of the original message.
- [RCSMessage.SecureSendReceipt](rcsmessage/securesendreceipt.md)
  A structure that contains the security context of an end-to-end encrypted message.
### Supporting types
- [RCSService.SendEncryptedMessageRequest.Result](rcsservice/sendencryptedmessagerequest/result.md)
  A structure that represents the result of sending an encrypted message.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func sendEncryptedMessageRequest(RCSService.SendEncryptedMessageRequest) async throws -> RCSService.SendEncryptedMessageRequest.Result](rcsservice/sendencryptedmessagerequest(_:).md)
  Sends an encrypted message to a specified destination.
- [RCSService.SendEncryptedMessageRequest.Result](rcsservice/sendencryptedmessagerequest/result.md)
  A structure that represents the result of sending an encrypted message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/rcsservice/sendencryptedmessagerequest)*