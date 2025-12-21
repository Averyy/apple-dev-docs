# ElectricHVACLoadEvent.Session.State.begin

**Framework**: EnergyKit  
**Kind**: case

A state that represents the start of the session.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+
- macOS 26.0+

## Declaration

```swift
case begin
```

#### Discussion

The electricity measurement stage must be 0

## See Also

- [ElectricHVACLoadEvent.Session.State.active](electrichvacloadevent/session-swift.struct/state-swift.enum/active.md)
  A state that represents all electricity consumption events with active states.
- [ElectricHVACLoadEvent.Session.State.end](electrichvacloadevent/session-swift.struct/state-swift.enum/end.md)
  The end of the session when a load device goes to idle, that is, power/stage returns to zero indicating the load device is no longer consuming or generating electricity A state that represents the end of the session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/energykit/electrichvacloadevent/session-swift.struct/state-swift.enum/begin)*