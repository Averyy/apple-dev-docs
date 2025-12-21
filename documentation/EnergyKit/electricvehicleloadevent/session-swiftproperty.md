# session

**Framework**: EnergyKit  
**Kind**: property

The session information.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+
- macOS 26.0+

## Declaration

```swift
let session: ElectricVehicleLoadEvent.Session
```

#### Discussion

An electric vehicle between charging or discharging sessions can be idling and load events must not be generated

## See Also

- [let id: UUID](electricvehicleloadevent/id.md)
  The unique identifier of the electrical load event.
- [let timestamp: Date](electricvehicleloadevent/timestamp.md)
  The timestamp for when the event occurred.


---

*[View on Apple Developer](https://developer.apple.com/documentation/energykit/electricvehicleloadevent/session-swift.property)*