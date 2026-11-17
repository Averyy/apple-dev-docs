# init(distanceRemaining:distanceRemainingToDisplay:timeRemaining:routeDetails:)

**Framework**: CarPlay  
**Kind**: init  
**Role**: Initializer

Initialize a @c CPTravelEstimates with distance, distance to display, time remaining, and additional trip information.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```swift
init(distanceRemaining: Measurement<UnitLength>, distanceRemainingToDisplay: Measurement<UnitLength>, timeRemaining time: TimeInterval, routeDetails: [CPRouteDetail])
```

```objc
- (instancetype) initWithDistanceRemaining:(NSMeasurement<NSUnitLength *> *) distanceRemaining distanceRemainingToDisplay:(NSMeasurement<NSUnitLength *> *) distanceRemainingToDisplay timeRemaining:(NSTimeInterval) time routeDetails:(NSArray<CPRouteDetail *> *) routeDetails;
```

## See Also

### Creating travel estimates
- [init(distanceRemaining: Measurement<UnitLength>, timeRemaining: TimeInterval)](./init%28distanceremaining,timeremaining%29.md)
  Creates travel estimates with the remaining distance and time.
- [init(distanceRemaining: Measurement<UnitLength>, distanceRemainingToDisplay: Measurement<UnitLength>, timeRemaining: TimeInterval)](./init%28distanceremaining,distanceremainingtodisplay,timeremaining%29.md)
  Creates a travel estimates instance with the distance remaining that the framework displays to a person.
- [init?(coder: NSCoder)](./init%28coder%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cptravelestimates/init(distanceremaining:distanceremainingtodisplay:timeremaining:routedetails:))*