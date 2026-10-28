# querying

**Framework**: MapKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value indicating whether the receiver is in the middle of reverse-geocoding its coordinate.

**Availability**:
- iOS 3.0+ - Deprecated in 5.0
- iPadOS 3.0+ - Deprecated in 5.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: Use the [`CLGeocoder`](../../CoreLocation/clgeocoder.md) class instead.

## Declaration

```objc
@property (nonatomic, readonly, getter=isQuerying) BOOL querying;
```

## Discussion

This property contains YES if the process is ongoing or NO if the process is done or has not yet been initiated.

## See Also

### Managing the Search
- [- start](./start.md)
  Starts the reverse-geocoding process asynchronously.
- [- cancel](./cancel.md)
  Cancels a pending reverse-geocoding request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkreversegeocoder/querying)*