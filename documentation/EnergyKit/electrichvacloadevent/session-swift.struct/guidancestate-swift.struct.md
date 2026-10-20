# ElectricHVACLoadEvent.Session.GuidanceState

**Framework**: EnergyKit  
**Kind**: struct  
**Role**: Structure

Identifies the provided guidance and its usability by the load device

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst

## Declaration

```swift
struct GuidanceState
```

## Topics

### Checking the guidance state
- [init(wasFollowingGuidance: Bool, guidanceToken: UUID)](./guidancestate-swift.struct/init%28wasfollowingguidance,guidancetoken%29.md)
  Initialize the GuidanceState for the [`ElectricHVACLoadEvent`](../../electrichvacloadevent.md)
- [var guidanceToken: UUID](./guidancestate-swift.struct/guidancetoken.md)
  The guidance token for the guidance that you requested.
- [let wasFollowingGuidance: Bool](./guidancestate-swift.struct/wasfollowingguidance.md)
  A Boolean value that indicates whether the device was applying the electricity guidance at the time of the event.

## Relationships

### Conforms To
- [Decodable](../../../Swift/decodable.md)
- [Encodable](../../../Swift/encodable.md)
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)

## See Also

### Identifying the guidance state
- [let guidanceState: ElectricHVACLoadEvent.Session.GuidanceState](./guidancestate-swift.property.md)
  Identifies the provided guidance and its usability by the load device


---

*[View on Apple Developer](https://developer.apple.com/documentation/energykit/electrichvacloadevent/session-swift.struct/guidancestate-swift.struct)*