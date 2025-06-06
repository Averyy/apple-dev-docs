# mapkit.Map.LoadPriorities

**Framework**: MapKit JS  
**Kind**: enum

Values for prioritizing the visibility of specific map features while the map is loading.

**Availability**:
- MapKit JS 5.75+

## Declaration

```swift
interface mapkit.Map.LoadPriorities {
	const string LandCover;
	const string PointsOfInterest;
	const null None;
};
```

## Topics

### Prioritizations
- [LandCover](mapkit.map.loadpriorities/landcover.md)
  Prioritizes loading of the map land cover and borders, without POIs or labels.
- [PointsOfInterest](mapkit.map.loadpriorities/pointsofinterest.md)
  Prioritizes loading of the full standard map, with rendered POIs.
- [None](mapkit.map.loadpriorities/none.md)
  Signifies no preferences over what to prioritize when loading the map.

## See Also

- [loadPriority](mapkit.map/loadpriority.md)
  A value MapKit JS uses for prioritizing the visibility of specific map features before the underlaying map tiles.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/mapkit.map.loadpriorities)*