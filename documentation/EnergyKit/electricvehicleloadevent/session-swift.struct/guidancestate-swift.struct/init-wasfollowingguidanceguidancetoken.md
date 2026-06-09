# init(wasFollowingGuidance:guidanceToken:)

**Framework**: EnergyKit  
**Kind**: init

Initialize the GuidanceState for the [`ElectricVehicleLoadEvent`](electricvehicleloadevent.md)

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+

## Declaration

```swift
init(wasFollowingGuidance: Bool, guidanceToken: UUID)
```

## Parameters

- `wasFollowingGuidance`: Whether the device was applying [`ElectricityGuidance`](electricityguidance.md) for its energy use at the time of the event.
- `guidanceToken`: The token provided at time of [`ElectricityGuidance`](electricityguidance.md) fetch.


---

*[View on Apple Developer](https://developer.apple.com/documentation/energykit/electricvehicleloadevent/session-swift.struct/guidancestate-swift.struct/init(wasfollowingguidance:guidancetoken:))*