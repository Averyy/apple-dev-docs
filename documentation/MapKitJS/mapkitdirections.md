# mapkit.Directions

**Framework**: MapKit JS  
**Kind**: class

An object that provides directions and estimated travel time based on the options you provide.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
interface mapkit.Directions
```

## Mentions

- [MapKit JS 5](mapkit-js-5.md)

## Topics

### Creating a directions object
- [mapkit.Directions](mapkit.directions/mapkit.directions.md)
  Creates a directions object with options you provide.
- [DirectionsConstructorOptions](directionsconstructoroptions.md)
  Options that you may provide when creating a directions object.
### Getting estimated arrival times
- [eta](mapkit.directions/eta.md)
  Retrieves estimated arrival times to up to 10 destinations from a single starting point.
- [EtaRequestOptions](etarequestoptions.md)
  The options you may provide for requesting estimated arrival times.
- [EtaResponse](etaresponse.md)
  The estimated arrival times for a set of destinations.
- [EtaResult](etaresult.md)
  The mode of transportation, distance, and travel time estimates for a single destination.
### Getting directions
- [route](mapkit.directions/route.md)
  Retrieves directions and estimated travel time based on the specified start and end points.
- [DirectionsRequest](directionsrequest.md)
  The requested start and end points for a route, as well as the planned mode of transportation.
- [DirectionsResponse](directionsresponse.md)
  The directions and estimated travel time that return for a route.
- [Route](route.md)
  Information about a route, including step-by-step instructions, distance, and estimated travel time.
- [RouteStep](routestep.md)
  A single step of the route between the requested start and end points.
### Canceling a directions request
- [cancel](mapkit.directions/cancel.md)
  Cancels a previous request for routes or estimated arrival times.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/mapkit.directions)*