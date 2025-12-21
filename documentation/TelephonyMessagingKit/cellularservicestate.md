# CellularServiceState

**Framework**: TelephonyMessagingKit  
**Kind**: struct

A structure that contains information about a cellular service.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+

## Declaration

```swift
struct CellularServiceState
```

## Mentions

- [Creating a carrier messaging app](../availability/creating-a-carrier-messaging-app.md)

## Topics

### Accessing state properties
- [let id: CellularServiceID](cellularservicestate/id.md)
  The cellular service identifier associated with this instance.
- [struct CellularServiceID](cellularserviceid.md)
  An opaque identifier that represents the cellular service for which to provide operations.
- [let label: String](cellularservicestate/label.md)
  The label for a service, as set by the person using the device.

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Identifiable](../Swift/Identifiable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var cellularServices: [CellularServiceState]](telephonymessagingsession/cellularservices.md)
  An array of cellular services available on the system.
- [var cellularServiceStateUpdates: some AsyncSequence<CellularServiceState, Never>](telephonymessagingsession/cellularservicestateupdates.md)
  An asynchronous sequence of cellular service state updates produced by this session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/cellularservicestate)*