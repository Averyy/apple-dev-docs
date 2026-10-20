# RCSService.SendEncryptedMessageRequest.Result

**Framework**: TelephonyMessagingKit  
**Kind**: struct  
**Role**: Structure

A structure that represents the result of sending an encrypted message.

**Availability**:
- iOS 26.5+

## Declaration

```swift
struct Result
```

## Topics

### Inspecting result properties
- [let secureSendReceipt: RCSMessage.SecureSendReceipt?](./result/securesendreceipt.md)
  The send receipt of the message.
- [RCSMessage.SecureSendReceipt](../../rcsmessage/securesendreceipt.md)
  A structure that contains the security context of an end-to-end encrypted message.

## Relationships

### Conforms To
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)

## See Also

### Sending encrypted messages
- [func sendEncryptedMessageRequest(RCSService.SendEncryptedMessageRequest) async throws -> RCSService.SendEncryptedMessageRequest.Result](../sendencryptedmessagerequest%28_%29.md)
  Sends an encrypted message to a specified destination.
- [RCSService.SendEncryptedMessageRequest](../sendencryptedmessagerequest.md)
  A structure that represents a request to send an encrypted message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/rcsservice/sendencryptedmessagerequest/result)*