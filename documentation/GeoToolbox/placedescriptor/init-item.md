# init(item:)

**Framework**: GeoToolbox  
**Kind**: init

Creates a place descriptor from a map item.

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
init?(item: MKMapItem)
```

#### Discussion

Use this method to create a `PlaceDescriptor` from an existing `MKMapItem` as shown here.

```swift

    guard let descriptor = PlaceDescriptor(item: selectedSearchResult) else {
        return
    }
```

Note that it’s possible for this initialization to fail if the system can’t resolve the provided map item.

## Parameters

- `item`: An  .

## See Also

- [init(representations: [PlaceDescriptor.PlaceRepresentation], commonName: String?, supportingRepresentations: [PlaceDescriptor.SupportingPlaceRepresentation])](placedescriptor/init(representations:commonname:supportingrepresentations:).md)
  Creates a place descriptor, suitable for use when searching or retrieving rich data about a place.


---

*[View on Apple Developer](https://developer.apple.com/documentation/geotoolbox/placedescriptor/init(item:))*