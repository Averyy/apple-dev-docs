# departureDate

**Framework**: MapKit JS  
**Kind**: property  
**Role**: Interface Property

The time of departure used in an estimated arrival time request.

**Availability**:
- MapKit JS 5.46+

## Declaration

```
departureDate?: Date;
```

#### Discussion

If you don’t specify a departure date, the server will use the current date and time when you make the request.

## See Also

### ETA Request
- [origin](./origin.md)
  The starting point for estimated arrival time requests.
- [destinations](./destinations.md)
  An array of coordinates that represent end points for estimated arrival time requests.
- [transportType](./transporttype.md)
  The mode of transportation the server uses when estimating arrival times.
- [signal](./signal.md)
  A signal object allowing you to cancel the request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/etarequestoptions/departuredate)*