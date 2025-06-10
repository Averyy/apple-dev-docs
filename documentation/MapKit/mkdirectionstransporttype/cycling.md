# cycling

**Framework**: MapKit  
**Kind**: property

Directions suitable for use while cycling.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
static var cycling: MKDirectionsTransportType { get }
```

#### Discussion

Use this transportation type to request cycling directions between locations.

The following example shows a task that requests directions between two locations.

```swift
  // Bethesda Terrace in Central Park, New York, NY, United States
  let origin = MKMapItem(location: .init(latitude: 40.77396, longitude: -73.97097), address: nil)

  // Grand Central Terminal, New York, NY, United States
  let destination = MKMapItem(location: .init(latitude: 40.7528, longitude: -73.97715), address: nil)

  Task {
      let request = MKDirections.Request()
      request.transportType = .cycling
      request.source = origin
      request.destination = destination
      directions = try? await MKDirections(request: request).calculate()
  }
```

## See Also

- [static var any: MKDirectionsTransportType](mkdirectionstransporttype/any.md)
  Directions suitable for any transportation option.
- [static var automobile: MKDirectionsTransportType](mkdirectionstransporttype/automobile.md)
  Directions suitable for use while driving.
- [static var transit: MKDirectionsTransportType](mkdirectionstransporttype/transit.md)
  Directions suitable for public transportation.
- [static var walking: MKDirectionsTransportType](mkdirectionstransporttype/walking.md)
  Directions suitable for a pedestrian.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkdirectionstransporttype/cycling)*