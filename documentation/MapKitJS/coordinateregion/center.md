# center

**Framework**: MapKit JS  
**Kind**: property  
**Role**: Instance Property

The center point of the region.

**Availability**:
- MapKit JS 5.0+

## Declaration

```
get center(): Coordinate;
set center(coordinate: CoordinateData);
```

## Discussion

Create a [`Coordinate`](../coordinate.md) with a latitude and longitude pair:

```javascript
const center = new mapkit.Coordinate(37.415, -122.048333); // latitude, longitude
```

## See Also

### Defining the region
- [span](./span.md)
  The horizontal and vertical span representing the amount of map to display.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/coordinateregion/center)*