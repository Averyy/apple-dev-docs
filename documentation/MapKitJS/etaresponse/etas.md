# etas

**Framework**: MapKit JS  
**Kind**: property

An array of estimated arrival times.

**Availability**:
- MapKit JS 5.46+

## Declaration

```swift
etas: EtaResult[];
```

#### Discussion

The server returns [`etas`](etaresponse/etas.md) as a part of the [`EtaResponse`](etaresponse.md) after your app creates an instance of the [`Directions`](directions.md) object and calls the [`eta(request, callback)`](directions/eta.md) method.

## See Also

- [request](etaresponse/request.md)
  The request object associated with the estimated time of arrival response.
- [origin](etaresponse/origin.md)
  The coordinates that represent the starting point for estimated arrival time requests.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/etaresponse/etas)*