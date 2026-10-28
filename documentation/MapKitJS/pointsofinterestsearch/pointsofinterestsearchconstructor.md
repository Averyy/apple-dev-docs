# new PointsOfInterestSearch(options)

**Framework**: MapKit JS  
**Kind**: init  
**Role**: Constructor

Creates a search object for fetching points of interest.

**Availability**:
- MapKit JS 5.45+

## Declaration

```
constructor(options?: PointsOfInterestSearchConstructorOptions);
```

## Discussion

To use search, create an instance of a [`PointsOfInterestSearch`](../pointsofinterestsearch.md). When you initialize a search, you can optionally set properties of the search object by providing a dictionary of [`PointsOfInterestSearchOptions`](../pointsofinterestsearchoptions.md).

## See Also

### Creating a Points of Interest Search
- [interface PointsOfInterestSearchConstructorOptions](../pointsofinterestsearchconstructoroptions.md)
  Options that you provide when creating a points-of-interest search.
- [interface PointsOfInterestSearchOptions](../pointsofinterestsearchoptions.md)
  Options that you may provide when you create a points of interest search.
- [region](./region.md)
  The region that bounds the area in which to fetch points of interest.
- [center](./center.md)
  The center point of the request represented as latitude and longitude.
- [radius](./radius.md)
  The distance provided in meters, or the longest distance derived from the center point to the region’s bounding box.
- [pointOfInterestFilter](./pointofinterestfilter.md)
  A filter that lists points of interest categories to include or exclude.
- [language](../serviceconstructoroptions/language.md)
  A language identifier that determines the language for the service results text.
- [MaxRadius](./maxradius.md)
  The maximum distance to use from the center of the region for fetching points of interest.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/pointsofinterestsearch/pointsofinterestsearchconstructor)*