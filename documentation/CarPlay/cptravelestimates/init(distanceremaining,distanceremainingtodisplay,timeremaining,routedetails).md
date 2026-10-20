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


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cptravelestimates/init(distanceremaining:distanceremainingtodisplay:timeremaining:routedetails:))*