# MKPlacemark

**Framework**: MapKit  
**Kind**: class

A user-friendly description of a location on the map.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.2+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class MKPlacemark
```

#### Overview

Placemark data includes information like the country or region, state, city, and street address associated with the specified coordinate. A placemark is a concrete annotation object and conforms to the [`MKAnnotation`](mkannotation.md) protocol. Because it’s an annotation, you can add a placemark directly to the map view’s list of annotations.

## Topics

### Creating a placemark object
- [init(coordinate: CLLocationCoordinate2D)](mkplacemark/init(coordinate:).md)
  Creates and returns a placemark object using the specified coordinate.
- [init(coordinate: CLLocationCoordinate2D, postalAddress: CNPostalAddress)](mkplacemark/init(coordinate:postaladdress:).md)
  Creates and returns a placemark object with the specified coordinate and postal address from the user’s Contacts database.
- [init(coordinate: CLLocationCoordinate2D, addressDictionary: [String : Any]?)](mkplacemark/init(coordinate:addressdictionary:).md)
  Creates and returns a placemark object using the specified coordinate and Address Book dictionary.
### Accessing the placemark attributes
- [var countryCode: String?](mkplacemark/countrycode.md)
  The abbreviated country or region name.

## Relationships

### Inherits From
- [CLPlacemark](../CoreLocation/CLPlacemark.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [MKAnnotation](mkannotation.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [protocol MKAnnotation](mkannotation.md)
  An interface for associating your content with a specific map location.
- [class MKAnnotationView](mkannotationview.md)
  The visual representation of one of your annotation objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkplacemark)*