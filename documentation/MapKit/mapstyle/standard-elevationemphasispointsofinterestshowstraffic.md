# standard(elevation:emphasis:pointsOfInterest:showsTraffic:)

**Framework**: MapKit  
**Kind**: method

Creates a standard map style that includes the elevation, point of interest, and traffic characteristics you specify.

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
static func standard(elevation: MapStyle.Elevation = .automatic, emphasis: MapStyle.StandardEmphasis = .automatic, pointsOfInterest: PointOfInterestCategories = .all, showsTraffic: Bool = false) -> MapStyle
```

#### Return Value

A [`MapStyle`](mapstyle.md) with the configuration you specified.

## Parameters

- `elevation`: One of the   values that determines whether the framework renders map elevation.
- `emphasis`: One of the   values that controls how the framework emphasizes map features.
- `pointsOfInterest`: A collection of   displayed on the map.
- `showsTraffic`: A Boolean value that indicates whether the map displays traffic.

## See Also

- [static func hybrid(elevation: MapStyle.Elevation, pointsOfInterest: PointOfInterestCategories, showsTraffic: Bool) -> MapStyle](mapstyle/hybrid(elevation:pointsofinterest:showstraffic:).md)
  Creates a hybrid map style that includes the elevation, point of interest, and traffic characteristics you specify.
- [static func imagery(elevation: MapStyle.Elevation) -> MapStyle](mapstyle/imagery(elevation:).md)
  Creates a map style based on satellite imagery with the elevation characteristics you specify.
- [MapStyle.Elevation](mapstyle/elevation.md)
  Values you use to determine whether a map renders elevation.
- [MapStyle.StandardEmphasis](mapstyle/standardemphasis.md)
  Values that control how the framework emphasizes map features.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mapstyle/standard(elevation:emphasis:pointsofinterest:showstraffic:))*