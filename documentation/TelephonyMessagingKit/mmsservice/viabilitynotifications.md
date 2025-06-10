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
final var viabilityNotifications: some AsyncSequence<MMSService.ViabilityNotification, Never> { get throws }
```

#### Discussion

Use a `for`-`await`-`in` loop to receive [`MMSService.ViabilityNotification`](mmsservice/viabilitynotification.md) instances from this property.

## See Also

- [func isViable(for: CellularServiceID) -> Bool](mmsservice/isviable(for:).md)
  Queries whether the device can perform MMS operations at this time.
- [MMSService.ViabilityNotification](mmsservice/viabilitynotification.md)
  A notification that indicates if MMS is viable for a given cellular service.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/mmsservice/viabilitynotifications)*