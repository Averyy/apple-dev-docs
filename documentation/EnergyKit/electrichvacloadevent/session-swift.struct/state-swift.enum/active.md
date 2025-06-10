# ElectricHVACLoadEvent.Session.State.active

**Framework**: EnergyKit  
**Kind**: case

A state that represents all electricity consumption events with active states.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+
- macOS 26.0+ (Beta)

## Declaration

```swift
case active
```

#### Discussion

The events are relative to the begin state corresponding to the `begin` events session ID.

## See Also

- [ElectricHVACLoadEvent.Session.State.begin](electrichvacloadevent/session-swift.struct/state-swift.enum/begin.md)
  A state that represents the start of the session.
- [ElectricHVACLoadEvent.Session.State.end](electrichvacloadevent/session-swift.struct/state-swift.enum/end.md)
  The end of the session when a load device goes to idle, that is, power/stage returns to zero indicating the load device is no longer consuming or generating electricity A state that represents the end of the session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/energykit/electrichvacloadevent/session-swift.struct/state-swift.enum/active)*