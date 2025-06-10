# incomingMessageNotifications

**Framework**: TelephonyMessagingKit  
**Kind**: property

An asynchronous sequence of incoming message notifications produced by this service.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+

## Declaration

```swift
final var incomingMessageNotifications: some AsyncSequence<SMSService.IncomingMessageNotification, Never> { get throws }
```

#### Discussion

Iterate over this sequence with a `for`-`await`-`in` loop to receive [`SMSService.IncomingMessageNotification`](smsservice/incomingmessagenotification.md) instances that indicate the arrival of incoming messages.

## See Also

- [SMSService.IncomingMessageNotification](smsservice/incomingmessagenotification.md)
  A structure that contains information about an incoming SMS message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/smsservice/incomingmessagenotifications)*