# hybrid

**Framework**: Mapkit  
**Kind**: property

A map style that represents a satellite image of the area, including the paths of roads with their names layered on top.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst ?+
- macOS 14.0+
- tvOS 17.0+
- visionOS ?+
- watchOS 10.0+

## Declaration

```swift
static var hybrid: MapStyle { get }
```

#### Discussion

> **Note**:  In watchOS, depending on rendering calculations, MapKit may render the map using the Standard map style rather than requested Hybrid or Imagery styles.

## See Also

- [static var imagery: MapStyle](mapstyle/imagery.md)
  A map style that represents a satellite image of the area the map displays.
- [static var standard: MapStyle](mapstyle/standard.md)
  A map style that represents the default map presentation, which is a street map that shows the position of all roads and some road names, depending upon the zoom level of the map.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mapstyle/hybrid)*