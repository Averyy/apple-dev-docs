# ElectricHVACLoadEvent.Session.GuidanceState

**Framework**: EnergyKit  
**Kind**: struct

Identifies the provided guidance and its usability by the load device

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+
- macOS 26.0+

## Declaration

```swift
struct GuidanceState
```

## Topics

### Checking the guidance state
- [init(wasFollowingGuidance: Bool, guidanceToken: UUID)](electrichvacloadevent/session-swift.struct/guidancestate-swift.struct/init(wasfollowingguidance:guidancetoken:).md)
  Initialize the GuidanceState for the [`ElectricHVACLoadEvent`](electrichvacloadevent.md)
- [var guidanceToken: UUID](electrichvacloadevent/session-swift.struct/guidancestate-swift.struct/guidancetoken.md)
  The guidance token for the guidance that you requested.
- [let wasFollowingGuidance: Bool](electrichvacloadevent/session-swift.struct/guidancestate-swift.struct/wasfollowingguidance.md)
  A Boolean value that indicates whether the device was applying the electricity guidance at the time of the event.

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [let guidanceState: ElectricHVACLoadEvent.Session.GuidanceState](electrichvacloadevent/session-swift.struct/guidancestate-swift.property.md)
  Identifies the provided guidance and its usability by the load device


---

*[View on Apple Developer](https://developer.apple.com/documentation/energykit/electrichvacloadevent/session-swift.struct/guidancestate-swift.struct)*