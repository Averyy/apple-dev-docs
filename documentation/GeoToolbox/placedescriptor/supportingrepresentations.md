# supportingRepresentations

**Framework**: GeoToolbox  
**Kind**: property

An array of proprietary or non-uniform representations of the place, such as representations you can use with other mapping services.

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
let supportingRepresentations: [PlaceDescriptor.SupportingPlaceRepresentation]
```

#### Discussion

This is an array of possible mapping service providers you can use in place of, or in addition to MapKit’s representations.

## See Also

- [let commonName: String?](placedescriptor/commonname.md)
  Publicly known name of the area or place of interest.
- [var address: String?](placedescriptor/address.md)
  A full address, that one could use in postal or administrative scenarios.
- [var coordinate: CLLocationCoordinate2D?](placedescriptor/coordinate.md)
  The latitude and longitude for a place.
- [let representations: [PlaceDescriptor.PlaceRepresentation]](placedescriptor/representations.md)
  An array of representations of the place using common mapping concepts.
- [func serviceIdentifier(for: String) -> String?](placedescriptor/serviceidentifier(for:).md)
  Retrieves the identifier for the specified service provider, if available.


---

*[View on Apple Developer](https://developer.apple.com/documentation/geotoolbox/placedescriptor/supportingrepresentations)*