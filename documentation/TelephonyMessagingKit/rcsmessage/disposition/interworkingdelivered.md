# RCSMessage.Disposition.interworkingDelivered

**Framework**: TelephonyMessagingKit  
**Kind**: case

The carrier used a non-CPM technology to deliver the message.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+

## Declaration

```swift
case interworkingDelivered
```

#### Discussion

This disposition indicates that the carrier used a technology like SMS or MMS to deliver the message.

## See Also

- [RCSMessage.Disposition.delivered](rcsmessage/disposition/delivered.md)
  The carrier delivered the message.
- [RCSMessage.Disposition.deliveryFailed](rcsmessage/disposition/deliveryfailed.md)
  The carrier failed to deliver the message.
- [RCSMessage.Disposition.displayed](rcsmessage/disposition/displayed.md)
  The recipient device displayed the message.
- [RCSMessage.Disposition.interworkingFailed](rcsmessage/disposition/interworkingfailed.md)
  The carrier attempted to use a non-CPM technology to deliver the message, but failed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/rcsmessage/disposition/interworkingdelivered)*