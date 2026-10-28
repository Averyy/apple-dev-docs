# hybrid(elevation:pointsOfInterest:showsTraffic:)

**Framework**: MapKit  
**Kind**: method  
**Role**: Type Method

Creates a hybrid map style that includes the elevation, point of interest, and traffic characteristics you specify.

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
static func hybrid(elevation: MapStyle.Elevation = .automatic, pointsOfInterest: PointOfInterestCategories = .all, showsTraffic: Bool = false) -> MapStyle
```

## Return Value

A [`MapStyle`](../mapstyle.md) with the configuration you specified.

## Discussion

> **Note**:  In watchOS, depending on rendering calculations, MapKit may render the map using the Standard map style rather than requested Hybrid or Imagery styles.

## Parameters

- `elevation`: One of the [`MapStyle.Elevation`](./elevation.md) values that determines whether the map renders elevation.
- `pointsOfInterest`: A collection of [`PointOfInterestCategories`](../pointofinterestcategories.md) that the map displays.
- `showsTraffic`: A Boolean value that indicates whether the map displays traffic.

## See Also

### Creating map styles
- [static func imagery(elevation: MapStyle.Elevation) -> MapStyle](./imagery%28elevation%29.md)
  Creates a map style based on satellite imagery with the elevation characteristics you specify.
- [static func standard(elevation: MapStyle.Elevation, emphasis: MapStyle.StandardEmphasis, pointsOfInterest: PointOfInterestCategories, showsTraffic: Bool) -> MapStyle](./standard%28elevation,emphasis,pointsofinterest,showstraffic%29.md)
  Creates a standard map style that includes the elevation, point of interest, and traffic characteristics you specify.
- [MapStyle.Elevation](./elevation.md)
  Values you use to determine whether a map renders elevation.
- [MapStyle.StandardEmphasis](./standardemphasis.md)
  Values that control how the framework emphasizes map features.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mapstyle/hybrid(elevation:pointsofinterest:showstraffic:))*