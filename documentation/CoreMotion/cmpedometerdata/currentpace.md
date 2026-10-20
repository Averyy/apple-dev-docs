# currentPace

**Framework**: Core Motion  
**Kind**: property  
**Role**: Instance Property

The current pace of the user, measured in seconds per meter.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- watchOS 2.0+

## Declaration

```swift
var currentPace: NSNumber? { get }
```

```objc
@property (nonatomic, readonly, nullable) NSNumber * currentPace;
```

#### Discussion

During regular updates, this property is set to the user’s pace. The value in this property is `nil` when you are performing a query for historical pedometer data or when pace information is not yet available for the user. This property is also `nil` for devices that do not support the gathering of pace data.

## See Also

### Getting the Pedestrian Data
- [var numberOfSteps: NSNumber](./numberofsteps.md)
  The number of steps taken by the user.
- [var distance: NSNumber?](./distance.md)
  The estimated distance (in meters) traveled by the user.
- [var averageActivePace: NSNumber?](./averageactivepace.md)
  The average pace of the user, measured in seconds per meter.
- [var currentCadence: NSNumber?](./currentcadence.md)
  The rate at which steps are taken, measured in steps per second.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmpedometerdata/currentpace)*