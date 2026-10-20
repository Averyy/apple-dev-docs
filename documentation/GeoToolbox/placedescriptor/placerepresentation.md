# PlaceDescriptor.PlaceRepresentation

**Framework**: GeoToolbox  
**Kind**: enum  
**Role**: Enumeration

Values that represent a physical place, suitable for use when searching or retrieving rich data.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
enum PlaceRepresentation
```

## Topics

### Place representations
- [var address: String?](./address.md)
  A full address, that one could use in postal or administrative scenarios.
- [var coordinate: CLLocationCoordinate2D?](./coordinate.md)
  The latitude and longitude for a place.
### Enumeration cases
- [PlaceDescriptor.PlaceRepresentation.address(_:)](./placerepresentation/address%28_%29.md)
  Full address, as you’d use in postal or administrative scenarios.
- [PlaceDescriptor.PlaceRepresentation.coordinate(_:)](./placerepresentation/coordinate%28_%29.md)
  A physical location described by its latitude and longitude.
- [PlaceDescriptor.PlaceRepresentation.deviceLocation(_:)](./placerepresentation/devicelocation%28_%29.md)
  Physical location in a coordinate system that a device would collect.

## Relationships

### Conforms To
- [Decodable](../../Swift/decodable.md)
- [Encodable](../../Swift/encodable.md)
- [Equatable](../../Swift/equatable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Values that describe places and mapping service providers
- [PlaceDescriptor.SupportingPlaceRepresentation](./supportingplacerepresentation.md)
  Values that describe the representation of a physical place using proprietary attributes, such as an alphanumeric location identifier from a mapping service provider.


---

*[View on Apple Developer](https://developer.apple.com/documentation/geotoolbox/placedescriptor/placerepresentation)*