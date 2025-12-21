# region

**Framework**: MapKit JS  
**Kind**: property

Sets the region that bounds the area in which to fetch points of interest.

**Availability**:
- MapKit JS 5.45+

## Declaration

```swift
region?: CoordinateRegion;
```

#### Discussion

The system determines the region from the provided bounding box or derives the region from a box that encloses the circle specified by [`center`](pointsofinterestsearchconstructoroptions/center.md) and [`radius`](pointsofinterestsearchconstructoroptions/radius.md).

## See Also

- [center](pointsofinterestsearchconstructoroptions/center.md)
  Sets the center point of the request represented as latitude and longitude.
- [radius](pointsofinterestsearchconstructoroptions/radius.md)
  Sets the distance provided in meters, or the longest distance derived from the center point to the region’s bounding box.
- [pointOfInterestFilter](pointsofinterestsearchconstructoroptions/pointofinterestfilter.md)
  Sets a filter that lists points of interest categories to include or exclude.
- [language](serviceconstructoroptions/language.md)
  A language identifier that determines the language for the service results text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/pointsofinterestsearchconstructoroptions/region)*