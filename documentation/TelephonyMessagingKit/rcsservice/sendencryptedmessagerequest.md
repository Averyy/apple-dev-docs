# RCSService.SendEncryptedMessageRequest

**Framework**: TelephonyMessagingKit  
**Kind**: struct  
**Role**: Structure

A structure that represents a request to send an encrypted message.

**Availability**:
- iOS 26.5+

## Declaration

```swift
struct SendEncryptedMessageRequest
```

## Topics

### Creating a request
- [init(content: RCSMessage.GeolocationPush, destination: RCSHandle, cellularServiceID: CellularServiceID, messageID: RCSMessageID)](./sendencryptedmessagerequest/init%28content,destination,cellularserviceid,messageid%29-3ox0y.md)
  Creates a new send encrypted message request with the given parameters.
- [init(content: RCSMessage.Text, destination: RCSHandle, cellularServiceID: CellularServiceID, messageID: RCSMessageID)](./sendencryptedmessagerequest/init%28content,destination,cellularserviceid,messageid%29-6dm2z.md)
  Creates a new send encrypted message request with the given parameters.
- [init(content: RCSMessage.FileTransfer, destination: RCSHandle, cellularServiceID: CellularServiceID, messageID: RCSMessageID)](./sendencryptedmessagerequest/init%28content,destination,cellularserviceid,messageid%29-jqfv.md)
  Creates a new send encrypted message request with the given parameters.
### Inspecting receipts
- [var secureSendReceipt: RCSMessage.SecureSendReceipt?](./sendencryptedmessagerequest/securesendreceipt.md)
  The send receipt of the original message.
- [RCSMessage.SecureSendReceipt](../rcsmessage/securesendreceipt.md)
  A structure that contains the security context of an end-to-end encrypted message.
### Supporting types
- [RCSService.SendEncryptedMessageRequest.Result](./sendencryptedmessagerequest/result.md)
  A structure that represents the result of sending an encrypted message.
### Initializers
- [init(content: RCSMessage.Reply, destination: RCSHandle, cellularServiceID: CellularServiceID, messageID: RCSMessageID)](./sendencryptedmessagerequest/init%28content,destination,cellularserviceid,messageid%29-8lk8q.md)
  Creates a new send encrypted message request with the given parameters.
- [init(content: RCSMessage.Reaction, destination: RCSHandle, cellularServiceID: CellularServiceID, messageID: RCSMessageID)](./sendencryptedmessagerequest/init%28content,destination,cellularserviceid,messageid%29-9lffd.md)
  Creates a new send encrypted message request with the given parameters.
- [init(content: RCSMessage.CustomReaction, destination: RCSHandle, cellularServiceID: CellularServiceID, messageID: RCSMessageID)](./sendencryptedmessagerequest/init%28content,destination,cellularserviceid,messageid%29-9ns32.md)
  Creates a new send encrypted message request with the given parameters.

## Relationships

### Conforms To
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Sending encrypted messages
- [func sendEncryptedMessageRequest(RCSService.SendEncryptedMessageRequest) async throws -> RCSService.SendEncryptedMessageRequest.Result](./sendencryptedmessagerequest%28_%29.md)
  Sends an encrypted message to a specified destination.
- [RCSService.SendEncryptedMessageRequest.Result](./sendencryptedmessagerequest/result.md)
  A structure that represents the result of sending an encrypted message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/rcsservice/sendencryptedmessagerequest)*