# init(wasFollowingGuidance:guidanceToken:)

**Framework**: EnergyKit  
**Kind**: init

Initialize the GuidanceState for the [`ElectricHVACLoadEvent`](electrichvacloadevent.md)

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+
- macOS 26.0+

## Declaration

```swift
init(wasFollowingGuidance: Bool, guidanceToken: UUID)
```

## Parameters

- `wasFollowingGuidance`: Whether the device was applying    for its energy use at the time of the event.
- `guidanceToken`: The token provided at time of   fetch.

## See Also

- [var guidanceToken: UUID](electrichvacloadevent/session-swift.struct/guidancestate-swift.struct/guidancetoken.md)
  The guidance token for the guidance that you requested.
- [let wasFollowingGuidance: Bool](electrichvacloadevent/session-swift.struct/guidancestate-swift.struct/wasfollowingguidance.md)
  A Boolean value that indicates whether the device was applying the electricity guidance at the time of the event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/energykit/electrichvacloadevent/session-swift.struct/guidancestate-swift.struct/init(wasfollowingguidance:guidancetoken:))*