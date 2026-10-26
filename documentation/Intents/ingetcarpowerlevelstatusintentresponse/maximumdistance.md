# maximumDistance

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The maximum rated distance the vehicle can travel with full resources.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
var maximumDistance: Measurement<UnitLength>? { get set }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readwrite, nullable) NSMeasurement<NSUnitLength *> * maximumDistance;
```

*macOS*

```objc
@property (atomic, copy, readwrite, nullable) NSMeasurement<NSUnitLength *> * maximumDistance;
```

#### Discussion

For an electric vehicle, this value is the same as [`distanceRemainingElectric`](./distanceremainingelectric.md). For a fuel-powered vehicle, this value is the same as [`distanceRemainingFuel`](./distanceremainingfuel.md). For a hybrid vehicle, this value is the sum of `distanceRemainingElectric` and `distanceRemainingFuel`.

Due to driving characteristics, this value can change over time when the vehicle’s in motion.

## See Also

### Providing Fuel, Charge, and Distance Information
- [var chargePercentRemaining: Float?](./chargepercentremaining-51zwv.md)
  The percentage of charge that remains for the electric vehicle.
- [var fuelPercentRemaining: Float?](./fuelpercentremaining-56xw3.md)
  The percentage of fuel that remains for the fuel-powered vehicle.
- [var distanceRemaining: Measurement<UnitLength>?](./distanceremaining.md)
  The maximum distance the vehicle can travel with the remaining resources.
- [var maximumDistanceElectric: Measurement<UnitLength>?](./maximumdistanceelectric.md)
  The maximum rated distance the electric vehicle can travel on a full charge.
- [var distanceRemainingElectric: Measurement<UnitLength>?](./distanceremainingelectric.md)
  The maximum distance the electric vehicle can travel with the remaining charge.
- [var maximumDistanceFuel: Measurement<UnitLength>?](./maximumdistancefuel.md)
  The maximum rated distance the fuel-powered vehicle can travel with a full tank of fuel.
- [var distanceRemainingFuel: Measurement<UnitLength>?](./distanceremainingfuel.md)
  The maximum distance the fuel-powered vehicle can travel with the remaining fuel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/ingetcarpowerlevelstatusintentresponse/maximumdistance)*