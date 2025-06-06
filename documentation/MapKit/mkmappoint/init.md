# init(_:)

**Framework**: MapKit  
**Kind**: init

Creates the map point data structure that corresponds to the specified coordinate.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.2+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
init(_ coordinate: CLLocationCoordinate2D)
```

#### Return Value

The map point value that corresponds to the specified coordinate on a two-dimensional map projection.

## Parameters

- `coordinate`: The coordinate containing the latitude and longitude values for the desired point.

## See Also

- [init()](mkmappoint/init.md)
  Creates a map point at an unspecified point.
- [init(x: Double, y: Double)](mkmappoint/init(x:y:).md)
  Creates a new map point structure from the specified values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmappoint/init(_:))*