# alternateIdentifiers

**Framework**: MapKit  
**Kind**: property

A set of alternative identifiers for a place.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
var alternateIdentifiers: Set<MKMapItem.Identifier> { get }
```

## Mentions

- [Identifying unique locations with Place IDs](identifying-unique-locations-with-place-ids.md)

#### Discussion

The identifier for a point of interest may change over time. This property provides a set of alternative identifiers for this map item.

## See Also

- [MKMapItem.Identifier](mkmapitem/identifier-swift.class.md)
  A unique identifier for a place.
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
- [var timeZone: TimeZone?](mkmapitem/timezone.md)
  The time zone of the specified location.
- [var url: URL?](mkmapitem/url.md)
  The URL associated with the specified location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmapitem/alternateidentifiers)*