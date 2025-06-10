# properties

**Framework**: MapKit  
**Kind**: property

Optional serialized JSON data that corresponds to the properties key.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
var properties: Data? { get }
```

#### Discussion

MapKit exposes these optional properties but treats them as opaque.

## See Also

- [var geometry: [any MKShape & MKGeoJSONObject]](mkgeojsonfeature/geometry.md)
  The shape or shapes associated with the GeoJSON feature.
- [var identifier: String?](mkgeojsonfeature/identifier.md)
  An optional identifier the class returns as a string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkgeojsonfeature/properties)*