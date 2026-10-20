# init(coordinate:altitude:)

**Framework**: ARKit  
**Kind**: init  
**Role**: Initializer

Initializes a location anchor with the given coordinate and altitude.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+

## Declaration

```swift
@nonobjc
convenience init(coordinate: CLLocationCoordinate2D, altitude: CLLocationDistance? = nil)
```

## Parameters

- `coordinate`: Lattitude and longitude of the anchor’s geographic location.
- `altitude`: Vertical distance, in meters, between this anchor and sea level.

## See Also

### Creating a Geo Anchor
- [init(name: String, coordinate: CLLocationCoordinate2D, altitude: CLLocationDistance)](./init%28name,coordinate,altitude%29-8sbh4.md)
  Initializes a named location anchor with the given coordinates and altitude.
- [convenience init(name: String, coordinate: CLLocationCoordinate2D, altitude: CLLocationDistance?)](./init%28name,coordinate,altitude%29-csze.md)
  Initializes a named location anchor with the given coordinates and altitude.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/argeoanchor/init(coordinate:altitude:))*