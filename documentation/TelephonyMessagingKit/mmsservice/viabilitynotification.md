# MMSService.ViabilityNotification

**Framework**: TelephonyMessagingKit  
**Kind**: struct

A notification that indicates if MMS is viable for a given cellular service.

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
- [let cellularServiceID: CellularServiceID](mmsservice/viabilitynotification/cellularserviceid.md)
  The cellular service identifier associated with this notification.
- [let isViable: Bool](mmsservice/viabilitynotification/isviable.md)
  A Boolean value that indicates whether the device can peform MMS operations at this time.
### Comparing notifications
- [static func == (MMSService.ViabilityNotification, MMSService.ViabilityNotification) -> Bool](mmsservice/viabilitynotification/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Default Implementations
- [Equatable Implementations](mmsservice/viabilitynotification/equatable-implementations.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func isViable(for: CellularServiceID) -> Bool](mmsservice/isviable(for:).md)
  Queries whether the device can perform MMS operations at this time.
- [var viabilityNotifications: some AsyncSequence<MMSService.ViabilityNotification, Never>](mmsservice/viabilitynotifications.md)
  An asynchronous sequence of service viability notifications produced by the service.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/mmsservice/viabilitynotification)*