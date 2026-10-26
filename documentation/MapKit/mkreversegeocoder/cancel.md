# cancel

**Framework**: MapKit  
**Kind**: method  
**Role**: Instance Method

Cancels a pending reverse-geocoding request.

**Availability**:
- iOS 3.0+ - Deprecated in 5.0
- iPadOS 3.0+ - Deprecated in 5.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: Use the [`CLGeocoder`](../../CoreLocation/clgeocoder.md) class instead.

## Declaration

```objc
- (void) cancel;
```

#### Discussion

You can use this method to cancel a pending request and free up the resources associated with that request. If the request has already returned or has not yet begun, calling this method has no effect.

## See Also

### Managing the Search
- [- start](./start.md)
  Starts the reverse-geocoding process asynchronously.
- [querying](./querying.md)
  A Boolean value indicating whether the receiver is in the middle of reverse-geocoding its coordinate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkreversegeocoder/cancel)*