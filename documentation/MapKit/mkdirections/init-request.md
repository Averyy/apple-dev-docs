# init(request:)

**Framework**: MapKit  
**Kind**: init

Creates and returns a directions object using the specified request.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.2+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
init(request: MKDirections.Request)
```

#### Return Value

An initialized directions object.

#### Discussion

After initializing your directions object, you must call the [`calculate(completionHandler:)`](mkdirections/calculate(completionhandler:).md) or [`calculateETA(completionHandler:)`](mkdirections/calculateeta(completionhandler:).md) method to perform the request.

## Parameters

- `request`: The request object containing the start and end points of the route. This parameter must not be  .

## See Also

- [Location and Maps Programming Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/LocationAwarenessPG/Introduction/Introduction.html#//apple_ref/doc/uid/TP40009497)
- [MKDirections.Request](mkdirections/request.md)
  The start and end points of a route, along with the planned mode of transportation.
- [MKDirections.RoutePreference](mkdirections/routepreference.md)
  Options that modify how the framework selects routes when calculating directions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkdirections/init(request:))*