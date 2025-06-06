# currentCadence

**Framework**: Core Motion  
**Kind**: property

The rate at which steps are taken, measured in steps per second.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- watchOS 2.0+

## Declaration

```swift
var currentCadence: NSNumber? { get }
```

#### Discussion

During regular updates, this property is set to the user’s cadence. The value in this property is `nil` when you are performing a query for historical pedometer data or when cadence information is not yet available for the user. This property is also `nil` for devices that do not support the gathering of cadence data.

## See Also

- [var numberOfSteps: NSNumber](cmpedometerdata/numberofsteps.md)
  The number of steps taken by the user.
- [var distance: NSNumber?](cmpedometerdata/distance.md)
  The estimated distance (in meters) traveled by the user.
- [var averageActivePace: NSNumber?](cmpedometerdata/averageactivepace.md)
  The average pace of the user, measured in seconds per meter.
- [var currentPace: NSNumber?](cmpedometerdata/currentpace.md)
  The current pace of the user, measured in seconds per meter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmpedometerdata/currentcadence)*