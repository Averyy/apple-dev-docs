# MapStyle.StandardEmphasis

**Framework**: MapKit  
**Kind**: struct

Values that control how the framework emphasizes map features.

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
struct StandardEmphasis
```

## Topics

### Controlling the map’s emphasis
- [static var automatic: MapStyle.StandardEmphasis](mapstyle/standardemphasis/automatic.md)
  The default level of emphasis.
- [static var muted: MapStyle.StandardEmphasis](mapstyle/standardemphasis/muted.md)
  A muted emphasis style, that deemphasizes the map’s imagery.

## See Also

- [static func hybrid(elevation: MapStyle.Elevation, pointsOfInterest: PointOfInterestCategories, showsTraffic: Bool) -> MapStyle](mapstyle/hybrid(elevation:pointsofinterest:showstraffic:).md)
  Creates a hybrid map style that includes the elevation, point of interest, and traffic characteristics you specify.
- [static func imagery(elevation: MapStyle.Elevation) -> MapStyle](mapstyle/imagery(elevation:).md)
  Creates a map style based on satellite imagery with the elevation characteristics you specify.
- [static func standard(elevation: MapStyle.Elevation, emphasis: MapStyle.StandardEmphasis, pointsOfInterest: PointOfInterestCategories, showsTraffic: Bool) -> MapStyle](mapstyle/standard(elevation:emphasis:pointsofinterest:showstraffic:).md)
  Creates a standard map style that includes the elevation, point of interest, and traffic characteristics you specify.
- [MapStyle.Elevation](mapstyle/elevation.md)
  Values you use to determine whether a map renders elevation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mapstyle/standardemphasis)*