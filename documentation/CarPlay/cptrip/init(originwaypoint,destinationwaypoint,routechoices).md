# init(originWaypoint:destinationWaypoint:routeChoices:)

**Framework**: CarPlay  
**Kind**: init  
**Role**: Initializer

Initialize a @c CPTrip with an origin waypoint, destination waypoint, and route choices.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst 26.4+

## Declaration

```swift
init(originWaypoint origin: CPNavigationWaypoint, destinationWaypoint destination: CPNavigationWaypoint, routeChoices: [CPRouteChoice])
```

```objc
- (instancetype) initWithOriginWaypoint:(CPNavigationWaypoint *) origin destinationWaypoint:(CPNavigationWaypoint *) destination routeChoices:(NSArray<CPRouteChoice *> *) routeChoices;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cptrip/init(originwaypoint:destinationwaypoint:routechoices:))*