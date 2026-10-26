# maximumDistanceFuel

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The maximum rated distance the fuel-powered vehicle can travel with a full tank of fuel.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
var maximumDistanceFuel: Measurement<UnitLength>? { get set }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readwrite, nullable) NSMeasurement<NSUnitLength *> * maximumDistanceFuel;
```

*macOS*

```objc
@property (atomic, copy, readwrite, nullable) NSMeasurement<NSUnitLength *> * maximumDistanceFuel;
```

#### Discussion

Due to driving characteristics, this value can change over time when the vehicle’s in motion.

## See Also

### Providing Fuel, Charge, and Distance Information
- [var chargePercentRemaining: Float?](./chargepercentremaining-51zwv.md)
  The percentage of charge that remains for the electric vehicle.
- [var fuelPercentRemaining: Float?](./fuelpercentremaining-56xw3.md)
  The percentage of fuel that remains for the fuel-powered vehicle.
- [var maximumDistance: Measurement<UnitLength>?](./maximumdistance.md)
  The maximum rated distance the vehicle can travel with full resources.
- [var distanceRemaining: Measurement<UnitLength>?](./distanceremaining.md)
  The maximum distance the vehicle can travel with the remaining resources.
- [var maximumDistanceElectric: Measurement<UnitLength>?](./maximumdistanceelectric.md)
  The maximum rated distance the electric vehicle can travel on a full charge.
- [var distanceRemainingElectric: Measurement<UnitLength>?](./distanceremainingelectric.md)
  The maximum distance the electric vehicle can travel with the remaining charge.
- [var distanceRemainingFuel: Measurement<UnitLength>?](./distanceremainingfuel.md)
  The maximum distance the fuel-powered vehicle can travel with the remaining fuel.
- [chargePercentRemaining](./chargepercentremaining-30zol.md)
  The percentage of charge that remains for the electric vehicle.
- [fuelPercentRemaining](./fuelpercentremaining-6mdv4.md)
  The percentage of fuel remaining for the fuel-powered vehicle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/ingetcarpowerlevelstatusintentresponse/maximumdistancefuel)*