# incomingMessageNotifications

**Framework**: TelephonyMessagingKit  
**Kind**: property  
**Role**: Instance Property

An asynchronous sequence of incoming message notifications produced by this service.

**Availability**:
- iOS 26.0+

## Declaration

```swift
final var incomingMessageNotifications: some AsyncSequence<SMSService.IncomingMessageNotification, Never> { get throws }
```

#### Discussion

Iterate over this sequence with a `for`-`await`-`in` loop to receive [`SMSService.IncomingMessageNotification`](./incomingmessagenotification.md) instances that indicate the arrival of incoming messages.

## See Also

### Receiving messages
- [SMSService.IncomingMessageNotification](./incomingmessagenotification.md)
  A structure that contains information about an incoming SMS message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/smsservice/incomingmessagenotifications)*