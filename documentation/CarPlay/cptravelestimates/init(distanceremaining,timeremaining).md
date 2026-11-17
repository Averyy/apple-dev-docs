# init(distanceRemaining:timeRemaining:)

**Framework**: CarPlay  
**Kind**: init  
**Role**: Initializer

Creates travel estimates with the remaining distance and time.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
init(distanceRemaining distance: Measurement<UnitLength>, timeRemaining time: TimeInterval)
```

```objc
- (instancetype) initWithDistanceRemaining:(NSMeasurement<NSUnitLength *> *) distance timeRemaining:(NSTimeInterval) time;
```

## Return Value

A newly initialized travel estimates object.

## Parameters

- `distance`: The remaining distance for the travel estimate.
- `time`: The remaining time for the travel estimate.

## See Also

### Creating travel estimates
- [init(distanceRemaining: Measurement<UnitLength>, distanceRemainingToDisplay: Measurement<UnitLength>, timeRemaining: TimeInterval)](./init%28distanceremaining,distanceremainingtodisplay,timeremaining%29.md)
  Creates a travel estimates instance with the distance remaining that the framework displays to a person.
- [init(distanceRemaining: Measurement<UnitLength>, distanceRemainingToDisplay: Measurement<UnitLength>, timeRemaining: TimeInterval, routeDetails: [CPRouteDetail])](./init%28distanceremaining,distanceremainingtodisplay,timeremaining,routedetails%29.md)
  Initialize a @c CPTravelEstimates with distance, distance to display, time remaining, and additional trip information.
- [init?(coder: NSCoder)](./init%28coder%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cptravelestimates/init(distanceremaining:timeremaining:))*