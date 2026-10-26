# maximumBatteryCapacity

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

A user-facing value that represents the maximum battery capacity of the electric vehicle.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
var maximumBatteryCapacity: Measurement<UnitEnergy>? { get set }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readwrite, nullable) NSMeasurement<NSUnitEnergy *> * maximumBatteryCapacity;
```

*macOS*

```objc
@property (atomic, copy, readwrite, nullable) NSMeasurement<NSUnitEnergy *> * maximumBatteryCapacity;
```

#### Discussion

The value the system displays to the user as 100% battery charge. It can never be less than that of [`currentBatteryCapacity`](./currentbatterycapacity.md).

## See Also

### Providing Battery Capacity
- [var minimumBatteryCapacity: Measurement<UnitEnergy>?](./minimumbatterycapacity.md)
  A user-facing value that represents the minimum battery capacity of the electric vehicle.
- [var currentBatteryCapacity: Measurement<UnitEnergy>?](./currentbatterycapacity.md)
  A user-facing value that represents the current battery capacity of the electric vehicle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/ingetcarpowerlevelstatusintentresponse/maximumbatterycapacity)*