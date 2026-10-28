# secureSendReceipt

**Framework**: TelephonyMessagingKit  
**Kind**: property  
**Role**: Instance Property

The send receipt of the original message.

**Availability**:
- iOS 26.5+

## Declaration

```swift
var secureSendReceipt: RCSMessage.SecureSendReceipt?
```

## Discussion

Set this after receiving an [`RCSMessage.DispositionNotification`](../../rcsmessage/dispositionnotification.md) message whose disposition is [`RCSMessage.Disposition.deliveryFailedDueToDecryptionFailure`](../../rcsmessage/disposition/deliveryfailedduetodecryptionfailure.md).

## See Also

### Inspecting receipts
- [RCSMessage.SecureSendReceipt](../../rcsmessage/securesendreceipt.md)
  A structure that contains the security context of an end-to-end encrypted message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/rcsservice/sendencryptedmessagerequest/securesendreceipt)*