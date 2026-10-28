# placemark

**Framework**: MapKit  
**Kind**: property  
**Role**: Instance Property

The result of the reverse-geocoding operation.

**Availability**:
- iOS 3.2+ - Deprecated in 5.0
- iPadOS 3.2+ - Deprecated in 5.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: Use the [`CLGeocoder`](../../CoreLocation/clgeocoder.md) class instead. Note that placemarks in [`CLGeocoder`](../../CoreLocation/clgeocoder.md) always come back to the coordinate of the place, not the requested coordinate.

## Declaration

```objc
@property (nonatomic, readonly) MKPlacemark * placemark;
```

## Discussion

The value of this property is `nil` by default. After a successful reverse-geocoding operation, it is set to the placemark object that was generated.

## See Also

### Accessing Reverse Geocoder Attributes
- [delegate](./delegate.md)
  The reverse geocoder’s delegate object.
- [coordinate](./coordinate.md)
  The coordinate whose placemark data you want to retrieve.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkreversegeocoder/placemark)*