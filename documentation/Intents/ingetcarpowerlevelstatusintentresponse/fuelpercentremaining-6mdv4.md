# fuelPercentRemaining

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The percentage of fuel remaining for the fuel-powered vehicle.

**Availability**:
- iOS 10.3+
- iPadOS 10.3+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readwrite, nullable) NSNumber * fuelPercentRemaining;
```

*macOS*

```objc
@property (atomic, copy, readwrite, nullable) NSNumber * fuelPercentRemaining;
```

## Discussion

Typically, you assign a value to this property only after handling the intent.

## See Also

### Providing Fuel, Charge, and Distance Information
- [chargePercentRemaining](./chargepercentremaining-30zol.md)
  The percentage of charge that remains for the electric vehicle.
- [var maximumDistance: Measurement<UnitLength>?](./maximumdistance.md)
  The maximum rated distance the vehicle can travel with full resources.
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

*[View on Apple Developer](https://developer.apple.com/documentation/intents/ingetcarpowerlevelstatusintentresponse/fuelpercentremaining-6mdv4)*