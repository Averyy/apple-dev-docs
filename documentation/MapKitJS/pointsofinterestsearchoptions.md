# PointsOfInterestSearchOptions

**Framework**: MapKit JS  
**Kind**: struct

Options that you may provide when you create a points of interest search.

**Availability**:
- MapKit JS 5.45+

## Declaration

```swift
dictionary PointsOfInterestSearchOptions {
	string language;
	mapkit.Coordinate center;
	number radius;
	mapkit.CoordinateRegion region;
	mapkit.PointOfInterestFilter pointOfInterestFilter;
};
```

## Topics

### Configuring fetch options
- [region](pointsofinterestsearchoptions/region.md)
  The region that bounds the area in which to fetch points of interest.
- [center](pointsofinterestsearchoptions/center.md)
  The center point of the request represented as latitude and longitude.
- [radius](pointsofinterestsearchoptions/radius.md)
  The distance provided in meters, or the longest distance derived from the center point to the region’s bounding box.
- [pointOfInterestFilter](pointsofinterestsearchoptions/pointofinterestfilter.md)
  A filter that lists points of interest categories to include or exclude.
- [language](pointsofinterestsearchoptions/language.md)
  The language ID to use when fetching points of interest.

## See Also

- [mapkit.PointsOfInterestSearch](mapkit.pointsofinterestsearch/mapkit.pointsofinterestsearch.md)
  Creates a search object for fetching points of interest.
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

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/pointsofinterestsearchoptions)*