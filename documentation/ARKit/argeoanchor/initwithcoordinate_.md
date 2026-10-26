# initWithCoordinate:

**Framework**: ARKit  
**Kind**: method  
**Role**: Instance Method

Initializes a new location anchor with the given coordinates.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+

## Declaration

```objc
- (instancetype) initWithCoordinate:(CLLocationCoordinate2D) coordinate;
```

#### Discussion

Because this initializer does not take an altitude argument, ARKit sets the anchor’s [`altitude`](./altitude-9kges.md) to ground level.

## Parameters

- `coordinate`: Lattitude and longitude of the anchor’s geographic location.

## See Also

### Creating a Geo Anchor
- [- initWithCoordinate:altitude:](./initwithcoordinate_altitude_.md)
  Initializes a location anchor with the given coordinate and altitude.
- [- initWithName:coordinate:](./initwithname_coordinate_.md)
  Initializes a named location anchor with the given coordinates.
- [init(name: String, coordinate: CLLocationCoordinate2D, altitude: CLLocationDistance)](./init%28name,coordinate,altitude%29-8sbh4.md)
  Initializes a named location anchor with the given coordinates and altitude.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/argeoanchor/initwithcoordinate:)*