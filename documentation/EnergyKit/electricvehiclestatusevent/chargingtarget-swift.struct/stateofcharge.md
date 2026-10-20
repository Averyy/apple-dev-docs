# stateOfCharge

**Framework**: EnergyKit  
**Kind**: property  
**Role**: Instance Property

Target state of charge for this charging session (0-100)

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst

## Declaration

```swift
let stateOfCharge: Int
```

## See Also

### Getting target information
- [let estimatedCompletionTime: Date](./estimatedcompletiontime.md)
  An estimated time of when charging completes.
- [let scheduledStartTime: Date](./scheduledstarttime.md)
  A scheduled time for when charging starts.
- [let estimatedRangeAtTarget: Measurement<UnitLength>?](./estimatedrangeattarget.md)
  An estimated range of driving distance for the target state of charge.


---

*[View on Apple Developer](https://developer.apple.com/documentation/energykit/electricvehiclestatusevent/chargingtarget-swift.struct/stateofcharge)*