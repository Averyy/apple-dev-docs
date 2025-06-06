# postalCode

**Framework**: Core Location  
**Kind**: property

The postal code associated with the placemark.

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
var postalCode: String? { get }
```

#### Discussion

If the placemark location is Apple’s headquarters, for example, the value for this property would be the string “95014”.

## See Also

- [var thoroughfare: String?](clplacemark/thoroughfare.md)
  The street address associated with the placemark.
- [var subThoroughfare: String?](clplacemark/subthoroughfare.md)
  Additional street-level information for the placemark.
- [var locality: String?](clplacemark/locality.md)
  The city associated with the placemark.
- [var subLocality: String?](clplacemark/sublocality.md)
  Additional city-level information for the placemark.
- [var administrativeArea: String?](clplacemark/administrativearea.md)
  The state or province associated with the placemark.
- [var subAdministrativeArea: String?](clplacemark/subadministrativearea.md)
  Additional administrative area information for the placemark.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/clplacemark/postalcode)*