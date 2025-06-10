# MKGeoJSONObject

**Framework**: MapKit  
**Kind**: protocol

Objects that the GeoJSON decoder can return.

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
protocol MKGeoJSONObject : NSObjectProtocol
```

#### Overview

Classes that conform to this protocol represent the types that the GeoJSON decoder can return.

There’s no reason to create your own classes that conform to this protocol; only MapKit can define classes that the GeoJSON decoder uses.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
### Conforming Types
- [MKGeoJSONFeature](mkgeojsonfeature.md)
- [MKGeodesicPolyline](mkgeodesicpolyline.md)
- [MKMultiPoint](mkmultipoint.md)
- [MKMultiPolygon](mkmultipolygon.md)
- [MKMultiPolyline](mkmultipolyline.md)
- [MKPointAnnotation](mkpointannotation.md)
- [MKPolygon](mkpolygon.md)
- [MKPolyline](mkpolyline.md)

## See Also

- [Displaying an Indoor Map](displaying-an-indoor-map.md)
  Use the Indoor Mapping Data Format (IMDF) to show an indoor map with custom overlays and points of interest.
- [class MKGeoJSONDecoder](mkgeojsondecoder.md)
  An object that decodes GeoJSON objects into MapKit types.
- [class MKGeoJSONFeature](mkgeojsonfeature.md)
  The decoded representation of a GeoJSON feature.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkgeojsonobject)*