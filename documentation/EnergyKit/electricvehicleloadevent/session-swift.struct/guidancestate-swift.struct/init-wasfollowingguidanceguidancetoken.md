# init(wasFollowingGuidance:guidanceToken:)

**Framework**: EnergyKit  
**Kind**: init

Initialize the GuidanceState for the [`ElectricVehicleLoadEvent`](electricvehicleloadevent.md)

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+
- macOS 26.0+ (Beta)

## Declaration

```swift
init(wasFollowingGuidance: Bool, guidanceToken: UUID)
```

## Parameters

- `wasFollowingGuidance`: Whether the device was applying    for its energy use at the time of the event.
- `guidanceToken`: The token provided at time of   fetch.


---

*[View on Apple Developer](https://developer.apple.com/documentation/energykit/electricvehicleloadevent/session-swift.struct/guidancestate-swift.struct/init(wasfollowingguidance:guidancetoken:))*