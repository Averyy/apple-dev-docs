# reverseGeocoder:didFindPlacemark:

**Framework**: MapKit  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that a reverse geocoder successfully obtained placemark information for its coordinate.

**Availability**:
- iOS 3.0+ - Deprecated in 5.0
- iPadOS 3.0+ - Deprecated in 5.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: Use the [`CLGeocoder`](../../CoreLocation/clgeocoder.md) class instead.

## Declaration

```objc
- (void) reverseGeocoder:(MKReverseGeocoder *) geocoder didFindPlacemark:(MKPlacemark *) placemark;
```

## Discussion

You can get the map coordinate for the associated request from either the reverse geocoder object or from the placemark object, which itself supports the [`MKAnnotation`](../mkannotation.md) protocol.

## Parameters

- `geocoder`: The reverse geocoder object that completed its request successfully.
- `placemark`: The object containing the placemark data.

## See Also

### Related Documentation
- [Location and Maps Programming Guide](https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/LocationAwarenessPG/Introduction/Introduction.html#//apple_ref/doc/uid/TP40009497)
### Processing placemark searches
- [- reverseGeocoder:didFailWithError:](./reversegeocoder_didfailwitherror_.md)
  Tells the delegate that the specified reverse geocoder failed to obtain information about its coordinate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkreversegeocoderdelegate/reversegeocoder:didfindplacemark:)*