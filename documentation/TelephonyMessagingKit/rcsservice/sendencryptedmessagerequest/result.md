# RCSService.SendEncryptedMessageRequest.Result

**Framework**: TelephonyMessagingKit  
**Kind**: struct

A structure that represents the result of sending an encrypted message.

**Availability**:
- iOS 26.5+

## Declaration

```swift
struct Result
```

## Topics

### Inspecting result properties
- [let secureSendReceipt: RCSMessage.SecureSendReceipt?](rcsservice/sendencryptedmessagerequest/result/securesendreceipt.md)
  The send receipt of the message.
- [RCSMessage.SecureSendReceipt](rcsmessage/securesendreceipt.md)
  A structure that contains the security context of an end-to-end encrypted message.

## Relationships

### Conforms To
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [func sendEncryptedMessageRequest(RCSService.SendEncryptedMessageRequest) async throws -> RCSService.SendEncryptedMessageRequest.Result](rcsservice/sendencryptedmessagerequest(_:).md)
  Sends an encrypted message to a specified destination.
- [RCSService.SendEncryptedMessageRequest](rcsservice/sendencryptedmessagerequest.md)
  A structure that represents a request to send an encrypted message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/rcsservice/sendencryptedmessagerequest/result)*