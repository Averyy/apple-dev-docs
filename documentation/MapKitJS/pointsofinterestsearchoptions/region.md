# region

**Framework**: MapKit JS  
**Kind**: property

The region that bounds the area in which to fetch points of interest.

**Availability**:
- MapKit JS 5.45+

## Declaration

```swift
attribute mapkit.CoordinateRegion region;
```

#### Discussion

The system determines the region from the provided bounding box or derives the region from a box enclosing the circle specified by [`center`](pointsofinterestsearchoptions/center.md) and [`radius`](pointsofinterestsearchoptions/radius.md).

## See Also

- [center](pointsofinterestsearchoptions/center.md)
  The center point of the request represented as latitude and longitude.
- [radius](pointsofinterestsearchoptions/radius.md)
  The distance provided in meters, or the longest distance derived from the center point to the region’s bounding box.
- [pointOfInterestFilter](pointsofinterestsearchoptions/pointofinterestfilter.md)
  A filter that lists points of interest categories to include or exclude.
- [language](pointsofinterestsearchoptions/language.md)
  The language ID to use when fetching points of interest.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/pointsofinterestsearchoptions/region)*