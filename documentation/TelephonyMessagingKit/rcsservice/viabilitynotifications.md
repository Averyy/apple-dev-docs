# viabilityNotifications

**Framework**: TelephonyMessagingKit  
**Kind**: property

An asynchronous sequence of service viability notifications produced by the service.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+

## Declaration

```swift
final var viabilityNotifications: some AsyncSequence<RCSService.ViabilityNotification, Never> { get throws }
```

#### Discussion

Use a `for`-`await`-`in` loop to receive [`RCSService.ViabilityNotification`](rcsservice/viabilitynotification.md) instances from this property.

## See Also

- [func isViable(for: CellularServiceID) -> Bool](rcsservice/isviable(for:).md)
  Queries whether the device can perform RCS operations at this time.
- [RCSService.ViabilityNotification](rcsservice/viabilitynotification.md)
  A notification that indicates whether RCS is viable for a given cellular service.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/rcsservice/viabilitynotifications)*