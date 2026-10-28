# CPTrip

**Framework**: CarPlay  
**Kind**: class  
**Role**: Class

An object that represents a journey between an origin and a destination.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
class CPTrip
```

```objc
@interface CPTrip : NSObject
```

## Overview

A trip represents a journey consisting of an origin, a destination, and up to three route choices. Use [`CPRouteChoice`](./cproutechoice.md) to define each possible route choice.

You create trips after the user has selected a destination, and present up to twelve trip previews by calling [`showTripPreviews(_:textConfiguration:)`](./cpmaptemplate/showtrippreviews%28_,textconfiguration%29.md) on the map template.

You provide estimates for each trip using the map template’s [`updateEstimates(_:for:)`](./cpmaptemplate/updateestimates%28_,for%29.md) method, and must update these estimates if the remaining time or distance changes.

## Topics

### Creating a Trip
- [convenience init(origin: MKMapItem, destination: MKMapItem, routeChoices: [CPRouteChoice])](./cptrip/init%28origin,destination,routechoices%29.md)
  Creates a trip with an origin, destination, and route choices.
- [class CPRouteChoice](./cproutechoice.md)
  A possible route for a trip.
### Getting the Trip’s Origin and Destination
- [var origin: MKMapItem](./cptrip/origin.md)
  The trip’s origin.
- [var destination: MKMapItem](./cptrip/destination.md)
  The trip’s destination.
### Getting Route Choices
- [var routeChoices: [CPRouteChoice]](./cptrip/routechoices.md)
  The list of route choices for the trip.
- [var destinationNameVariants: [String]?](./cptrip/destinationnamevariants.md)
  An array of strings that represents the names of the destination for this trip, arranged from most to least preferred.
### Providing Additional Information
- [var userInfo: Any?](./cptrip/userinfo.md)
  A custom object associated with the trip.
### Initializers
- [init?(coder: NSCoder)](./cptrip/init%28coder%29.md)
- [init(originWaypoint: CPNavigationWaypoint, destinationWaypoint: CPNavigationWaypoint, routeChoices: [CPRouteChoice])](./cptrip/init%28originwaypoint,destinationwaypoint,routechoices%29.md)
  Initialize a @c CPTrip with an origin waypoint, destination waypoint, and route choices.
### Instance Properties
- [var destinationWaypoint: CPNavigationWaypoint](./cptrip/destinationwaypoint.md)
- [var hasShareableDestination: Bool](./cptrip/hasshareabledestination.md)
  Set to @YES to enable sharing of the destination of this trip.
- [var originWaypoint: CPNavigationWaypoint](./cptrip/originwaypoint.md)
- [var routeSegmentsAvailableForRegion: Bool](./cptrip/routesegmentsavailableforregion.md)
  Set to @NO to disable route sharing for this trip when route sharing is not supported in the current region.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### Getting the Trip
- [var trip: CPTrip](./cpnavigationsession/trip.md)
  The trip associated with the navigation session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cptrip)*