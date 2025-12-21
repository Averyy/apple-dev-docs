# language

**Framework**: MapKit JS  
**Kind**: property

A language identifier that determines the language for the service results text.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
language?: string;
```

#### Discussion

If you set a language ID, the service request returns content in the specified language, if available, such as, `fr-CA` or `en-GB`. If you don’t provide a language ID, the service object uses the language ID the system provides to the [`init(options)`](mapkit/init.md) call, or the browser’s default language.

## See Also

- [new PointsOfInterestSearch(options)](pointsofinterestsearch/pointsofinterestsearchconstructor.md)
  Creates a search object for fetching points of interest.
- [interface PointsOfInterestSearchConstructorOptions](pointsofinterestsearchconstructoroptions.md)
  Options that you provide when creating a points-of-interest search.
- [interface PointsOfInterestSearchOptions](pointsofinterestsearchoptions.md)
  Options that you may provide when you create a points of interest search.
- [region](pointsofinterestsearch/region.md)
  The region that bounds the area in which to fetch points of interest.
- [center](pointsofinterestsearch/center.md)
  The center point of the request represented as latitude and longitude.
- [radius](pointsofinterestsearch/radius.md)
  The distance provided in meters, or the longest distance derived from the center point to the region’s bounding box.
- [pointOfInterestFilter](pointsofinterestsearch/pointofinterestfilter.md)
  A filter that lists points of interest categories to include or exclude.
- [MaxRadius](pointsofinterestsearch/maxradius.md)
  The maximum distance to use from the center of the region for fetching points of interest.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/serviceconstructoroptions/language)*