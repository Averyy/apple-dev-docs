# MKDirections.RoutePreference

**Framework**: MapKit  
**Kind**: enum  
**Role**: Enumeration

Options that modify how the framework selects routes when calculating directions.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
enum RoutePreference
```

```c
enum MKDirectionsRoutePreference : NSInteger;
```

## Topics

### Route selection options
- [MKDirections.RoutePreference.any](./routepreference/any.md)
  The option that specifies any available route.
- [MKDirections.RoutePreference.avoid](./routepreference/avoid.md)
  The option that requests the framework avoid certain routes.
### Initializers
- [init?(rawValue: Int)](./routepreference/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Creating a directions object
- [init(request: MKDirections.Request)](./init%28request%29.md)
  Creates and returns a directions object using the specified request.
- [MKDirections.Request](./request.md)
  The start and end points of a route, along with the planned mode of transportation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkdirections/routepreference)*