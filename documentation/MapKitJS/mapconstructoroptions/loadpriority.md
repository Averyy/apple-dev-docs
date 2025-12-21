# loadPriority

**Framework**: MapKit JS  
**Kind**: property

A value MapKit JS uses for prioritizing the visibility of specific map features before the underlaying map tiles.

**Availability**:
- MapKit JS 5.73+

## Declaration

```swift
loadPriority?: LoadPriority;
```

#### Discussion

Use this property to optimize the map-loading experience and prioritize the visibility of specific map features. The available prioritization options are:

- [`LandCover`](loadpriority/landcover.md) — Prioritizes loading of the map land cover and borders, without points of interest (POIs) or labels. This is the default.
- [`PointsOfInterest`](loadpriority/pointsofinterest.md) — Prioritizes loading of the full standard map, with rendering of POIs.
- [`None`](loadpriority/none.md) — Signifies no preferences over what to prioritize when loading the map.

## See Also

- [const LoadPriority](loadpriority.md)
  Values for prioritizing the visibility of specific map features while the map is loading.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/mapconstructoroptions/loadpriority)*