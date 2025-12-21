# representations

**Framework**: GeoToolbox  
**Kind**: property

An array of representations of the place using common mapping concepts.

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
let representations: [PlaceDescriptor.PlaceRepresentation]
```

#### Discussion

When searching or fetching a place from a mapping service provider, the order of the list can be a hint of usefulness for a specific purpose. Representations that most closely match the original data source come first.

For example a hike tracking app may include a `.coordinate` first, even if an approximate `.address` is available. A contacts app may put `.address` first, even if the service provider fetched a `.coordinate` for display on a Map.

## See Also

- [let commonName: String?](placedescriptor/commonname.md)
  Publicly known name of the area or place of interest.
- [var address: String?](placedescriptor/address.md)
  A full address, that one could use in postal or administrative scenarios.
- [var coordinate: CLLocationCoordinate2D?](placedescriptor/coordinate.md)
  The latitude and longitude for a place.
- [let supportingRepresentations: [PlaceDescriptor.SupportingPlaceRepresentation]](placedescriptor/supportingrepresentations.md)
  An array of proprietary or non-uniform representations of the place, such as representations you can use with other mapping services.
- [func serviceIdentifier(for: String) -> String?](placedescriptor/serviceidentifier(for:).md)
  Retrieves the identifier for the specified service provider, if available.


---

*[View on Apple Developer](https://developer.apple.com/documentation/geotoolbox/placedescriptor/representations)*