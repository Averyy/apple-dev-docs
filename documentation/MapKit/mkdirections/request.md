# MKDirections.Request

**Framework**: Mapkit  
**Kind**: class

The start and end points of a route, along with the planned mode of transportation.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.2+
- visionOS 1.0+

## Declaration

```swift
class Request
```

#### Overview

You use an [`MKDirections.Request`](mkdirections/request.md) object when requesting or providing directions. If your app provides directions, use this class to decode the URL that the Maps app sends to you. If you need to request directions from Apple, pass an instance of this class to an [`MKDirections`](mkdirections.md) object. For example, an app that provides subway directions might request walking directions to and from relevant subway stations.

Prior to iOS 14, for apps that provide directions, you receive direction-related URLs in your app delegate’s [`application(_:open:options:)`](https://developer.apple.com/documentation/UIKit/UIApplicationDelegate/application(_:open:options:))method. Upon receiving a URL, call the [`isDirectionsRequest(_:)`](mkdirections/request/isdirectionsrequest(_:).md) method of this class to determine whether the URL relates to routing directions. If it does, create an instance of this class using the provided URL and extract the map items associated with the start and end points.

> **Note**:  Prior to iOS 14, to provide routing directions, your app needs to include special keys in its `Info.plist` file and be able to handle URLs that the Maps app sends to it. These keys indicate a special URL type that you app needs to handle. For information about how to implement this support, see [`Location and Maps Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/LocationAwarenessPG/Introduction/Introduction.html#//apple_ref/doc/uid/TP40009497).

## Topics

### Creating a directions request object
- [class func isDirectionsRequest(URL) -> Bool](mkdirections/request/isdirectionsrequest(_:).md)
  Returns a Boolean value that indicates whether the specified URL contains a directions request.
- [init(contentsOfURL: URL)](mkdirections/request/init(contentsofurl:).md)
  Creates and returns a directions request object using the specified URL.
### Accessing the start and end points
- [var source: MKMapItem?](mkdirections/request/source.md)
  The starting point for routing directions.
- [var destination: MKMapItem?](mkdirections/request/destination.md)
  The end point for routing directions.
### Specifying transportation options
- [var transportType: MKDirectionsTransportType](mkdirections/request/transporttype.md)
  The type of conveyance that the directions apply to.
- [var highwayPreference: MKDirections.RoutePreference](mkdirections/request/highwaypreference.md)
  The value that indicates whether the framework uses or avoids highways when providing directions.
- [var tollPreference: MKDirections.RoutePreference](mkdirections/request/tollpreference.md)
  The value that indicates whether the framework avoids routes that have tolls when providing directions.
- [MKDirections.RoutePreference](mkdirections/routepreference.md)
  Options that modify how the framework selects routes when calculating directions.
- [var requestsAlternateRoutes: Bool](mkdirections/request/requestsalternateroutes.md)
  A Boolean value that indicates whether your app requests multiple routes when they’re available.
- [var departureDate: Date?](mkdirections/request/departuredate.md)
  The departure date for the trip.
- [var arrivalDate: Date?](mkdirections/request/arrivaldate.md)
  The arrival date for the trip.
### Constants
- [struct MKDirectionsTransportType](mkdirectionstransporttype.md)
  Constants that specify the type of conveyance to use.
### Launch options
- [let MKLaunchOptionsCameraKey: String](mklaunchoptionscamerakey.md)
  The virtual camera to use for viewing the map.
- [let MKLaunchOptionsDirectionsModeDefault: String](mklaunchoptionsdirectionsmodedefault.md)
  Directions that match the user’s preferred transportation type.
- [let MKLaunchOptionsDirectionsModeDriving: String](mklaunchoptionsdirectionsmodedriving.md)
  Driving directions between the specified start and end points.
- [let MKLaunchOptionsDirectionsModeKey: String](mklaunchoptionsdirectionsmodekey.md)
  The mode of transportation.
- [let MKLaunchOptionsDirectionsModeTransit: String](mklaunchoptionsdirectionsmodetransit.md)
  Public transit directions between the specified start and end points.
- [let MKLaunchOptionsDirectionsModeWalking: String](mklaunchoptionsdirectionsmodewalking.md)
  Walking directions between the specified start and end points.
- [let MKLaunchOptionsMapCenterKey: String](mklaunchoptionsmapcenterkey.md)
  The coordinate value on which to center the map.
- [let MKLaunchOptionsMapSpanKey: String](mklaunchoptionsmapspankey.md)
  The amount of the map to display.
- [let MKLaunchOptionsMapTypeKey: String](mklaunchoptionsmaptypekey.md)
  The type of map (standard, satellite, or hybrid) to display.
- [let MKLaunchOptionsShowsTrafficKey: String](mklaunchoptionsshowstraffickey.md)
  A Boolean value that indicates whether to display traffic information.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class MKDirections](mkdirections.md)
  A utility object that computes directions and travel-time information based on the route information you provide.
- [MKDirections.Response](mkdirections/response.md)
  The route information that Apple servers return in response to your request for directions.
- [MKDirections.ETAResponse](mkdirections/etaresponse.md)
  The travel-time information that Apple servers return.
- [class MKRoute](mkroute.md)
  A single route between a requested start and end point.
- [MKRoute.Step](mkroute/step.md)
  One portion of an overall route.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkdirections/request)*