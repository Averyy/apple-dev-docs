# region

**Framework**: Core Location  
**Kind**: property  
**Role**: Instance Property

The geographic region associated with the placemark.

**Availability**:
- iOS 5.0+ - Deprecated in 27.2
- iPadOS 5.0+ - Deprecated in 27.2
- Mac Catalyst 13.1+ - Deprecated in 27.0
- macOS 10.8+ - Deprecated in 27.2
- tvOS 9.0+ - Deprecated in 27.0
- watchOS 2.0+ - Deprecated in 27.2

> **Deprecated**: Use either GeoToolbox.PlaceDescriptor or MapKit

## Declaration

```swift
@NSCopying
var region: CLRegion? { get }
```

```objc
@property (nonatomic, copy, readonly, nullable) CLRegion * region;
```

## See Also

### Getting the placemark’s location
- [var location: CLLocation?](./location.md)
  The location object containing latitude and longitude information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/clplacemark/region)*