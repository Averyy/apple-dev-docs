# sendEncryptedMessageRequest(_:)

**Framework**: TelephonyMessagingKit  
**Kind**: method  
**Role**: Instance Method

Sends an encrypted message to a specified destination.

**Availability**:
- iOS 26.5+

## Declaration

```swift
final func sendEncryptedMessageRequest(_ request: RCSService.SendEncryptedMessageRequest) async throws -> RCSService.SendEncryptedMessageRequest.Result
```

## Discussion

Your app may persist the returned [`RCSMessage.SecureSendReceipt`](../rcsmessage/securesendreceipt.md) instance to retry sending the message in the event that the recipient device fails to decrypt the original message.

To retry a request, set the [`secureSendReceipt`](./sendencryptedmessagerequest/securesendreceipt.md) property of the request, after receiving an [`RCSMessage.DispositionNotification`](../rcsmessage/dispositionnotification.md) message whose disposition is [`RCSMessage.Disposition.deliveryFailedDueToDecryptionFailure`](../rcsmessage/disposition/deliveryfailedduetodecryptionfailure.md).

## See Also

### Sending encrypted messages
- [RCSService.SendEncryptedMessageRequest](./sendencryptedmessagerequest.md)
  A structure that represents a request to send an encrypted message.
- [RCSService.SendEncryptedMessageRequest.Result](./sendencryptedmessagerequest/result.md)
  A structure that represents the result of sending an encrypted message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/rcsservice/sendencryptedmessagerequest(_:))*