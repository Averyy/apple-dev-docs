# etas

**Framework**: MapKit JS  
**Kind**: property  
**Role**: Interface Property

An array of estimated arrival times.

**Availability**:
- MapKit JS 5.46+

## Declaration

```
etas: EtaResult[];
```

#### Discussion

The server returns [`etas`](./etas.md) as a part of the [`EtaResponse`](../etaresponse.md) after your app creates an instance of the [`Directions`](../directions.md) object and calls the [`eta()`](../directions/eta.md) method.

## See Also

### Estimated Arrival Time Responses
- [origin](./origin.md)
  The coordinates that represent the starting point for estimated arrival time requests.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/etaresponse/etas)*