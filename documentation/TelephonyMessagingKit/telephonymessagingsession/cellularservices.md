# cellularServices

**Framework**: TelephonyMessagingKit  
**Kind**: property  
**Role**: Instance Property

An array of cellular services available on the system.

**Availability**:
- iOS 26.0+

## Declaration

```swift
final var cellularServices: [CellularServiceState] { get throws }
```

## Mentions

- [Creating a carrier messaging app](../creating-a-carrier-messaging-app.md)

#### Discussion

To receive notification of changes to the available services, monitor the [`cellularServiceStateUpdates`](./cellularservicestateupdates.md) property.

## See Also

### Determining service availability
- [var cellularServiceStateUpdates: some AsyncSequence<CellularServiceState, Never>](./cellularservicestateupdates.md)
  An asynchronous sequence of cellular service state updates produced by this session.
- [struct CellularServiceState](../cellularservicestate.md)
  A structure that contains information about a cellular service.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/telephonymessagingsession/cellularservices)*