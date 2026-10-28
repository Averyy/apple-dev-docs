# identifier

**Framework**: MapKit  
**Kind**: property  
**Role**: Instance Property

An optional identifier the class returns as a string.

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
var identifier: String? { get }
```

```objc
@property (nonatomic, readonly, nullable) NSString * identifier;
```

## Discussion

Note that the GeoJSON specification states that the identifier can be a number or a string. However, this [`identifier`](./identifier.md) returns as a string.

## See Also

### Feature properties
- [var geometry: [any MKShape & MKGeoJSONObject]](./geometry.md)
  The shape or shapes associated with the GeoJSON feature.
- [var properties: Data?](./properties.md)
  Optional serialized JSON data that corresponds to the properties key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkgeojsonfeature/identifier)*