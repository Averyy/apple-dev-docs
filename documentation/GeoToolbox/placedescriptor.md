# PlaceDescriptor

**Framework**: GeoToolbox  
**Kind**: struct

A structure that contains identifying information about a place that a mapping service may use to attempt to find rich place information such as phone numbers, websites, and so on.

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
struct PlaceDescriptor
```

#### Discussion

A [`PlaceDescriptor`](placedescriptor.md) allows you to construct a collection of metadata about a place, including at least one [`PlaceDescriptor.PlaceRepresentation`](placedescriptor/placerepresentation.md) which contains common geographic concepts like an address or coordinate. `PlaceDescriptor` may optionally include a [`supportingRepresentations`](placedescriptor/supportingrepresentations.md) which contains identifiers that match the place for mapping service providers. Use `PlaceDescriptor` in conjunction with a mapping service to request rich information about a place.

For example to create a [`PlaceDescriptor`](placedescriptor.md) that describes an address with a common name use [`init(representations:commonName:supportingRepresentations:)`](placedescriptor/init(representations:commonname:supportingrepresentations:).md) as shown here.

```swift
    let fountain = PlaceDescriptor(
        representations: [.address("121-122 James's St \n Dublin 8 \n D08 ET27 \n Ireland")],
        commonName: "Obelisk Fountain"
    )
```

You can also initialize a `PlaceDescriptor` using an [`MKMapItem`](https://developer.apple.com/documentation/MapKit/MKMapItem) as shown below.

```swift
    guard let descriptor = PlaceDescriptor(item: myMapItem) else {
        return
    }
```

## Topics

### Creating place descriptors
- [init(representations: [PlaceDescriptor.PlaceRepresentation], commonName: String?, supportingRepresentations: [PlaceDescriptor.SupportingPlaceRepresentation])](placedescriptor/init(representations:commonname:supportingrepresentations:).md)
  Creates a place descriptor, suitable for use when searching or retrieving rich data about a place.
- [init?(item: MKMapItem)](placedescriptor/init(item:).md)
  Creates a place descriptor from a map item.
### Getting the attributes of a place descriptor
- [let commonName: String?](placedescriptor/commonname.md)
  Publicly known name of the area or place of interest.
- [var address: String?](placedescriptor/address.md)
  A full address, that one could use in postal or administrative scenarios.
- [var coordinate: CLLocationCoordinate2D?](placedescriptor/coordinate.md)
  The latitude and longitude for a place.
- [let representations: [PlaceDescriptor.PlaceRepresentation]](placedescriptor/representations.md)
  An array of representations of the place using common mapping concepts.
- [let supportingRepresentations: [PlaceDescriptor.SupportingPlaceRepresentation]](placedescriptor/supportingrepresentations.md)
  An array of proprietary or non-uniform representations of the place, such as representations you can use with other mapping services.
- [func serviceIdentifier(for: String) -> String?](placedescriptor/serviceidentifier(for:).md)
  Retrieves the identifier for the specified service provider, if available.
### Enumeration values that describe places and mapping service representations
- [PlaceDescriptor.PlaceRepresentation](placedescriptor/placerepresentation.md)
  Values that represent a physical place, suitable for use when searching or retrieving rich data.
- [PlaceDescriptor.SupportingPlaceRepresentation](placedescriptor/supportingplacerepresentation.md)
  Values that describe the representation of a physical place using proprietary attributes, such as an alphanumeric location identifier from a mapping service provider.
### Type Aliases
- [PlaceDescriptor.Specification](placedescriptor/specification.md)
- [PlaceDescriptor.UnwrappedType](placedescriptor/unwrappedtype.md)
- [PlaceDescriptor.ValueType](placedescriptor/valuetype.md)
### Type Properties
- [static var defaultResolverSpecification: some ResolverSpecification](placedescriptor/defaultresolverspecification.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomLocalizedStringResourceConvertible](../Foundation/CustomLocalizedStringResourceConvertible.md)
- [Decodable](../Swift/Decodable.md)
- [DisplayRepresentable](../AppIntents/DisplayRepresentable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [InstanceDisplayRepresentable](../AppIntents/InstanceDisplayRepresentable.md)
- [PersistentlyIdentifiable](../AppIntents/PersistentlyIdentifiable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [TypeDisplayRepresentable](../AppIntents/TypeDisplayRepresentable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/geotoolbox/placedescriptor)*