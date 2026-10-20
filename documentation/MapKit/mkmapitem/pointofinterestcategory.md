# pointOfInterestCategory

**Framework**: MapKit  
**Kind**: property  
**Role**: Instance Property

The point-of-interest category for the map item.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
var pointOfInterestCategory: MKPointOfInterestCategory? { get set }
```

```objc
@property (nonatomic, copy, nullable) MKPointOfInterestCategory pointOfInterestCategory;
```

#### Discussion

If the map item doesn’t correspond to a point of interest, or if the point of interest isn’t one of the known values in [`MKPointOfInterestCategory`](../mkpointofinterestcategory.md), [`pointOfInterestCategory`](./pointofinterestcategory.md) is `nil`.

## See Also

### Accessing the map item attributes
- [MKMapItem.Identifier](./identifier-swift.class.md)
  A unique identifier for a place.
- [var alternateIdentifiers: Set<MKMapItem.Identifier>](./alternateidentifiers.md)
  A set of alternative identifiers for a place.
- [var identifier: MKMapItem.Identifier?](./identifier-swift.property.md)
  A unique identifier for a place.
- [var isCurrentLocation: Bool](./iscurrentlocation.md)
  A Boolean value that indicates whether the map item represents the user’s location.
- [var name: String?](./name.md)
  The descriptive name associated with the map item.
- [var placemark: MKPlacemark](./placemark.md)
  The placemark object containing the location information.
- [var phoneNumber: String?](./phonenumber.md)
  The phone number associated with a business at the specified location.
- [var timeZone: TimeZone?](./timezone.md)
  The time zone of the specified location.
- [var url: URL?](./url.md)
  The URL associated with the specified location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmapitem/pointofinterestcategory)*