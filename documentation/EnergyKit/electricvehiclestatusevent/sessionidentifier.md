# sessionIdentifier

**Framework**: EnergyKit  
**Kind**: property  
**Role**: Instance Property

A unique identifier for the session.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst

## Declaration

```swift
let sessionIdentifier: UUID?
```

## Discussion

Provide the session identifier if the status event corresponds to an active charging session. The session identifier associates status snapshots with session-based energy flow data.

## See Also

### Identifying the event
- [let id: UUID](./id.md)
  A unique identifier for the status event.
- [let timestamp: Date](./timestamp.md)
  The time when the status event occurs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/energykit/electricvehiclestatusevent/sessionidentifier)*