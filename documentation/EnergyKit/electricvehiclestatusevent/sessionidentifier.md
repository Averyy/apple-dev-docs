# sessionIdentifier

**Framework**: EnergyKit  
**Kind**: property

A unique identifier for the session.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst ?+

## Declaration

```swift
let sessionIdentifier: UUID?
```

#### Discussion

Provide the session identifier if the status event corresponds to an active charging session. The session identifier associates status snapshots with session-based energy flow data.

## See Also

- [let id: UUID](electricvehiclestatusevent/id.md)
  A unique identifier for the status event.
- [let timestamp: Date](electricvehiclestatusevent/timestamp.md)
  The time when the status event occurs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/energykit/electricvehiclestatusevent/sessionidentifier)*