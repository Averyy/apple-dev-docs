# delegate

**Framework**: MapKit  
**Kind**: property  
**Role**: Instance Property

The reverse geocoder’s delegate object.

**Availability**:
- iOS 3.0+ - Deprecated in 5.0
- iPadOS 3.0+ - Deprecated in 5.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: Use the [`CLGeocoder`](../../CoreLocation/clgeocoder.md) class instead.

## Declaration

```objc
@property (nonatomic, weak) id<MKReverseGeocoderDelegate> delegate;
```

## Discussion

A reverse-geocoder object sends messages to its delegate regarding the successful (or unsuccessful) acquisition of placemark data. You must provide a delegate object to receive this data.

For more information about the [`MKReverseGeocoderDelegate`](../mkreversegeocoderdelegate.md) protocol, see [`MKReverseGeocoderDelegate`](../mkreversegeocoderdelegate.md).

## See Also

### Accessing Reverse Geocoder Attributes
- [coordinate](./coordinate.md)
  The coordinate whose placemark data you want to retrieve.
- [placemark](./placemark.md)
  The result of the reverse-geocoding operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkreversegeocoder/delegate)*