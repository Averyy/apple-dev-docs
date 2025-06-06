# init(origin:destination:routeChoices:)

**Framework**: CarPlay  
**Kind**: init

Creates a trip with an origin, destination, and route choices.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
init(origin: MKMapItem, destination: MKMapItem, routeChoices: [CPRouteChoice])
```

#### Return Value

A newly initialized trip.

## Parameters

- `origin`: The trip’s origin.
- `destination`: The trip’s destination.
- `routeChoices`: Up to three route choices available for the trip.

## See Also

- [class CPRouteChoice](cproutechoice.md)
  A possible route for a trip.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cptrip/init(origin:destination:routechoices:))*