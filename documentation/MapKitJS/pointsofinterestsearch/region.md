# region

**Framework**: MapKit JS  
**Kind**: property

The region that bounds the area in which to fetch points of interest.

**Availability**:
- MapKit JS 5.45+

## Declaration

```swift
get region(): CoordinateRegion | null;
set region(value: CoordinateRegion | null);
```

#### Discussion

The system determines the region from the provided bounding box or derives the region from a box enclosing the circle specified by [`center`](pointsofinterestsearchoptions/center.md) and [`radius`](pointsofinterestsearchoptions/radius.md).

## See Also

- [new PointsOfInterestSearch(options)](pointsofinterestsearch/pointsofinterestsearchconstructor.md)
  Creates a search object for fetching points of interest.
- [interface PointsOfInterestSearchConstructorOptions](pointsofinterestsearchconstructoroptions.md)
  Options that you provide when creating a points-of-interest search.
- [interface PointsOfInterestSearchOptions](pointsofinterestsearchoptions.md)
  Options that you may provide when you create a points of interest search.
- [center](pointsofinterestsearch/center.md)
  The center point of the request represented as latitude and longitude.
- [radius](pointsofinterestsearch/radius.md)
  The distance provided in meters, or the longest distance derived from the center point to the region’s bounding box.
- [pointOfInterestFilter](pointsofinterestsearch/pointofinterestfilter.md)
  A filter that lists points of interest categories to include or exclude.
- [language](serviceconstructoroptions/language.md)
  A language identifier that determines the language for the service results text.
- [MaxRadius](pointsofinterestsearch/maxradius.md)
  The maximum distance to use from the center of the region for fetching points of interest.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/pointsofinterestsearch/region)*