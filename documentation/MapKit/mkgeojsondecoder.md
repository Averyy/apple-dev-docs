# MKGeoJSONDecoder

**Framework**: MapKit  
**Kind**: class

An object that decodes GeoJSON objects into MapKit types.

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
class MKGeoJSONDecoder
```

#### Overview

The GeoJSON decoder returns objects that conform to the [`MKGeoJSONObject`](mkgeojsonobject.md) protocol.

## Topics

### Decoding GeoJSON objects
- [func decode(Data) throws -> [any MKGeoJSONObject]](mkgeojsondecoder/decode(_:).md)
  Decodes the provided data into native MapKit types that a map can display.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [Displaying an Indoor Map](displaying-an-indoor-map.md)
  Use the Indoor Mapping Data Format (IMDF) to show an indoor map with custom overlays and points of interest.
- [class MKGeoJSONFeature](mkgeojsonfeature.md)
  The decoded representation of a GeoJSON feature.
- [protocol MKGeoJSONObject](mkgeojsonobject.md)
  Objects that the GeoJSON decoder can return.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkgeojsondecoder)*