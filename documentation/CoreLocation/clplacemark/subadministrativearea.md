# subAdministrativeArea

**Framework**: Core Location  
**Kind**: property  
**Role**: Instance Property

Additional administrative area information for the placemark.

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
var subAdministrativeArea: String? { get }
```

```objc
@property (nonatomic, copy, readonly, nullable) NSString * subAdministrativeArea;
```

## Discussion

Subadministrative areas typically correspond to counties or other regions that are then organized into a larger administrative area or state. For example, if the placemark location is Apple’s headquarters, the value for this property would be the string “Santa Clara”, which is the county in California that contains the city of Cupertino.

## See Also

### Getting the placemark details
- [var thoroughfare: String?](./thoroughfare.md)
  The street address associated with the placemark.
- [var subThoroughfare: String?](./subthoroughfare.md)
  Additional street-level information for the placemark.
- [var locality: String?](./locality.md)
  The city associated with the placemark.
- [var subLocality: String?](./sublocality.md)
  Additional city-level information for the placemark.
- [var administrativeArea: String?](./administrativearea.md)
  The state or province associated with the placemark.
- [var postalCode: String?](./postalcode.md)
  The postal code associated with the placemark.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/clplacemark/subadministrativearea)*