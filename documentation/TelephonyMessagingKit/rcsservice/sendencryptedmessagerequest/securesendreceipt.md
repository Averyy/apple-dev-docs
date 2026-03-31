# secureSendReceipt

**Framework**: TelephonyMessagingKit  
**Kind**: property

The send receipt of the original message.

**Availability**:
- iOS 26.5+ (Beta)
- iPadOS 26.5+ (Beta)

## Declaration

```swift
var secureSendReceipt: RCSMessage.SecureSendReceipt?
```

#### Discussion

Set this after receiving an [`RCSMessage.DispositionNotification`](rcsmessage/dispositionnotification.md) message whose disposition is [`RCSMessage.Disposition.deliveryFailedDueToDecryptionFailure`](rcsmessage/disposition/deliveryfailedduetodecryptionfailure.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/rcsservice/sendencryptedmessagerequest/securesendreceipt)*