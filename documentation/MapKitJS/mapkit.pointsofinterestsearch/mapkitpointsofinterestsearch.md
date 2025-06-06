# mapkit.PointsOfInterestSearch

**Framework**: MapKit JS  
**Kind**: init

Creates a search object for fetching points of interest.

**Availability**:
- MapKit JS 5.45+

## Declaration

```swift
new mapkit.PointsOfInterestSearch();
```

#### Discussion

To use search, create an instance of a [`mapkit.PointsOfInterestSearch`](mapkit.pointsofinterestsearch/mapkit.pointsofinterestsearch.md). When you initialize a search, you can optionally set properties of the search object by providing a dictionary of [`PointsOfInterestSearchOptions`](pointsofinterestsearchoptions.md).

## See Also

- [PointsOfInterestSearchOptions](pointsofinterestsearchoptions.md)
  Options that you may provide when you create a points of interest search.
- [region](mapkit.pointsofinterestsearch/region.md)
  The region that bounds the area in which to fetch points of interest.
- [center](mapkit.pointsofinterestsearch/center.md)
  The center point of the request represented as latitude and longitude.
- [radius](mapkit.pointsofinterestsearch/radius.md)
  The distance provided in meters, or the longest distance derived from the center point to the region’s bounding box.
- [pointOfInterestFilter](mapkit.pointsofinterestsearch/pointofinterestfilter.md)
  A filter that lists points of interest categories to include or exclude.
- [language](mapkit.pointsofinterestsearch/language.md)
  The language ID to use when fetching points of interest.
- [MaxRadius](mapkit.pointsofinterestsearch/maxradius.md)
  The maximum distance to use from the center of the region for fetching points of interest.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/mapkit.pointsofinterestsearch/mapkit.pointsofinterestsearch)*