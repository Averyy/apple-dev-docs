# initWithCoordinate:

**Framework**: MapKit  
**Kind**: method  
**Role**: Instance Method

Initializes the reverse geocoder with the specified coordinate value.

**Availability**:
- iOS 3.0+ - Deprecated in 5.0
- iPadOS 3.0+ - Deprecated in 5.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: Use the [`CLGeocoder`](../../CoreLocation/clgeocoder.md) class instead.

## Declaration

```objc
- (instancetype) initWithCoordinate:(CLLocationCoordinate2D) coordinate;
```

## Return Value

An initialized `MKReverseGeocoder` object.

## Parameters

- `coordinate`: The map coordinate whose placemark information you want to retrieve.

## See Also

### Related Documentation
- [Location and Maps Programming Guide](https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/LocationAwarenessPG/Introduction/Introduction.html#//apple_ref/doc/uid/TP40009497)


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkreversegeocoder/initwithcoordinate:)*