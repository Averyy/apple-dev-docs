# radius

**Framework**: MapKit JS  
**Kind**: property

The distance provided in meters or the longest distance derived from the center point to the region’s bounding box.

**Availability**:
- MapKit JS 5.45+

## Declaration

```swift
readonly attribute number radius;
```

#### Discussion

When fetching points of interest with a region, you may compare this value with [`MaxRadius`](mapkit.pointsofinterestsearch/maxradius.md) to determine if this region is larger than the maximum available radius for a points of interest search.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/mapkit.coordinateregion/radius)*