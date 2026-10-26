# initWithCoordinate:altitude:

**Framework**: ARKit  
**Kind**: method  
**Role**: Instance Method

Initializes a location anchor with the given coordinate and altitude.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+

## Declaration

```objc
- (instancetype) initWithCoordinate:(CLLocationCoordinate2D) coordinate altitude:(CLLocationDistance) altitude;
```

## Parameters

- `coordinate`: Lattitude and longitude of the anchor’s geographic location.
- `altitude`: Vertical distance, in meters, between this anchor and sea level.

## See Also

### Creating a Geo Anchor
- [- initWithCoordinate:](./initwithcoordinate_.md)
  Initializes a new location anchor with the given coordinates.
- [- initWithName:coordinate:](./initwithname_coordinate_.md)
  Initializes a named location anchor with the given coordinates.
- [init(name: String, coordinate: CLLocationCoordinate2D, altitude: CLLocationDistance)](./init%28name,coordinate,altitude%29-8sbh4.md)
  Initializes a named location anchor with the given coordinates and altitude.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/argeoanchor/initwithcoordinate:altitude:)*