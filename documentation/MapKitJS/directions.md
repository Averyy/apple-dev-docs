# Directions

**Framework**: MapKit JS  
**Kind**: class

An object that provides directions and estimated travel time based on the options you provide.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
class Directions extends Service
```

## Mentions

- [MapKit JS 5](mapkit-js-5.md)

## Topics

### Creating a directions object
- [new Directions(options)](directions/directionsconstructor.md)
  Creates a directions object with options you provide.
- [interface DirectionsConstructorOptions](directionsconstructoroptions.md)
  Options that you may provide when creating a directions object.
### Getting estimated arrival times
- [eta(request, callback)](directions/eta.md)
  Retrieves estimated arrival times to up to 10 destinations from a single starting point.
- [interface EtaRequestOptions](etarequestoptions.md)
  The options you may provide for requesting estimated arrival times.
- [interface EtaResponse](etaresponse.md)
  The estimated arrival times for a set of destinations.
- [interface EtaResult](etaresult.md)
  The mode of transportation, distance, and travel time estimates for a single destination.
### Getting directions
- [route(request, callback)](directions/route.md)
  Retrieves directions and estimated travel time based on the specified start and end points.
- [interface DirectionsRequest](directionsrequest.md)
  The requested start and end points for a route, as well as the planned mode of transportation.
- [interface DirectionsResponse](directionsresponse.md)
  The directions and estimated travel time that return for a route.
- [class Route](route.md)
  Information about a route, including step-by-step instructions, distance, and estimated travel time.
- [class RouteStep](routestep.md)
  A single step of the route between the requested start and end points.
### Canceling a directions request
- [cancel(id)](service/cancel.md)
  Cancels a request using the provided request ID.
### Static properties
- [Transport](directions/transport.md)
  A static property that refers to an object that describes the available transport type values.

## Relationships

### Inherits From
- [Service](service.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/directions)*