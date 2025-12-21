# serviceIdentifier(for:)

**Framework**: GeoToolbox  
**Kind**: method

Retrieves the identifier for the specified service provider, if available.

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
func serviceIdentifier(for serviceProvider: String) -> String?
```

## Parameters

- `serviceProvider`: A string that represents the identifier of the service provider to search for.

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/geotoolbox/placedescriptor/serviceidentifier(for:))*