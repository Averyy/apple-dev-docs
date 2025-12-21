# cellularServices

**Framework**: TelephonyMessagingKit  
**Kind**: property

An array of cellular services available on the system.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+

## Declaration

```swift
final var cellularServices: [CellularServiceState] { get throws }
```

## Mentions

- [Creating a carrier messaging app](../availability/creating-a-carrier-messaging-app.md)

#### Discussion

To receive notification of changes to the available services, monitor the [`cellularServiceStateUpdates`](telephonymessagingsession/cellularservicestateupdates.md) property.

## See Also

- [var cellularServiceStateUpdates: some AsyncSequence<CellularServiceState, Never>](telephonymessagingsession/cellularservicestateupdates.md)
  An asynchronous sequence of cellular service state updates produced by this session.
- [struct CellularServiceState](cellularservicestate.md)
  A structure that contains information about a cellular service.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/telephonymessagingsession/cellularservices)*