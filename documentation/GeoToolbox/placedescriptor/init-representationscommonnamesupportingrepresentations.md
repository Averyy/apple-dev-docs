# init(representations:commonName:supportingRepresentations:)

**Framework**: GeoToolbox  
**Kind**: init

Creates a place descriptor, suitable for use when searching or retrieving rich data about a place.

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
init(representations: [PlaceDescriptor.PlaceRepresentation], commonName: String?, supportingRepresentations: [PlaceDescriptor.SupportingPlaceRepresentation] = [])
```

#### Discussion

The `representations` property needs to have at least one member. Sort arrays with original or most accurate representations first.

## Parameters

- `representations`: A list of ways to reference the place using common mapping concepts.
- `commonName`: Publicly known name of the area or place of interest, such as “City Hall”, “Times Square”, or “The New York Public Library”.
- `supportingRepresentations`: List of ways to represent a place that are proprietary or non-uniform, such as a dictionary of mapping service identifiers and their related place identifiers.

## See Also

- [init?(item: MKMapItem)](placedescriptor/init(item:).md)
  Creates a place descriptor from a map item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/geotoolbox/placedescriptor/init(representations:commonname:supportingrepresentations:))*