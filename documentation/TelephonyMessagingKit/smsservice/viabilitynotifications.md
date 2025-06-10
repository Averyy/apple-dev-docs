# viabilityNotifications

**Framework**: TelephonyMessagingKit  
**Kind**: property

An asynchronous sequence of service viability notifications produced by this service.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+

## Declaration

```swift
final var viabilityNotifications: some AsyncSequence<SMSService.ViabilityNotification, Never> { get throws }
```

#### Discussion

Use a `for`-`await`-`in` loop to receive [`SMSService.ViabilityNotification`](smsservice/viabilitynotification.md) instances from this property.

## See Also

- [func isViable(for: CellularServiceID) -> Bool](smsservice/isviable(for:).md)
  Queries whether the device can perform SMS operations at this time.
- [SMSService.ViabilityNotification](smsservice/viabilitynotification.md)
  A notification that indicates whether SMS is viable for a given cellular service.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/smsservice/viabilitynotifications)*