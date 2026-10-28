# session

**Framework**: EnergyKit  
**Kind**: property  
**Role**: Instance Property

The session information.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst

## Declaration

```swift
let session: ElectricHVACLoadEvent.Session
```

## Discussion

An HVAC system between its cooling or heating cycles can be idling and load events must not be generated

## See Also

### Getting load event information
- [let id: UUID](./id.md)
  The unique identifier of the electrical load event.
- [let timestamp: Date](./timestamp.md)
  The timestamp for when the event occurred.
- [ElectricHVACLoadEvent.Session](./session-swift.struct.md)
  A session that tracks the event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/energykit/electrichvacloadevent/session-swift.property)*