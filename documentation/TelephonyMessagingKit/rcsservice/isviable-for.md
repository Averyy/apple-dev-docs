# isViable(for:)

**Framework**: TelephonyMessagingKit  
**Kind**: method

Queries whether the device can perform RCS operations at this time.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+

## Declaration

```swift
final func isViable(for cellularServiceID: CellularServiceID) -> Bool
```

#### Return Value

`true` if RCS is currently viable for the cellular service; `false`, otherwise.

## Parameters

- `cellularServiceID`: The cellular service identifier for which to check RCS viability.

## See Also

- [var viabilityNotifications: some AsyncSequence<RCSService.ViabilityNotification, Never>](rcsservice/viabilitynotifications.md)
  An asynchronous sequence of service viability notifications produced by the service.
- [RCSService.ViabilityNotification](rcsservice/viabilitynotification.md)
  A notification that indicates whether RCS is viable for a given cellular service.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/rcsservice/isviable(for:))*