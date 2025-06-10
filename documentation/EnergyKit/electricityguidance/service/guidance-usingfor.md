# guidance(using:for:)

**Framework**: EnergyKit  
**Kind**: method

Returns an async sequence of electricity guidance forecasts without cost information incorporated.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+
- macOS 26.0+ (Beta)

## Declaration

```swift
final func guidance(using query: ElectricityGuidance.Query, for location: CLLocation) -> some AsyncSequence<ElectricityGuidance, any Error>
```

#### Return Value

An `AsyncSequence` of [`ElectricityGuidance`](electricityguidance.md) forecasts with error type [`EnergyKitError.guidanceUnavailable`](energykiterror/guidanceunavailable.md).

#### Discussion

An electric vehicle charging away from home is an example of a location.

## Parameters

- `query`: The   that you request.
- `location`: The location at which the devices consume electricity.

## See Also

- [func guidance(using: ElectricityGuidance.Query, at: UUID) -> some AsyncSequence<ElectricityGuidance, any Error>
](electricityguidance/service/guidance(using:at:).md)
  Returns an async sequence of electricity guidance forecasts for the requested venue with cost information incorporated, if available.


---

*[View on Apple Developer](https://developer.apple.com/documentation/energykit/electricityguidance/service/guidance(using:for:))*