# init(stateOfCharge:estimatedCompletionTime:scheduledStartTime:estimatedRangeAtTarget:)

**Framework**: EnergyKit  
**Kind**: init

Creates target information for the desired outcome of charging an electric vehicle.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst ?+

## Declaration

```swift
init(stateOfCharge: Int, estimatedCompletionTime: Date, scheduledStartTime: Date, estimatedRangeAtTarget: Measurement<UnitLength>? = nil)
```

## Parameters

- `stateOfCharge`: The target state of charge percentage (0-100).
- `estimatedCompletionTime`: The estimated time when charging completes.
- `scheduledStartTime`: The scheduled time when charging starts.
- `estimatedRangeAtTarget`: The estimated range at target state of charge, or `nil` if the range is unavailable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/energykit/electricvehiclestatusevent/chargingtarget-swift.struct/init(stateofcharge:estimatedcompletiontime:scheduledstarttime:estimatedrangeattarget:))*