# name

**Framework**: MapKit  
**Kind**: property

The descriptive name associated with the map item.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.2+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var name: String? { get set }
```

#### Discussion

Use this property to specify the name associated with the location. For example, if there’s a business at the specified location, use this property to specify the name of the business.

If this map item represents the user’s location, the value in this property is a localized version of .

## See Also

- [MKMapItem.Identifier](mkmapitem/identifier-swift.class.md)
  A unique identifier for a place.
- [var alternateIdentifiers: Set<MKMapItem.Identifier>](mkmapitem/alternateidentifiers.md)
  A set of alternative identifiers for a place.
- [var identifier: MKMapItem.Identifier?](mkmapitem/identifier-swift.property.md)
  A unique identifier for a place.
- [var isCurrentLocation: Bool](mkmapitem/iscurrentlocation.md)
  A Boolean value that indicates whether the map item represents the user’s location.
- [var placemark: MKPlacemark](mkmapitem/placemark.md)
  The placemark object containing the location information.
- [var pointOfInterestCategory: MKPointOfInterestCategory?](mkmapitem/pointofinterestcategory.md)
  The point-of-interest category for the map item.
- [var phoneNumber: String?](mkmapitem/phonenumber.md)
  The phone number associated with a business at the specified location.
- [var timeZone: TimeZone?](mkmapitem/timezone.md)
  The time zone of the specified location.
- [var url: URL?](mkmapitem/url.md)
  The URL associated with the specified location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmapitem/name)*