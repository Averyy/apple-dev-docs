# PlaceDescriptor.SupportingPlaceRepresentation

**Framework**: GeoToolbox  
**Kind**: enum

Values that describe the representation of a physical place using proprietary attributes, such as an alphanumeric location identifier from a mapping service provider.

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
enum SupportingPlaceRepresentation
```

## Topics

### Getting available supporting representations
- [PlaceDescriptor.SupportingPlaceRepresentation.serviceIdentifiers(_:)](placedescriptor/supportingplacerepresentation/serviceidentifiers(_:).md)
  Identifiers that represent a place for different mapping service providers
### Operators
- [static func == (PlaceDescriptor.SupportingPlaceRepresentation, PlaceDescriptor.SupportingPlaceRepresentation) -> Bool](placedescriptor/supportingplacerepresentation/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Initializers
- [init(from: any Decoder) throws](placedescriptor/supportingplacerepresentation/init(from:).md)
  Creates a new instance by decoding from the given decoder.
### Instance Methods
- [func encode(to: any Encoder) throws](placedescriptor/supportingplacerepresentation/encode(to:).md)
  Encodes this value into the given encoder.
### Default Implementations
- [Equatable Implementations](placedescriptor/supportingplacerepresentation/equatable-implementations.md)

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [PlaceDescriptor.PlaceRepresentation](placedescriptor/placerepresentation.md)
  Values that represent a physical place, suitable for use when searching or retrieving rich data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/geotoolbox/placedescriptor/supportingplacerepresentation)*