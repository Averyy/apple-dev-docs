# timeZone

**Framework**: MapKit  
**Kind**: property

The time zone of the specified location.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var timeZone: TimeZone? { get set }
```

#### Discussion

When you search for map items, MapKit populates this field with the time zone information as a convenience. You may also set the time zone for any map items you create.

## See Also

- [MKMapItem.Identifier](mkmapitem/identifier-swift.class.md)
  A unique identifier for a place.
- [var alternateIdentifiers: Set<MKMapItem.Identifier>](mkmapitem/alternateidentifiers.md)
  A set of alternative identifiers for a place.
- [var identifier: MKMapItem.Identifier?](mkmapitem/identifier-swift.property.md)
  A unique identifier for a place.
- [var isCurrentLocation: Bool](mkmapitem/iscurrentlocation.md)
  A Boolean value that indicates whether the map item represents the user’s location.
- [var name: String?](mkmapitem/name.md)
  The descriptive name associated with the map item.
- [var placemark: MKPlacemark](mkmapitem/placemark.md)
  The placemark object containing the location information.
- [var pointOfInterestCategory: MKPointOfInterestCategory?](mkmapitem/pointofinterestcategory.md)
  The point-of-interest category for the map item.
- [var phoneNumber: String?](mkmapitem/phonenumber.md)
  The phone number associated with a business at the specified location.
- [var url: URL?](mkmapitem/url.md)
  The URL associated with the specified location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmapitem/timezone)*