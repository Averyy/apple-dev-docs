# SMSService.ViabilityNotification

**Framework**: TelephonyMessagingKit  
**Kind**: struct  
**Role**: Structure

A notification that indicates whether SMS is viable for a given cellular service.

**Availability**:
- iOS 26.0+

## Declaration

```swift
struct ViabilityNotification
```

## Topics

### Accessing notification properties
- [let cellularServiceID: CellularServiceID](./viabilitynotification/cellularserviceid.md)
  The cellular service identifier associated with the notification.
- [let isViable: Bool](./viabilitynotification/isviable.md)
  A Boolean value that indicates whether the device can peform SMS operations at this time.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Determining service viabililty
- [func isViable(for: CellularServiceID) -> Bool](./isviable%28for%29.md)
  Queries whether the device can perform SMS operations at this time.
- [var viabilityNotifications: some AsyncSequence<SMSService.ViabilityNotification, Never>](./viabilitynotifications.md)
  An asynchronous sequence of service viability notifications produced by this service.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/smsservice/viabilitynotification)*