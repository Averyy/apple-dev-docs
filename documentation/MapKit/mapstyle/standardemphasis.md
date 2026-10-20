# MapStyle.StandardEmphasis

**Framework**: MapKit  
**Kind**: struct  
**Role**: Structure

Values that control how the framework emphasizes map features.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS
- watchOS 10.0+

## Declaration

```swift
struct StandardEmphasis
```

## Topics

### Controlling the map’s emphasis
- [static var automatic: MapStyle.StandardEmphasis](./standardemphasis/automatic.md)
  The default level of emphasis.
- [static var muted: MapStyle.StandardEmphasis](./standardemphasis/muted.md)
  A muted emphasis style, that deemphasizes the map’s imagery.

## See Also

### Creating map styles
- [static func hybrid(elevation: MapStyle.Elevation, pointsOfInterest: PointOfInterestCategories, showsTraffic: Bool) -> MapStyle](./hybrid%28elevation,pointsofinterest,showstraffic%29.md)
  Creates a hybrid map style that includes the elevation, point of interest, and traffic characteristics you specify.
- [static func imagery(elevation: MapStyle.Elevation) -> MapStyle](./imagery%28elevation%29.md)
  Creates a map style based on satellite imagery with the elevation characteristics you specify.
- [static func standard(elevation: MapStyle.Elevation, emphasis: MapStyle.StandardEmphasis, pointsOfInterest: PointOfInterestCategories, showsTraffic: Bool) -> MapStyle](./standard%28elevation,emphasis,pointsofinterest,showstraffic%29.md)
  Creates a standard map style that includes the elevation, point of interest, and traffic characteristics you specify.
- [MapStyle.Elevation](./elevation.md)
  Values you use to determine whether a map renders elevation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mapstyle/standardemphasis)*