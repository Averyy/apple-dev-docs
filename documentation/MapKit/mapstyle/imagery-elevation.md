# imagery(elevation:)

**Framework**: MapKit  
**Kind**: method

Creates a map style based on satellite imagery with the elevation characteristics you specify.

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
static func imagery(elevation: MapStyle.Elevation = .automatic) -> MapStyle
```

#### Return Value

A [`MapStyle`](mapstyle.md) with the elevation style you specified.

#### Discussion

> **Note**:  In watchOS, depending on rendering calculations, MapKit may render the map using the Standard map style rather than requested Hybrid or Imagery styles.

 In watchOS, depending on rendering calculations, MapKit may render the map using the Standard map style rather than requested Hybrid or Imagery styles.

## Parameters

- `elevation`: One of the   values that determines how the map renders elevation.

## See Also

- [static func hybrid(elevation: MapStyle.Elevation, pointsOfInterest: PointOfInterestCategories, showsTraffic: Bool) -> MapStyle](mapstyle/hybrid(elevation:pointsofinterest:showstraffic:).md)
  Creates a hybrid map style that includes the elevation, point of interest, and traffic characteristics you specify.
- [static func standard(elevation: MapStyle.Elevation, emphasis: MapStyle.StandardEmphasis, pointsOfInterest: PointOfInterestCategories, showsTraffic: Bool) -> MapStyle](mapstyle/standard(elevation:emphasis:pointsofinterest:showstraffic:).md)
  Creates a standard map style that includes the elevation, point of interest, and traffic characteristics you specify.
- [MapStyle.Elevation](mapstyle/elevation.md)
  Values you use to determine whether a map renders elevation.
- [MapStyle.StandardEmphasis](mapstyle/standardemphasis.md)
  Values that control how the framework emphasizes map features.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mapstyle/imagery(elevation:))*