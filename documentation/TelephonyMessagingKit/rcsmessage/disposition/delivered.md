# RCSMessage.Disposition.delivered

**Framework**: TelephonyMessagingKit  
**Kind**: case  
**Role**: Case

The carrier delivered the message.

**Availability**:
- iOS 26.0+

## Declaration

```swift
case delivered
```

## See Also

### Accessing disposition values
- [RCSMessage.Disposition.deliveryFailed](./deliveryfailed.md)
  The carrier failed to deliver the message.
- [RCSMessage.Disposition.displayed](./displayed.md)
  The recipient device displayed the message.
- [RCSMessage.Disposition.interworkingDelivered](./interworkingdelivered.md)
  The carrier used a non-CPM technology to deliver the message.
- [RCSMessage.Disposition.interworkingFailed](./interworkingfailed.md)
  The carrier attempted to use a non-CPM technology to deliver the message, but failed.
- [RCSMessage.Disposition.deliveryFailedDueToDecryptionFailure](./deliveryfailedduetodecryptionfailure.md)
  The recipient device was unable to decrypt the encrypted message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/rcsmessage/disposition/delivered)*