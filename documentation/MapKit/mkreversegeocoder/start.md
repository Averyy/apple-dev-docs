# start

**Framework**: MapKit  
**Kind**: method  
**Role**: Instance Method

Starts the reverse-geocoding process asynchronously.

**Availability**:
- iOS 3.0+ - Deprecated in 5.0
- iPadOS 3.0+ - Deprecated in 5.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: Use the [`CLGeocoder`](../../CoreLocation/clgeocoder.md) class instead.

## Declaration

```objc
- (void) start;
```

#### Discussion

You should call this method only once to begin the reverse-geocoding process. This method submits the coordinate value to the map server asynchronously and returns. Once the process is complete, the results are delivered to the associated delegate object.

## See Also

### Managing the Search
- [querying](./querying.md)
  A Boolean value indicating whether the receiver is in the middle of reverse-geocoding its coordinate.
- [- cancel](./cancel.md)
  Cancels a pending reverse-geocoding request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkreversegeocoder/start)*