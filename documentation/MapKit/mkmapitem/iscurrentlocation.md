# isCurrentLocation

**Framework**: MapKit  
**Kind**: property

A Boolean value that indicates whether the map item represents the user’s location.

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
var isCurrentLocation: Bool { get }
```

#### Discussion

If the value of this property is [`true`](https://developer.apple.com/documentation/swift/true), the map item represents the user’s location, and the value in the [`placemark`](mkmapitem/placemark.md) property is `nil`.

## See Also

- [MKMapItem.Identifier](mkmapitem/identifier-swift.class.md)
  A unique identifier for a place.
- [var alternateIdentifiers: Set<MKMapItem.Identifier>](mkmapitem/alternateidentifiers.md)
  A set of alternative identifiers for a place.
- [var identifier: MKMapItem.Identifier?](mkmapitem/identifier-swift.property.md)
  A unique identifier for a place.
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

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmapitem/iscurrentlocation)*