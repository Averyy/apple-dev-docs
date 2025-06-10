# PlaceDescriptor.PlaceRepresentation

**Framework**: GeoToolbox  
**Kind**: enum

Values that represent a physical place, suitable for use when searching or retrieving rich data.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
enum PlaceRepresentation
```

## Topics

### Place representations
- [var address: String?](placedescriptor/address.md)
  A full address, that one could use in postal or administrative scenarios.
- [var coordinate: CLLocationCoordinate2D?](placedescriptor/coordinate.md)
  The latitude and longitude for a place.
### Enumeration cases
- [PlaceDescriptor.PlaceRepresentation.address(_:)](placedescriptor/placerepresentation/address(_:).md)
  Full address, as you’d use in postal or administrative scenarios.
- [PlaceDescriptor.PlaceRepresentation.coordinate(_:)](placedescriptor/placerepresentation/coordinate(_:).md)
  A physical location described by its latitude and longitude.
- [PlaceDescriptor.PlaceRepresentation.deviceLocation(_:)](placedescriptor/placerepresentation/devicelocation(_:).md)
  Physical location in a coordinate system that a device would collect.
### Operators
- [static func == (PlaceDescriptor.PlaceRepresentation, PlaceDescriptor.PlaceRepresentation) -> Bool](placedescriptor/placerepresentation/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Initializers
- [init(from: any Decoder) throws](placedescriptor/placerepresentation/init(from:).md)
  Creates a new instance by decoding from the given decoder.
### Instance Methods
- [func encode(to: any Encoder) throws](placedescriptor/placerepresentation/encode(to:).md)
  Encodes this value into the given encoder.
### Default Implementations
- [Equatable Implementations](placedescriptor/placerepresentation/equatable-implementations.md)

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [PlaceDescriptor.SupportingPlaceRepresentation](placedescriptor/supportingplacerepresentation.md)
  Values that describe the representation of a physical place using proprietary attributes, such as an alphanumeric location identifier from a mapping service provider.


---

*[View on Apple Developer](https://developer.apple.com/documentation/geotoolbox/placedescriptor/placerepresentation)*