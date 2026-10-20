# MKGeoJSONFeature

**Framework**: MapKit  
**Kind**: class  
**Role**: Class

The decoded representation of a GeoJSON feature.

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
class MKGeoJSONFeature
```

```objc
@interface MKGeoJSONFeature : NSObject
```

#### Overview

A feature is an object with associated geometry and optional properties in JSON that you define. MapKit exposes these optional properties, but treats them as opaque. [`MKGeoJSONFeature`](./mkgeojsonfeature.md) is one of the classes that the GeoJSON decoder ([`MKGeoJSONDecoder`](./mkgeojsondecoder.md)) can return.

See the GeoJSON standards specification [RFC 7946](https://tools.ietf.org/html/rfc7946#section-3.2) for more information about `Feature` objects.

## Topics

### Feature properties
- [var geometry: [any MKShape & MKGeoJSONObject]](./mkgeojsonfeature/geometry.md)
  The shape or shapes associated with the GeoJSON feature.
- [var identifier: String?](./mkgeojsonfeature/identifier.md)
  An optional identifier the class returns as a string.
- [var properties: Data?](./mkgeojsonfeature/properties.md)
  Optional serialized JSON data that corresponds to the properties key.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [MKGeoJSONObject](./mkgeojsonobject.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Geographical features
- [Displaying an Indoor Map](./displaying-an-indoor-map.md)
  Use the Indoor Mapping Data Format (IMDF) to show an indoor map with custom overlays and points of interest.
- [class MKGeoJSONDecoder](./mkgeojsondecoder.md)
  An object that decodes GeoJSON objects into MapKit types.
- [protocol MKGeoJSONObject](./mkgeojsonobject.md)
  Objects that the GeoJSON decoder can return.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkgeojsonfeature)*