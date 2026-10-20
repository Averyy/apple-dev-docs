# supportingRepresentations

**Framework**: GeoToolbox  
**Kind**: property  
**Role**: Instance Property

An array of proprietary or non-uniform representations of the place, such as representations you can use with other mapping services.

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
let supportingRepresentations: [PlaceDescriptor.SupportingPlaceRepresentation]
```

#### Discussion

This is an array of possible mapping service providers you can use in place of, or in addition to MapKit’s representations.

## See Also

### Getting the attributes of a place descriptor
- [let commonName: String?](./commonname.md)
  Publicly known name of the area or place of interest.
- [var address: String?](./address.md)
  A full address, that one could use in postal or administrative scenarios.
- [var coordinate: CLLocationCoordinate2D?](./coordinate.md)
  The latitude and longitude for a place.
- [let representations: [PlaceDescriptor.PlaceRepresentation]](./representations.md)
  An array of representations of the place using common mapping concepts.
- [func serviceIdentifier(for: String) -> String?](./serviceidentifier%28for%29.md)
  Retrieves the identifier for the specified service provider, if available.


---

*[View on Apple Developer](https://developer.apple.com/documentation/geotoolbox/placedescriptor/supportingrepresentations)*