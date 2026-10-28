# location

**Framework**: Core Location  
**Kind**: property  
**Role**: Instance Property

The location object containing latitude and longitude information.

**Availability**:
- iOS 5.0+ - Deprecated in 27.2
- iPadOS 5.0+ - Deprecated in 27.2
- Mac Catalyst 13.1+ - Deprecated in 27.0
- macOS 10.8+ - Deprecated in 27.2
- tvOS 9.0+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.2
- watchOS 2.0+ - Deprecated in 27.2

> **Deprecated**: Use either GeoToolbox.PlaceDescriptor or MapKit

## Declaration

```swift
@NSCopying
var location: CLLocation? { get }
```

```objc
@property (nonatomic, copy, readonly, nullable) CLLocation * location;
```

## Discussion

Use this object to initialize the placemark object.

## See Also

### Getting the placemark’s location
- [var region: CLRegion?](./region.md)
  The geographic region associated with the placemark.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/clplacemark/location)*