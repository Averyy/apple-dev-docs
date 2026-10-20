# locality

**Framework**: Core Location  
**Kind**: property  
**Role**: Instance Property

The city associated with the placemark.

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
var locality: String? { get }
```

```objc
@property (nonatomic, copy, readonly, nullable) NSString * locality;
```

## Mentions

- [Converting a user’s location to a descriptive placemark](../converting-a-user-s-location-to-a-descriptive-placemark.md)

#### Discussion

If the placemark location is Apple’s headquarters, for example, the value for this property would be the string “Cupertino”.

## See Also

### Getting the placemark details
- [var thoroughfare: String?](./thoroughfare.md)
  The street address associated with the placemark.
- [var subThoroughfare: String?](./subthoroughfare.md)
  Additional street-level information for the placemark.
- [var subLocality: String?](./sublocality.md)
  Additional city-level information for the placemark.
- [var administrativeArea: String?](./administrativearea.md)
  The state or province associated with the placemark.
- [var subAdministrativeArea: String?](./subadministrativearea.md)
  Additional administrative area information for the placemark.
- [var postalCode: String?](./postalcode.md)
  The postal code associated with the placemark.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/clplacemark/locality)*