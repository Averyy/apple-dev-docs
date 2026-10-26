# currentBatteryCapacity

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

A user-facing value that represents the current battery capacity of the electric vehicle.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
var currentBatteryCapacity: Measurement<UnitEnergy>? { get set }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readwrite, nullable) NSMeasurement<NSUnitEnergy *> * currentBatteryCapacity;
```

*macOS*

```objc
@property (atomic, copy, readwrite, nullable) NSMeasurement<NSUnitEnergy *> * currentBatteryCapacity;
```

#### Discussion

The value the system displays to the user as the current percentage of battery charge. It must always be within the range of `minBatteryCapacity` and `maxBatteryCapacity`.

## See Also

### Providing Battery Capacity
- [var minimumBatteryCapacity: Measurement<UnitEnergy>?](./minimumbatterycapacity.md)
  A user-facing value that represents the minimum battery capacity of the electric vehicle.
- [var maximumBatteryCapacity: Measurement<UnitEnergy>?](./maximumbatterycapacity.md)
  A user-facing value that represents the maximum battery capacity of the electric vehicle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/ingetcarpowerlevelstatusintentresponse/currentbatterycapacity)*