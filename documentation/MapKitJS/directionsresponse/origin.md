# origin

**Framework**: MapKit JS  
**Kind**: property  
**Role**: Interface Property

An optional starting point for routing directions.

**Availability**:
- MapKit JS 5.55+

## Declaration

```
origin?: Coordinate | Place;
```

#### Discussion

If you use [`Coordinate`](../coordinate.md) to request directions with [`route()`](../directions/route.md), MapKit JS returns a `mapkit.Coordinate` in the direction’s response. If you use a string or a [`Place`](../place.md) to request directions, the property may be `null` or a `Place` instance.

When MapKit JS returns a `Place` instance, it may contain additional details that weren’t included in the original item used to request directions.

## See Also

### Directions response
- [routes](./routes.md)
  An array of route objects.
- [destination](./destination.md)
  An optional end point for routing directions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/directionsresponse/origin)*