# imagery(elevation:)

**Framework**: MapKit  
**Kind**: method  
**Role**: Type Method

Creates a map style based on satellite imagery with the elevation characteristics you specify.

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
static func imagery(elevation: MapStyle.Elevation = .automatic) -> MapStyle
```

#### Return Value

A [`MapStyle`](../mapstyle.md) with the elevation style you specified.

#### Discussion

> **Note**:  In watchOS, depending on rendering calculations, MapKit may render the map using the Standard map style rather than requested Hybrid or Imagery styles.

## Parameters

- `elevation`: One of the [`MapStyle.Elevation`](./elevation.md) values that determines how the map renders elevation.

## See Also

### Creating map styles
- [static func hybrid(elevation: MapStyle.Elevation, pointsOfInterest: PointOfInterestCategories, showsTraffic: Bool) -> MapStyle](./hybrid%28elevation,pointsofinterest,showstraffic%29.md)
  Creates a hybrid map style that includes the elevation, point of interest, and traffic characteristics you specify.
- [static func standard(elevation: MapStyle.Elevation, emphasis: MapStyle.StandardEmphasis, pointsOfInterest: PointOfInterestCategories, showsTraffic: Bool) -> MapStyle](./standard%28elevation,emphasis,pointsofinterest,showstraffic%29.md)
  Creates a standard map style that includes the elevation, point of interest, and traffic characteristics you specify.
- [MapStyle.Elevation](./elevation.md)
  Values you use to determine whether a map renders elevation.
- [MapStyle.StandardEmphasis](./standardemphasis.md)
  Values that control how the framework emphasizes map features.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mapstyle/imagery(elevation:))*