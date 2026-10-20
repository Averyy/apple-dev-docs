# name

**Framework**: MapKit  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, copy, nullable) NSString * name;
```

#### Discussion

Use this property to specify the name associated with the location. For example, if there’s a business at the specified location, use this property to specify the name of the business.

If this map item represents the user’s location, the value in this property is a localized version of *Current Location*.

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

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmapitem/name)*