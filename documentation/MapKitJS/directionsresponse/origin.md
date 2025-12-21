# origin

**Framework**: MapKit JS  
**Kind**: property

An optional starting point for routing directions.

**Availability**:
- MapKit JS 5.55+

## Declaration

```swift
origin?: Coordinate | Place;
```

#### Discussion

If you use [`Coordinate`](coordinate.md) to request directions with [`route(request, callback)`](directions/route.md), MapKit JS returns a `mapkit.Coordinate` in the direction’s response. If you use a string or a [`Place`](place.md) to request directions, the property may be `null` or a `Place` instance.

When MapKit JS returns a `Place` instance, it may contain additional details that weren’t included in the original item used to request directions.

## See Also

- [request](directionsresponse/request.md)
  The request object associated with the direction’s response.
- [routes](directionsresponse/routes.md)
  An array of route objects.
- [destination](directionsresponse/destination.md)
  An optional end point for routing directions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/directionsresponse/origin)*