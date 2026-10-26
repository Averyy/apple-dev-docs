# reverseGeocoder:didFailWithError:

**Framework**: MapKit  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that the specified reverse geocoder failed to obtain information about its coordinate.

**Availability**:
- iOS 3.0+ - Deprecated in 5.0
- iPadOS 3.0+ - Deprecated in 5.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: Use the [`CLGeocoder`](../../CoreLocation/clgeocoder.md) class instead.

## Declaration

```objc
- (void) reverseGeocoder:(MKReverseGeocoder *) geocoder didFailWithError:(NSError *) error;
```

## Parameters

- `geocoder`: The reverse geocoder object that was unable to complete its request.
- `error`: An error object indicating the reason the request did not succeed.

## See Also

### Processing placemark searches
- [- reverseGeocoder:didFindPlacemark:](./reversegeocoder_didfindplacemark_.md)
  Tells the delegate that a reverse geocoder successfully obtained placemark information for its coordinate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkreversegeocoderdelegate/reversegeocoder:didfailwitherror:)*