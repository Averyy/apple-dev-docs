# loadPriority

**Framework**: MapKit JS  
**Kind**: property

A value MapKit JS uses for prioritizing the visibility of specific map features before the underlaying map tiles.

**Availability**:
- MapKit JS 5.75+

## Declaration

```swift
attribute string|null loadPriority;
```

#### Discussion

Use this property to optimize the map-loading experience and prioritize the visibility of specific map features. The available prioritization options are:

- [`LandCover`](mapkit.map.loadpriorities/landcover.md) — Prioritizes loading of the map land cover and borders, without points of interest (POIs) or labels. This is the default.
- [`PointsOfInterest`](mapkit.map.loadpriorities/pointsofinterest.md) — Prioritizes loading of the full standard map, with rendering of POIs.
- [`None`](mapkit.map.loadpriorities/none.md) — Signifies no preferences over what to prioritize when loading the map.

## See Also

- [mapkit.Map.LoadPriorities](mapkit.map.loadpriorities.md)
  Values for prioritizing the visibility of specific map features while the map is loading.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/mapconstructoroptions/loadpriority)*