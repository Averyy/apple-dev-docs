# hybrid(elevation:pointsOfInterest:showsTraffic:)

**Framework**: Mapkit  
**Kind**: method

Creates a hybrid map style that includes the elevation, point of interest, and traffic characteristics you specify.

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
static func hybrid(elevation: MapStyle.Elevation = .automatic, pointsOfInterest: PointOfInterestCategories = .all, showsTraffic: Bool = false) -> MapStyle
```

#### Return Value

A [`MapStyle`](mapstyle.md) with the configuration you specified.

#### Discussion

> **Note**:  In watchOS, depending on rendering calculations, MapKit may render the map using the Standard map style rather than requested Hybrid or Imagery styles.

## Parameters

- `elevation`: One of the   values that determines whether the map renders elevation.
- `pointsOfInterest`: A collection of   that the map displays.
- `showsTraffic`: A Boolean value that indicates whether the map displays traffic.

## See Also

- [static func imagery(elevation: MapStyle.Elevation) -> MapStyle](mapstyle/imagery(elevation:).md)
  Creates a map style based on satellite imagery with the elevation characteristics you specify.
- [static func standard(elevation: MapStyle.Elevation, emphasis: MapStyle.StandardEmphasis, pointsOfInterest: PointOfInterestCategories, showsTraffic: Bool) -> MapStyle](mapstyle/standard(elevation:emphasis:pointsofinterest:showstraffic:).md)
  Creates a standard map style that includes the elevation, point of interest, and traffic characteristics you specify.
- [MapStyle.Elevation](mapstyle/elevation.md)
  Values you use to determine whether a map renders elevation.
- [MapStyle.StandardEmphasis](mapstyle/standardemphasis.md)
  Values that control how the framework emphasizes map features.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mapstyle/hybrid(elevation:pointsofinterest:showstraffic:))*