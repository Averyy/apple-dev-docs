# timeRemaining

**Framework**: CarPlay  
**Kind**: property  
**Role**: Instance Property

The remaining time for the travel estimate.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
var timeRemaining: TimeInterval { get }
```

```objc
@property (nonatomic, assign, readonly) NSTimeInterval timeRemaining;
```

## See Also

### Getting travel estimates
- [var distanceRemaining: Measurement<UnitLength>](./distanceremaining.md)
  The remaining distance for the travel estimate.
- [var distanceRemainingToDisplay: Measurement<UnitLength>](./distanceremainingtodisplay.md)
  The distance remaining that the framework displays to a person, in the default units of measurement.
- [var routeDetails: [CPRouteDetail]](./routedetails.md)
  Additional trip information such as battery, fuel, or toll information to display with travel estimates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cptravelestimates/timeremaining)*