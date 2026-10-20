# init(request:)

**Framework**: MapKit  
**Kind**: init  
**Role**: Initializer

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

```objc
- (instancetype) initWithRequest:(MKDirectionsRequest *) request;
```

#### Return Value

An initialized directions object.

#### Discussion

After initializing your directions object, you must call the [`calculate(completionHandler:)`](./calculate%28completionhandler%29.md) or [`calculateETA(completionHandler:)`](./calculateeta%28completionhandler%29.md) method to perform the request.

## Parameters

- `request`: The request object containing the start and end points of the route. This parameter must not be `nil`.

## See Also

### Related Documentation
- [Location and Maps Programming Guide](https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/LocationAwarenessPG/Introduction/Introduction.html#//apple_ref/doc/uid/TP40009497)
### Creating a directions object
- [MKDirections.Request](./request.md)
  The start and end points of a route, along with the planned mode of transportation.
- [MKDirections.RoutePreference](./routepreference.md)
  Options that modify how the framework selects routes when calculating directions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkdirections/init(request:))*