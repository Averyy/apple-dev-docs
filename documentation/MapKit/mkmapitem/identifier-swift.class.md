# MKMapItem.Identifier

**Framework**: MapKit  
**Kind**: class  
**Role**: Class

A unique identifier for a place.

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
class Identifier
```

```objc
@interface MKMapItemIdentifier : NSObject
```

## Topics

### Initializers
- [init?(coder: NSCoder)](./identifier-swift.class/init%28coder%29.md)
- [init?(identifierString: String)](./identifier-swift.class/init%28identifierstring%29.md)
### Instance Properties
- [identifierString](../mkmapitemidentifier/identifierstring.md)
### Instance Methods
- [- initWithIdentifierString:](../mkmapitemidentifier/initwithidentifierstring_.md)

## Relationships

### Inherits From
- [NSObject](../../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../../Swift/cvararg.md)
- [Copyable](../../Swift/copyable.md)
- [CustomDebugStringConvertible](../../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../../Swift/customstringconvertible.md)
- [Decodable](../../Swift/decodable.md)
- [Encodable](../../Swift/encodable.md)
- [Equatable](../../Swift/equatable.md)
- [Escapable](../../Swift/escapable.md)
- [Hashable](../../Swift/hashable.md)
- [NSCoding](../../Foundation/nscoding.md)
- [NSCopying](../../Foundation/nscopying.md)
- [NSObjectProtocol](../../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../../Foundation/nssecurecoding.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)

## See Also

### Accessing the map item attributes
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
- [var pointOfInterestCategory: MKPointOfInterestCategory?](./pointofinterestcategory.md)
  The point-of-interest category for the map item.
- [var phoneNumber: String?](./phonenumber.md)
  The phone number associated with a business at the specified location.
- [var timeZone: TimeZone?](./timezone.md)
  The time zone of the specified location.
- [var url: URL?](./url.md)
  The URL associated with the specified location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmapitem/identifier-swift.class)*