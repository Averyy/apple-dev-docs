# distanceRemaining

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The maximum distance the vehicle can travel with the remaining resources.

**Availability**:
- iOS 10.3+
- iPadOS 10.3+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
var distanceRemaining: Measurement<UnitLength>? { get set }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readwrite, nullable) NSMeasurement<NSUnitLength *> * distanceRemaining;
```

*macOS*

```objc
@property (atomic, copy, readwrite, nullable) NSMeasurement<NSUnitLength *> * distanceRemaining;
```

## Discussion

For an electric vehicle, this value is the same as [`distanceRemainingElectric`](./distanceremainingelectric.md). For a fuel-powered vehicle, this value is the same as `distanceRemainingGasoline`. For a hybrid vehicle, this value is the sum of `distanceRemainingElectric` and `distanceRemainingGasoline`.

As a result of driving characteristics, this value can change over time when the vehicle’s in motion.

## See Also

### Providing Fuel, Charge, and Distance Information
- [var chargePercentRemaining: Float?](./chargepercentremaining-51zwv.md)
  The percentage of charge that remains for the electric vehicle.
- [var fuelPercentRemaining: Float?](./fuelpercentremaining-56xw3.md)
  The percentage of fuel that remains for the fuel-powered vehicle.
- [var maximumDistance: Measurement<UnitLength>?](./maximumdistance.md)
  The maximum rated distance the vehicle can travel with full resources.
- [var maximumDistanceElectric: Measurement<UnitLength>?](./maximumdistanceelectric.md)
  The maximum rated distance the electric vehicle can travel on a full charge.
- [var distanceRemainingElectric: Measurement<UnitLength>?](./distanceremainingelectric.md)
  The maximum distance the electric vehicle can travel with the remaining charge.
- [var maximumDistanceFuel: Measurement<UnitLength>?](./maximumdistancefuel.md)
  The maximum rated distance the fuel-powered vehicle can travel with a full tank of fuel.
- [var distanceRemainingFuel: Measurement<UnitLength>?](./distanceremainingfuel.md)
  The maximum distance the fuel-powered vehicle can travel with the remaining fuel.
- [chargePercentRemaining](./chargepercentremaining-30zol.md)
  The percentage of charge that remains for the electric vehicle.
- [fuelPercentRemaining](./fuelpercentremaining-6mdv4.md)
  The percentage of fuel remaining for the fuel-powered vehicle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/ingetcarpowerlevelstatusintentresponse/distanceremaining)*