# init(center:radius:)

**Framework**: MapKit  
**Kind**: init  
**Role**: Initializer

Creates and returns a circle object using the specified coordinate and radius.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.2+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
convenience init(center coord: CLLocationCoordinate2D, radius: CLLocationDistance)
```

```objc
+ (instancetype) circleWithCenterCoordinate:(CLLocationCoordinate2D) coord radius:(CLLocationDistance) radius;
```

## Return Value

A circle overlay object.

## Parameters

- `coord`: The center point of the circle, specified as a latitude and longitude value.
- `radius`: The radius of the circle, measured in meters from the center point.

## See Also

### Related Documentation
- [Location and Maps Programming Guide](https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/LocationAwarenessPG/Introduction/Introduction.html#//apple_ref/doc/uid/TP40009497)
### Creating a circle overlay
- [convenience init(mapRect: MKMapRect)](./init%28maprect%29.md)
  Creates and returns a circle object that derives the circular area from the specified rectangle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkcircle/init(center:radius:))*