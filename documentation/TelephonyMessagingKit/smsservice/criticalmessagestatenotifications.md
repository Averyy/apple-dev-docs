# criticalMessageStateNotifications

**Framework**: TelephonyMessagingKit  
**Kind**: property  
**Role**: Instance Property

An asynchronous sequence of critical message state notifications.

**Availability**:
- iOS 26.0+

## Declaration

```swift
final var criticalMessageStateNotifications: some AsyncSequence<SMSService.CriticalMessageStateNotification, Never> { get throws }
```

## Discussion

This sequence tracks messages sent with the Critical Messaging API, as described in [Sending SMS messages from an app](../../Messages/critical-messaging-api.md).

## See Also

### Handling critical state changes
- [SMSService.CriticalMessageStateNotification](./criticalmessagestatenotification.md)
  A structure that contains information about a critical SMS message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/smsservice/criticalmessagestatenotifications)*