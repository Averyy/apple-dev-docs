# guidanceToken

**Framework**: EnergyKit  
**Kind**: property  
**Role**: Instance Property

The guidance token for the guidance that you requested.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst

## Declaration

```swift
var guidanceToken: UUID
```

## See Also

### Checking the guidance state
- [init(wasFollowingGuidance: Bool, guidanceToken: UUID)](./init%28wasfollowingguidance,guidancetoken%29.md)
  Initialize the GuidanceState for the [`ElectricHVACLoadEvent`](../../../electrichvacloadevent.md)
- [let wasFollowingGuidance: Bool](./wasfollowingguidance.md)
  A Boolean value that indicates whether the device was applying the electricity guidance at the time of the event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/energykit/electrichvacloadevent/session-swift.struct/guidancestate-swift.struct/guidancetoken)*