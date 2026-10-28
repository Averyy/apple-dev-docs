# placemark

**Framework**: MapKit  
**Kind**: property  
**Role**: Instance Property

The placemark object containing the location information.

**Availability**:
- iOS 6.0+ - Deprecated in 26.0
- iPadOS 6.0+ - Deprecated in 26.0
- Mac Catalyst 13.1+ - Deprecated in 26.0
- macOS 10.9+ - Deprecated in 26.0
- tvOS 9.2+ - Deprecated in 26.0
- visionOS 1.0+ - Deprecated in 26.0
- watchOS 2.0+ - Deprecated in 26.0

> **Deprecated**: Use location, address and addressRepresentations instead

## Declaration

```swift
var placemark: MKPlacemark { get }
```

```objc
@property (nonatomic, readonly) MKPlacemark * placemark;
```

## Discussion

If you create the map item using the [`forCurrentLocation()`](./forcurrentlocation%28%29.md) method, the value of this property is `nil` and the [`isCurrentLocation`](./iscurrentlocation.md) property is [`true`](../../Swift/true.md).

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
- [var pointOfInterestCategory: MKPointOfInterestCategory?](./pointofinterestcategory.md)
  The point-of-interest category for the map item.
- [var phoneNumber: String?](./phonenumber.md)
  The phone number associated with a business at the specified location.
- [var timeZone: TimeZone?](./timezone.md)
  The time zone of the specified location.
- [var url: URL?](./url.md)
  The URL associated with the specified location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmapitem/placemark)*