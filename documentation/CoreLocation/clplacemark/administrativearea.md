# administrativeArea

**Framework**: Core Location  
**Kind**: property

The state or province associated with the placemark.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var administrativeArea: String? { get }
```

#### Discussion

The string in this property can be either the spelled out name of the administrative area or its designated abbreviation, if one exists. If the placemark location is Apple’s headquarters, for example, the value for this property would be the string “CA” or “California”.

## See Also

- [var thoroughfare: String?](clplacemark/thoroughfare.md)
  The street address associated with the placemark.
- [var subThoroughfare: String?](clplacemark/subthoroughfare.md)
  Additional street-level information for the placemark.
- [var locality: String?](clplacemark/locality.md)
  The city associated with the placemark.
- [var subLocality: String?](clplacemark/sublocality.md)
  Additional city-level information for the placemark.
- [var subAdministrativeArea: String?](clplacemark/subadministrativearea.md)
  Additional administrative area information for the placemark.
- [var postalCode: String?](clplacemark/postalcode.md)
  The postal code associated with the placemark.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/clplacemark/administrativearea)*