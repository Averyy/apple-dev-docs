# isViable(for:)

**Framework**: TelephonyMessagingKit  
**Kind**: method

Queries whether the device can perform SMS operations at this time.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+

## Declaration

```swift
final func isViable(for cellularServiceID: CellularServiceID) -> Bool
```

#### Return Value

`true` if SMS is currently viabale for the given cellular service; `false`, otherwise.

## Parameters

- `cellularServiceID`: The cellular service identifier for which to check SMS viability.

## See Also

- [var viabilityNotifications: some AsyncSequence<SMSService.ViabilityNotification, Never>](smsservice/viabilitynotifications.md)
  An asynchronous sequence of service viability notifications produced by this service.
- [SMSService.ViabilityNotification](smsservice/viabilitynotification.md)
  A notification that indicates whether SMS is viable for a given cellular service.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/smsservice/isviable(for:))*