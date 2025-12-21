# guidance(using:at:)

**Framework**: EnergyKit  
**Kind**: method

Returns an async sequence of electricity guidance forecasts for the requested venue with cost information incorporated, if available.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+
- macOS 26.0+

## Declaration

```swift
final func guidance(using query: ElectricityGuidance.Query, at energyVenueID: UUID) -> some AsyncSequence<ElectricityGuidance, any Error>
```

#### Return Value

Returns an `AsyncSequence` of [`ElectricityGuidance`](electricityguidance.md) forecasts with error type [`EnergyKitError.guidanceUnavailable`](energykiterror/guidanceunavailable.md).

## Parameters

- `query`: The   that you request.
- `energyVenueID`: The   at which the devices consume electricity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/energykit/electricityguidance/service/guidance(using:at:))*