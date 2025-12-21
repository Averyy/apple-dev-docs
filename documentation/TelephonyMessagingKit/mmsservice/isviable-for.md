# isViable(for:)

**Framework**: TelephonyMessagingKit  
**Kind**: method

Queries whether the device can perform MMS operations at this time.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+

## Declaration

```swift
final func isViable(for cellularServiceID: CellularServiceID) -> Bool
```

#### Return Value

`true` if MMS is currently viable for the cellular service; `false`, otherwise.

## Parameters

- `cellularServiceID`: The cellular service identifier for which to check MMS viability.

## See Also

- [var viabilityNotifications: some AsyncSequence<MMSService.ViabilityNotification, Never>](mmsservice/viabilitynotifications.md)
  An asynchronous sequence of service viability notifications produced by the service.
- [MMSService.ViabilityNotification](mmsservice/viabilitynotification.md)
  A notification that indicates if MMS is viable for a given cellular service.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/mmsservice/isviable(for:))*