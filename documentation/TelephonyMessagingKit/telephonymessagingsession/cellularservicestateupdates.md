# cellularServiceStateUpdates

**Framework**: TelephonyMessagingKit  
**Kind**: property

An asynchronous sequence of cellular service state updates produced by this session.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+

## Declaration

```swift
final var cellularServiceStateUpdates: some AsyncSequence<CellularServiceState, Never> { get }
```

#### Discussion

Use a `for`-`await`-`in` loop to iterate over this asynchronous sequence and receive updates about service availability.

## See Also

- [var cellularServices: [CellularServiceState]](telephonymessagingsession/cellularservices.md)
  An array of cellular services available on the system.
- [struct CellularServiceState](cellularservicestate.md)
  A structure that contains information about a cellular service.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/telephonymessagingsession/cellularservicestateupdates)*