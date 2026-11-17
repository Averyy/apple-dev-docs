# distanceRemaining

**Framework**: CarPlay  
**Kind**: property  
**Role**: Instance Property

The remaining distance for the travel estimate.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
var distanceRemaining: Measurement<UnitLength> { get }
```

```objc
@property (nonatomic, copy, readonly) NSMeasurement<NSUnitLength *> * distanceRemaining;
```

## See Also

### Getting travel estimates
- [var distanceRemainingToDisplay: Measurement<UnitLength>](./distanceremainingtodisplay.md)
  The distance remaining that the framework displays to a person, in the default units of measurement.
- [var timeRemaining: TimeInterval](./timeremaining.md)
  The remaining time for the travel estimate.
- [var routeDetails: [CPRouteDetail]](./routedetails.md)
  Additional trip information such as battery, fuel, or toll information to display with travel estimates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cptravelestimates/distanceremaining)*