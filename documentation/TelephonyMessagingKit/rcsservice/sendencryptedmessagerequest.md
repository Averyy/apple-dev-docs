# sendEncryptedMessageRequest(_:)

**Framework**: TelephonyMessagingKit  
**Kind**: method

Sends an encrypted message to a specified destination.

**Availability**:
- iOS 26.5+ (Beta)
- iPadOS 26.5+ (Beta)

## Declaration

```swift
final func sendEncryptedMessageRequest(_ request: RCSService.SendEncryptedMessageRequest) async throws -> RCSService.SendEncryptedMessageRequest.Result
```

#### Discussion

Your app may persist the returned [`RCSMessage.SecureSendReceipt`](rcsmessage/securesendreceipt.md) instance to retry sending the message in the event that the recipient device fails to decrypt the original message.

To retry a request, set the [`secureSendReceipt`](rcsservice/sendencryptedmessagerequest/securesendreceipt.md) property of the request, after receiving an [`RCSMessage.DispositionNotification`](rcsmessage/dispositionnotification.md) message whose disposition is [`RCSMessage.Disposition.deliveryFailedDueToDecryptionFailure`](rcsmessage/disposition/deliveryfailedduetodecryptionfailure.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/rcsservice/sendencryptedmessagerequest(_:))*