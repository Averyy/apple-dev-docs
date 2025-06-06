# CPTrip

**Framework**: CarPlay  
**Kind**: class

An object that represents a journey between an origin and a destination.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
class CPTrip
```

#### Overview

A trip represents a journey consisting of an origin, a destination, and up to three route choices. Use [`CPRouteChoice`](cproutechoice.md) to define each possible route choice.

You create trips after the user has selected a destination, and present up to twelve trip previews by calling [`showTripPreviews(_:textConfiguration:)`](cpmaptemplate/showtrippreviews(_:textconfiguration:).md) on the map template.

You provide estimates for each trip using the map template’s [`updateEstimates(_:for:)`](cpmaptemplate/updateestimates(_:for:).md) method, and must update these estimates if the remaining time or distance changes.

## Topics

### Creating a Trip
- [init(origin: MKMapItem, destination: MKMapItem, routeChoices: [CPRouteChoice])](cptrip/init(origin:destination:routechoices:).md)
  Creates a trip with an origin, destination, and route choices.
- [class CPRouteChoice](cproutechoice.md)
  A possible route for a trip.
### Getting the Trip’s Origin and Destination
- [var origin: MKMapItem](cptrip/origin.md)
  The trip’s origin.
- [var destination: MKMapItem](cptrip/destination.md)
  The trip’s destination.
### Getting Route Choices
- [var routeChoices: [CPRouteChoice]](cptrip/routechoices.md)
  The list of route choices for the trip.
- [var destinationNameVariants: [String]?](cptrip/destinationnamevariants.md)
  An array of strings that represents the names of the destination for this trip, arranged from most to least preferred.
### Providing Additional Information
- [var userInfo: Any?](cptrip/userinfo.md)
  A custom object associated with the trip.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

## See Also

- [var trip: CPTrip](cpnavigationsession/trip.md)
  The trip associated with the navigation session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cptrip)*