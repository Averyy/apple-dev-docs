# MapStyle

**Framework**: MapKit  
**Kind**: struct

A style that you can apply to a map.

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
struct MapStyle
```

## Topics

### Creating map styles
- [static func hybrid(elevation: MapStyle.Elevation, pointsOfInterest: PointOfInterestCategories, showsTraffic: Bool) -> MapStyle](mapstyle/hybrid(elevation:pointsofinterest:showstraffic:).md)
  Creates a hybrid map style that includes the elevation, point of interest, and traffic characteristics you specify.
- [static func imagery(elevation: MapStyle.Elevation) -> MapStyle](mapstyle/imagery(elevation:).md)
  Creates a map style based on satellite imagery with the elevation characteristics you specify.
- [static func standard(elevation: MapStyle.Elevation, emphasis: MapStyle.StandardEmphasis, pointsOfInterest: PointOfInterestCategories, showsTraffic: Bool) -> MapStyle](mapstyle/standard(elevation:emphasis:pointsofinterest:showstraffic:).md)
  Creates a standard map style that includes the elevation, point of interest, and traffic characteristics you specify.
- [MapStyle.Elevation](mapstyle/elevation.md)
  Values you use to determine whether a map renders elevation.
- [MapStyle.StandardEmphasis](mapstyle/standardemphasis.md)
  Values that control how the framework emphasizes map features.
### Map styles
- [static var hybrid: MapStyle](mapstyle/hybrid.md)
  A map style that represents a satellite image of the area, including the paths of roads with their names layered on top.
- [static var imagery: MapStyle](mapstyle/imagery.md)
  A map style that represents a satellite image of the area the map displays.
- [static var standard: MapStyle](mapstyle/standard.md)
  A map style that represents the default map presentation, which is a street map that shows the position of all roads and some road names, depending upon the zoom level of the map.

## See Also

- [struct Map](map.md)
  A view that displays an embedded map interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mapstyle)*