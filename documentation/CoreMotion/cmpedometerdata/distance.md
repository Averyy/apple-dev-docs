# distance

**Framework**: Core Motion  
**Kind**: property  
**Role**: Instance Property

The estimated distance (in meters) traveled by the user.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- watchOS 2.0+

## Declaration

```swift
var distance: NSNumber? { get }
```

```objc
@property (nonatomic, readonly, nullable) NSNumber * distance;
```

## Discussion

This value reflects the distance traveled while walking and running. The value in this property may be `nil` if distance estimation is not supported on the current device.

## See Also

### Getting the Pedestrian Data
- [var numberOfSteps: NSNumber](./numberofsteps.md)
  The number of steps taken by the user.
- [var averageActivePace: NSNumber?](./averageactivepace.md)
  The average pace of the user, measured in seconds per meter.
- [var currentPace: NSNumber?](./currentpace.md)
  The current pace of the user, measured in seconds per meter.
- [var currentCadence: NSNumber?](./currentcadence.md)
  The rate at which steps are taken, measured in steps per second.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmpedometerdata/distance)*