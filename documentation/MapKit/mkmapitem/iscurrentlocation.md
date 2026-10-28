# isCurrentLocation

**Framework**: MapKit  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, readonly) BOOL isCurrentLocation;
```

## Discussion

If the value of this property is [`true`](../../Swift/true.md), the map item represents the user’s location, and the value in the [`placemark`](./placemark.md) property is `nil`.

## See Also

### Accessing the map item attributes
- [MKMapItem.Identifier](./identifier-swift.class.md)
  A unique identifier for a place.
- [var alternateIdentifiers: Set<MKMapItem.Identifier>](./alternateidentifiers.md)
  A set of alternative identifiers for a place.
- [var identifier: MKMapItem.Identifier?](./identifier-swift.property.md)
  A unique identifier for a place.
- [var name: String?](./name.md)
  The descriptive name associated with the map item.
- [var placemark: MKPlacemark](./placemark.md)
  The placemark object containing the location information.
- [var pointOfInterestCategory: MKPointOfInterestCategory?](./pointofinterestcategory.md)
  The point-of-interest category for the map item.
- [var phoneNumber: String?](./phonenumber.md)
  The phone number associated with a business at the specified location.
- [var timeZone: TimeZone?](./timezone.md)
  The time zone of the specified location.
- [var url: URL?](./url.md)
  The URL associated with the specified location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmapitem/iscurrentlocation)*