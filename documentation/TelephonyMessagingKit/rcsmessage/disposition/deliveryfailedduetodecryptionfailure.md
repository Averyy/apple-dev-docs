# RCSMessage.Disposition.deliveryFailedDueToDecryptionFailure

**Framework**: TelephonyMessagingKit  
**Kind**: case  
**Role**: Case

The recipient device was unable to decrypt the encrypted message.

**Availability**:
- iOS 26.5+

## Declaration

```swift
case deliveryFailedDueToDecryptionFailure
```

## See Also

### Accessing disposition values
- [RCSMessage.Disposition.delivered](./delivered.md)
  The carrier delivered the message.
- [RCSMessage.Disposition.deliveryFailed](./deliveryfailed.md)
  The carrier failed to deliver the message.
- [RCSMessage.Disposition.displayed](./displayed.md)
  The recipient device displayed the message.
- [RCSMessage.Disposition.interworkingDelivered](./interworkingdelivered.md)
  The carrier used a non-CPM technology to deliver the message.
- [RCSMessage.Disposition.interworkingFailed](./interworkingfailed.md)
  The carrier attempted to use a non-CPM technology to deliver the message, but failed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/rcsmessage/disposition/deliveryfailedduetodecryptionfailure)*