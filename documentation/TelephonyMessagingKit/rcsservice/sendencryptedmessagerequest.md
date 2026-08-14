# RCSService.SendEncryptedMessageRequest

**Framework**: TelephonyMessagingKit  
**Kind**: struct

A structure that represents a request to send an encrypted message.

**Availability**:
- iOS 26.5+

## Declaration

```swift
struct SendEncryptedMessageRequest
```

## Topics

### Creating a request
- [init(content: RCSMessage.GeolocationPush, destination: RCSHandle, cellularServiceID: CellularServiceID, messageID: RCSMessageID)](rcsservice/sendencryptedmessagerequest/init(content:destination:cellularserviceid:messageid:)-3ox0y.md)
  Creates a new send encrypted message request with the given parameters.
- [init(content: RCSMessage.Text, destination: RCSHandle, cellularServiceID: CellularServiceID, messageID: RCSMessageID)](rcsservice/sendencryptedmessagerequest/init(content:destination:cellularserviceid:messageid:)-6dm2z.md)
  Creates a new send encrypted message request with the given parameters.
- [init(content: RCSMessage.FileTransfer, destination: RCSHandle, cellularServiceID: CellularServiceID, messageID: RCSMessageID)](rcsservice/sendencryptedmessagerequest/init(content:destination:cellularserviceid:messageid:)-jqfv.md)
  Creates a new send encrypted message request with the given parameters.
### Inspecting receipts
- [var secureSendReceipt: RCSMessage.SecureSendReceipt?](rcsservice/sendencryptedmessagerequest/securesendreceipt.md)
  The send receipt of the original message.
- [RCSMessage.SecureSendReceipt](rcsmessage/securesendreceipt.md)
  A structure that contains the security context of an end-to-end encrypted message.
### Supporting types
- [RCSService.SendEncryptedMessageRequest.Result](rcsservice/sendencryptedmessagerequest/result.md)
  A structure that represents the result of sending an encrypted message.
### Initializers
- [init(content: RCSMessage.Reply, destination: RCSHandle, cellularServiceID: CellularServiceID, messageID: RCSMessageID)](rcsservice/sendencryptedmessagerequest/init(content:destination:cellularserviceid:messageid:)-8lk8q.md)
  Creates a new send encrypted message request with the given parameters.
- [init(content: RCSMessage.Reaction, destination: RCSHandle, cellularServiceID: CellularServiceID, messageID: RCSMessageID)](rcsservice/sendencryptedmessagerequest/init(content:destination:cellularserviceid:messageid:)-9lffd.md)
  Creates a new send encrypted message request with the given parameters.
- [init(content: RCSMessage.CustomReaction, destination: RCSHandle, cellularServiceID: CellularServiceID, messageID: RCSMessageID)](rcsservice/sendencryptedmessagerequest/init(content:destination:cellularserviceid:messageid:)-9ns32.md)
  Creates a new send encrypted message request with the given parameters.

## Relationships

### Conforms To
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [func sendEncryptedMessageRequest(RCSService.SendEncryptedMessageRequest) async throws -> RCSService.SendEncryptedMessageRequest.Result](rcsservice/sendencryptedmessagerequest(_:).md)
  Sends an encrypted message to a specified destination.
- [RCSService.SendEncryptedMessageRequest.Result](rcsservice/sendencryptedmessagerequest/result.md)
  A structure that represents the result of sending an encrypted message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/rcsservice/sendencryptedmessagerequest)*