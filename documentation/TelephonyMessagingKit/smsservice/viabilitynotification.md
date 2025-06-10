# SMSService.ViabilityNotification

**Framework**: TelephonyMessagingKit  
**Kind**: struct

A notification that indicates whether SMS is viable for a given cellular service.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+

## Declaration

```swift
struct ViabilityNotification
```

## Topics

### Accessing notification properties
- [let cellularServiceID: CellularServiceID](smsservice/viabilitynotification/cellularserviceid.md)
  The cellular service identifier associated with the notification.
- [let isViable: Bool](smsservice/viabilitynotification/isviable.md)
  A Boolean value that indicates whether the device can peform SMS operations at this time.
### Operators
- [static func == (SMSService.ViabilityNotification, SMSService.ViabilityNotification) -> Bool](smsservice/viabilitynotification/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Default Implementations
- [Equatable Implementations](smsservice/viabilitynotification/equatable-implementations.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func isViable(for: CellularServiceID) -> Bool](smsservice/isviable(for:).md)
  Queries whether the device can perform SMS operations at this time.
- [var viabilityNotifications: some AsyncSequence<SMSService.ViabilityNotification, Never>](smsservice/viabilitynotifications.md)
  An asynchronous sequence of service viability notifications produced by this service.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/smsservice/viabilitynotification)*