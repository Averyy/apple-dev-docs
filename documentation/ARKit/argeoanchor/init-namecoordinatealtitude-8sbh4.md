# init(name:coordinate:altitude:)

**Framework**: ARKit  
**Kind**: init

Initializes a named location anchor with the given coordinates and altitude.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
init(name: String, coordinate: CLLocationCoordinate2D, altitude: CLLocationDistance)
```

## Parameters

- `name`: Name of the anchor.
- `coordinate`: Lattitude and longitude of the anchor’s geographic location.
- `altitude`: Vertical distance, in meters, between this anchor and sea level.

## See Also

- [convenience init(coordinate: CLLocationCoordinate2D, altitude: CLLocationDistance?)](argeoanchor/init(coordinate:altitude:).md)
  Initializes a location anchor with the given coordinate and altitude.
- [convenience init(name: String, coordinate: CLLocationCoordinate2D, altitude: CLLocationDistance?)](argeoanchor/init(name:coordinate:altitude:)-csze.md)
  Initializes a named location anchor with the given coordinates and altitude.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/argeoanchor/init(name:coordinate:altitude:)-8sbh4)*