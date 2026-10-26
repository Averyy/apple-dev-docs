# chargePercentRemaining

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The percentage of charge that remains for the electric vehicle.

**Availability**:
- iOS 10.3+
- iPadOS 10.3+
- Mac Catalyst 10.3+
- watchOS 3.2+

## Declaration

```swift
@nonobjc
final var chargePercentRemaining: Float? { get set }
```

#### Discussion

Typically, you assign a value to this property only after handling the intent.

## See Also

### Providing Fuel, Charge, and Distance Information
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
- [var maximumDistanceFuel: Measurement<UnitLength>?](./maximumdistancefuel.md)
  The maximum rated distance the fuel-powered vehicle can travel with a full tank of fuel.
- [var distanceRemainingFuel: Measurement<UnitLength>?](./distanceremainingfuel.md)
  The maximum distance the fuel-powered vehicle can travel with the remaining fuel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/ingetcarpowerlevelstatusintentresponse/chargepercentremaining-51zwv)*