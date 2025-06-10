# criticalMessageStateNotifications

**Framework**: TelephonyMessagingKit  
**Kind**: property

An asynchronous sequence of critical message state notifications.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+

## Declaration

```swift
final var criticalMessageStateNotifications: some AsyncSequence<SMSService.CriticalMessageStateNotification, Never> { get throws }
```

#### Discussion

This sequence tracks messages sent with the Critical Messaging API, as described in [`Sending SMS messages from an app`](https://developer.apple.com/documentation/Messages/critical-messaging-api).

## See Also

- [SMSService.CriticalMessageStateNotification](smsservice/criticalmessagestatenotification.md)
  A structure that contains information about a critical SMS message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/smsservice/criticalmessagestatenotifications)*