# MKDirections.RoutePreference

**Framework**: MapKit  
**Kind**: enum

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

## Topics

### Route selection options
- [MKDirections.RoutePreference.any](mkdirections/routepreference/any.md)
  The option that specifies any available route.
- [MKDirections.RoutePreference.avoid](mkdirections/routepreference/avoid.md)
  The option that requests the framework avoid certain routes.
### Initializers
- [init?(rawValue: Int)](mkdirections/routepreference/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../swift/bitwisecopyable.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [init(request: MKDirections.Request)](mkdirections/init(request:).md)
  Creates and returns a directions object using the specified request.
- [MKDirections.Request](mkdirections/request.md)
  The start and end points of a route, along with the planned mode of transportation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkdirections/routepreference)*