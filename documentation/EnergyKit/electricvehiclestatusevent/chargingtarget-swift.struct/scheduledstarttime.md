# scheduledStartTime

**Framework**: EnergyKit  
**Kind**: property  
**Role**: Instance Property

A scheduled time for when charging starts.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst

## Declaration

```swift
let scheduledStartTime: Date
```

## See Also

### Getting target information
- [let stateOfCharge: Int](./stateofcharge.md)
  Target state of charge for this charging session (0-100)
- [let estimatedCompletionTime: Date](./estimatedcompletiontime.md)
  An estimated time of when charging completes.
- [let estimatedRangeAtTarget: Measurement<UnitLength>?](./estimatedrangeattarget.md)
  An estimated range of driving distance for the target state of charge.


---

*[View on Apple Developer](https://developer.apple.com/documentation/energykit/electricvehiclestatusevent/chargingtarget-swift.struct/scheduledstarttime)*