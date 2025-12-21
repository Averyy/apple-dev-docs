# center

**Framework**: MapKit JS  
**Kind**: property

The center point of the request represented as latitude and longitude.

**Availability**:
- MapKit JS 5.45+

## Declaration

```swift
get center(): Coordinate | null;
set center(value: Coordinate | null);
```

## See Also

- [new PointsOfInterestSearch(options)](pointsofinterestsearch/pointsofinterestsearchconstructor.md)
  Creates a search object for fetching points of interest.
- [interface PointsOfInterestSearchConstructorOptions](pointsofinterestsearchconstructoroptions.md)
  Options that you provide when creating a points-of-interest search.
- [interface PointsOfInterestSearchOptions](pointsofinterestsearchoptions.md)
  Options that you may provide when you create a points of interest search.
- [region](pointsofinterestsearch/region.md)
  The region that bounds the area in which to fetch points of interest.
- [radius](pointsofinterestsearch/radius.md)
  The distance provided in meters, or the longest distance derived from the center point to the region’s bounding box.
- [pointOfInterestFilter](pointsofinterestsearch/pointofinterestfilter.md)
  A filter that lists points of interest categories to include or exclude.
- [language](serviceconstructoroptions/language.md)
  A language identifier that determines the language for the service results text.
- [MaxRadius](pointsofinterestsearch/maxradius.md)
  The maximum distance to use from the center of the region for fetching points of interest.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/pointsofinterestsearch/center)*