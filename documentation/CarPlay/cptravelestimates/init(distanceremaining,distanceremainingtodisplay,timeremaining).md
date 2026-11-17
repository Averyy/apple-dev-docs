# init(distanceRemaining:distanceRemainingToDisplay:timeRemaining:)

**Framework**: CarPlay  
**Kind**: init  
**Role**: Initializer

Creates a travel estimates instance with the distance remaining that the framework displays to a person.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+

## Declaration

```swift
init(distanceRemaining: Measurement<UnitLength>, distanceRemainingToDisplay: Measurement<UnitLength>, timeRemaining time: TimeInterval)
```

```objc
- (instancetype) initWithDistanceRemaining:(NSMeasurement<NSUnitLength *> *) distanceRemaining distanceRemainingToDisplay:(NSMeasurement<NSUnitLength *> *) distanceRemainingToDisplay timeRemaining:(NSTimeInterval) time;
```

## Return Value

A newly initialized travel estimates object.

## Discussion

If not set, falls back to `distanceRemaining`.

## Parameters

- `distanceRemaining`: The distance remaining in [`Measurement`](../../Foundation/measurement.md) units.
- `distanceRemainingToDisplay`: The disance remaining to dfisk to a person, in `Measurement` units.
- `time`: `TimeInterval`

## See Also

### Creating travel estimates
- [init(distanceRemaining: Measurement<UnitLength>, timeRemaining: TimeInterval)](./init%28distanceremaining,timeremaining%29.md)
  Creates travel estimates with the remaining distance and time.
- [init(distanceRemaining: Measurement<UnitLength>, distanceRemainingToDisplay: Measurement<UnitLength>, timeRemaining: TimeInterval, routeDetails: [CPRouteDetail])](./init%28distanceremaining,distanceremainingtodisplay,timeremaining,routedetails%29.md)
  Initialize a @c CPTravelEstimates with distance, distance to display, time remaining, and additional trip information.
- [init?(coder: NSCoder)](./init%28coder%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cptravelestimates/init(distanceremaining:distanceremainingtodisplay:timeremaining:))*