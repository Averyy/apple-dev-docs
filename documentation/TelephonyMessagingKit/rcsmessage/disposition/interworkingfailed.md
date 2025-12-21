# RCSMessage.Disposition.interworkingFailed

**Framework**: TelephonyMessagingKit  
**Kind**: case

The carrier attempted to use a non-CPM technology to deliver the message, but failed.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+

## Declaration

```swift
case interworkingFailed
```

#### Discussion

This disposition indicates that the carrier attempted to use a technology like SMS or MMS to deliver the message.

## See Also

- [RCSMessage.Disposition.delivered](rcsmessage/disposition/delivered.md)
  The carrier delivered the message.
- [RCSMessage.Disposition.deliveryFailed](rcsmessage/disposition/deliveryfailed.md)
  The carrier failed to deliver the message.
- [RCSMessage.Disposition.displayed](rcsmessage/disposition/displayed.md)
  The recipient device displayed the message.
- [RCSMessage.Disposition.interworkingDelivered](rcsmessage/disposition/interworkingdelivered.md)
  The carrier used a non-CPM technology to deliver the message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/rcsmessage/disposition/interworkingfailed)*