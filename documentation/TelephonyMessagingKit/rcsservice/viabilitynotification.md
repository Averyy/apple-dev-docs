# RCSService.ViabilityNotification

**Framework**: TelephonyMessagingKit  
**Kind**: struct

A notification that indicates whether RCS is viable for a given cellular service.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+

## Declaration

```swift
struct ViabilityNotification
```

## Topics

### Operators
- [static func == (RCSService.ViabilityNotification, RCSService.ViabilityNotification) -> Bool](rcsservice/viabilitynotification/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Instance Properties
- [let cellularServiceID: CellularServiceID](rcsservice/viabilitynotification/cellularserviceid.md)
  The cellular service identifier associated with this notification.
- [let isViable: Bool](rcsservice/viabilitynotification/isviable.md)
  A Boolean value that indicates whether the device can peform RCS operations at this time.
### Default Implementations
- [Equatable Implementations](rcsservice/viabilitynotification/equatable-implementations.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func isViable(for: CellularServiceID) -> Bool](rcsservice/isviable(for:).md)
  Queries whether the device can perform RCS operations at this time.
- [var viabilityNotifications: some AsyncSequence<RCSService.ViabilityNotification, Never>](rcsservice/viabilitynotifications.md)
  An asynchronous sequence of service viability notifications produced by the service.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/rcsservice/viabilitynotification)*