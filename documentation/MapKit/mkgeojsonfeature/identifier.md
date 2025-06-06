# identifier

**Framework**: MapKit  
**Kind**: property

An optional identifier the class returns as a string.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
var identifier: String? { get }
```

#### Discussion

Note that the GeoJSON specification states that the identifier can be a number or a string. However, this [`identifier`](mkgeojsonfeature/identifier.md) returns as a string.

## See Also

- [var geometry: [any MKShape & MKGeoJSONObject]](mkgeojsonfeature/geometry.md)
  The shape or shapes associated with the GeoJSON feature.
- [var properties: Data?](mkgeojsonfeature/properties.md)
  Optional serialized JSON data that corresponds to the properties key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkgeojsonfeature/identifier)*