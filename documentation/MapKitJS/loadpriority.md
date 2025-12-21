# LoadPriority

**Framework**: MapKit JS  
**Kind**: enum

Values for prioritizing the visibility of specific map features while the map is loading.

**Availability**:
- MapKit JS 5.73+

## Declaration

```swift
const LoadPriority: Readonly<{
    readonly LandCover: "LandCover";
    readonly PointsOfInterest: "PointsOfInterest";
    readonly None: null;
}>
```

## Topics

### Prioritizations
- [LandCover](loadpriority/landcover.md)
  Prioritizes loading of the map land cover and borders, without POIs or labels.
- [PointsOfInterest](loadpriority/pointsofinterest.md)
  Prioritizes loading of the full standard map, with rendered POIs.
- [None](loadpriority/none.md)
  Signifies no preferences over what to prioritize when loading the map.
### Type Aliases
- [type LoadPriority](loadpriority/loadpriority.md)
  A type alias that represents the values of the load priority enumeration.

## See Also

- [loadPriority](map/loadpriority.md)
  A value MapKit JS uses for prioritizing the visibility of specific map features before the underlaying map tiles.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/loadpriority)*