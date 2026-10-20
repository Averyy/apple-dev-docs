# MKPlacemark

**Framework**: MapKit  
**Kind**: class  
**Role**: Class

A user-friendly description of a location on the map.

**Availability**:
- iOS 3.0+ - Deprecated in 26.0
- iPadOS 3.0+ - Deprecated in 26.0
- Mac Catalyst 13.1+ - Deprecated in 26.0
- macOS 10.9+ - Deprecated in 26.0
- tvOS 9.2+ - Deprecated in 26.0
- visionOS 1.0+ - Deprecated in 26.0
- watchOS 2.0+ - Deprecated in 26.0

> **Deprecated**: Use MKMapItem's location, address and addressRepresentations properties instead. Use MKAddressRepresentations for formatted address strings for MapKit provided MKMapItems

## Declaration

```swift
class MKPlacemark
```

```objc
@interface MKPlacemark : CLPlacemark
```

#### Overview

Placemark data includes information like the country or region, state, city, and street address associated with the specified coordinate. A placemark is a concrete annotation object and conforms to the [`MKAnnotation`](./mkannotation.md) protocol. Because it’s an annotation, you can add a placemark directly to the map view’s list of annotations.

## Topics

### Creating a placemark object
- [init(coordinate: CLLocationCoordinate2D)](./mkplacemark/init%28coordinate%29.md)
  Creates and returns a placemark object using the specified coordinate.
- [init(coordinate: CLLocationCoordinate2D, postalAddress: CNPostalAddress)](./mkplacemark/init%28coordinate,postaladdress%29.md)
  Creates and returns a placemark object with the specified coordinate and postal address from the user’s Contacts database.
- [init(coordinate: CLLocationCoordinate2D, addressDictionary: [String : Any]?)](./mkplacemark/init%28coordinate,addressdictionary%29.md)
  Creates and returns a placemark object using the specified coordinate and Address Book dictionary.
### Accessing the placemark attributes
- [var countryCode: String?](./mkplacemark/countrycode.md)
  The abbreviated country or region name.

## Relationships

### Inherits From
- [CLPlacemark](../CoreLocation/clplacemark.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [MKAnnotation](./mkannotation.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Shared behavior
- [protocol MKAnnotation](./mkannotation.md)
  An interface for associating your content with a specific map location.
- [class MKAnnotationView](./mkannotationview.md)
  The visual representation of one of your annotation objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkplacemark)*