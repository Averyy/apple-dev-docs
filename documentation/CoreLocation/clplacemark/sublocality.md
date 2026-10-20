# subLocality

**Framework**: Core Location  
**Kind**: property  
**Role**: Instance Property

Additional city-level information for the placemark.

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
var subLocality: String? { get }
```

```objc
@property (nonatomic, copy, readonly, nullable) NSString * subLocality;
```

#### Discussion

This property contains additional information, such as the name of the neighborhood or landmark associated with the placemark. It might also refer to a common name that’s associated with the location.

## See Also

### Getting the placemark details
- [var thoroughfare: String?](./thoroughfare.md)
  The street address associated with the placemark.
- [var subThoroughfare: String?](./subthoroughfare.md)
  Additional street-level information for the placemark.
- [var locality: String?](./locality.md)
  The city associated with the placemark.
- [var administrativeArea: String?](./administrativearea.md)
  The state or province associated with the placemark.
- [var subAdministrativeArea: String?](./subadministrativearea.md)
  Additional administrative area information for the placemark.
- [var postalCode: String?](./postalcode.md)
  The postal code associated with the placemark.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/clplacemark/sublocality)*