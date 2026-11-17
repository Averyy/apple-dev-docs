# routeDetails

**Framework**: CarPlay  
**Kind**: property  
**Role**: Instance Property

Additional trip information such as battery, fuel, or toll information to display with travel estimates.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```swift
var routeDetails: [CPRouteDetail] { get }
```

```objc
@property (nonatomic, copy, readonly) NSArray<CPRouteDetail *> * routeDetails;
```

## See Also

### Getting travel estimates
- [var distanceRemaining: Measurement<UnitLength>](./distanceremaining.md)
  The remaining distance for the travel estimate.
- [var distanceRemainingToDisplay: Measurement<UnitLength>](./distanceremainingtodisplay.md)
  The distance remaining that the framework displays to a person, in the default units of measurement.
- [var timeRemaining: TimeInterval](./timeremaining.md)
  The remaining time for the travel estimate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cptravelestimates/routedetails)*